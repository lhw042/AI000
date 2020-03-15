import os
import sys
import json
import time
import gitlab

VERSION = '0.0.1'
# 将仓库的 id 号保存到变量中，这么做的目的是什么？
project_id = 16345223
#将 保存有 token 数据的文件名字符串保存到变量中，以便下一步 open 出这个 token
private_token_file_name = "private_token"
#这个变量名的作用又是什么呢？
lastest_version_file_name = "lastest_version.json"


# 新建了一个字典，字典中对应的 key 值都是空的，这个字典的作用是什么呢？  看起来有点像是要用来储存数据的
data = {
    'branches': {},
    'branch_heads': {},
    'commits': {},
    'commit_root_id': None,  # 最早的提交节点 ID
    'issues': {}
}

# 版本号
def get_version():#已读
    return VERSION


#返回 token 字符串
def get_private_token():#已读
    """read the private_token from file"""
    with open(os.path.join(os.path.dirname(__file__), private_token_file_name),
              'r',
              encoding='utf-8') as f:
        return f.readline().strip()

# 这个函数的作用其实就是创建一个 json文件，将 date 字典写进去，用来接收数据的。
def save_data():#已读
    """save data in file"""
    with open(os.path.join(os.path.dirname(__file__),#打开了一个lastest_version.json的文件
                           lastest_version_file_name),#疑问的是这个文件是从哪里来的？
              'w',
              encoding='utf-8') as f:
        json.dump(data, f) #到这里位置只是将 data 这个字典写入json 文件，


def load_data():#未读
    """load data from file"""
    with open(os.path.join(os.path.dirname(__file__),
                           lastest_version_file_name),
              'r',
              encoding='utf-8') as f:
        return json.load(f)


def commit_traverse(branch_name, id):#未读
    """递归遍历分支上的 commit 节点"""
    if id == data['commit_root_id']:
        return
    if len(data['commits'][id]['parent_ids']) == 0:
        if id not in data['branches'][branch_name]['orphan_point_commit_ids']:
            data['branches'][branch_name]['orphan_point_commit_ids'].append(id)
        return
    for parent_id in data['commits'][id]['parent_ids']:
        commit_traverse(branch_name, parent_id)




gl = gitlab.Gitlab('https://gitlab.com', private_token=get_private_token())
project = gl.projects.get(project_id)
#这是 gitlab 的内置函数嘛
branch_list = project.branches.list(all=True)
print(type(branch_list))

for branch in branch_list:
        data['branches'][branch.name] = {'orphan_point_commit_ids': []}
        data['branch_heads'][branch.name] = branch.commit['id']
#这时候这个字典里应该被写入了很多东西了
print(data)

def pull_all():
    """pull all necessary changes AT FIRST..."""
    # 获取所有分支
    gl = gitlab.Gitlab('https://gitlab.com', private_token=get_private_token())
    project = gl.projects.get(project_id)

    # 初始化 branches, branch_heads, commits, commit_root_id
    branch_list = project.branches.list(all=True)
    #不知道这条命令是做什么用的

    for branch in branch_list:
        data['branches'][branch.name] = {'orphan_point_commit_ids': []}
        data['branch_heads'][branch.name] = branch.commit['id']
        branch_commits = project.commits.list(all=True, ref_name=branch.name)
        last_commit_id = None
        for c in branch_commits:
            if c.id not in data['commits']:
                data['commits'][c.id] = {
                    'commit_message': c.message,
                    'commit_created_at': c.created_at,
                    'parent_ids': c.parent_ids,
                    'children_ids': []
                }
                if data['commit_root_id'] is None:
                    data['commit_root_id'] = c.id
                else:
                    if data['commits'][data['commit_root_id']][
                            'commit_created_at'] > c.created_at:
                        data['commit_root_id'] = c.id
            if last_commit_id is not None:
                data['commits'][c.id]['children_ids'].append(last_commit_id)
            last_commit_id = c.id

    # 找出 orphan 分支
    for branch_name, commit_id in data['branch_heads'].items():
        commit_traverse(branch_name, commit_id)

    # 初始化 issues
    issue_list = project.issues.list(all=True)
    for issue in issue_list:
        data['issues'][issue.iid] = {
            'author': issue.author,
            'closed_at': issue.closed_at,
            'created_at': issue.created_at,
            'description': issue.description,
            'discussion_locked': issue.discussion_locked,
            'id': issue.id,
            'iid': issue.iid,
            'state': issue.state,
            'title': issue.title,
            'updated_at': issue.updated_at,
            'user_notes_count': issue.user_notes_count
        }
        discussion_list = issue.discussions.list(all=True)
        data['issues'][issue.iid]['discussions'] = []
        for discussion in discussion_list:
            data['issues'][issue.iid]['discussions'].append({
                'id':
                discussion.id,
                'individual_note':
                discussion.individual_note,
                'notes':
                discussion.attributes['notes']
            })

    save_data()


def print_branches_simple_info():
    """输出所有分支的名称"""
    data = load_data()
    print("branch:")
    for name in data['branches'].keys():
        print("\t", name)


def print_orphan_branches():
    """输出 orphan 分支信息"""
    print("orphan branch:\n")
    for name, attr in data['branches'].items():
        if len(attr['orphan_point_commit_ids']) is 0:
            print("%s is not an orphan branch\n" % name)
        else:
            print("%s is an orphan branch" % name)
            for id in attr['orphan_point_commit_ids']:
                print("    at %s %s:\n    commit message: %s" %
                      (id, data['commits'][id]['commit_created_at'],
                       data['commits'][id]['commit_message']))


def print_orphan_branches_simple_info():
    """输出 orphan 分支的简单信息"""
    data = load_data()
    print("orphan branch:")
    for name, attr in data['branches'].items():
        if len(attr['orphan_point_commit_ids']) > 0:
            print("\t", name)


def issues(iid):
    """show issues info"""
    data = load_data()
    # 此处需要排序
    print("issue %s created by %s at %s" %
          (iid, data['issues'][iid]['author']['name'],
           data['issues'][iid]['created_at']))
    for discussion in data['issues'][iid]['discussions']:
        tab_line = '-------------------------------------------------------------------------\n'
        for note in discussion['notes']:
            if note['system']:
                print("%s SYSTEM NOTE %s \n    by %s at %s" %
                      (tab_line, note['body'], note['author']['name'],
                       note['created_at']))
            else:
                print("%s %s \n    by %s at %s" %
                      (tab_line, note['body'], note['author']['name'],
                       note['created_at']))
            tab_line = '  |-------------------------------------------------------------------------\n'


def issues_count():
    """show the count of issues"""
    data = load_data()
    print('issues: %d' % len(data['issues']))


def issues_title():
    """show issues iid and title"""
    data = load_data()
    print("issues title (%s):" % len(data['issues']))
    for iid, issue in data['issues'].items():
        print("%s %s" % (iid, issue['title']))


def issues_summary():
    """show issues summary"""
    data = load_data()
    print("issues summary:")
    # 此处需要排序
    issues = sorted(data['issues'].items(), key=lambda x: int(x[0]))
    for iid, issue in issues:
        print("issue %s created by %s at %s" %
              (iid, issue['author']['name'], issue['created_at']))
        for discussion in issue['discussions']:
            tab_line = ' '
            for note in discussion['notes']:
                if note['system']:
                    print(
                        "%s SYSTEM NOTE by %s at %s" %
                        (tab_line, note['author']['name'], note['created_at']))
                else:
                    print(
                        "%s USER NOTE by %s at %s" %
                        (tab_line, note['author']['name'], note['created_at']))
                tab_line = '  |'
