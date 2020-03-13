import requests
import sys
import json

p_token = "JwP4Hobx5YpfUsW9jRpk"
#第二个位置参数为 koken
repository = "16345223"
#第一个参数为课程仓库。
issues_url = "https://gitlab.com/api/v4/projects/{}/issues?private_token={}&simple=true?per_page=10&page={}"
#第一个 issues 用到的头
issues_statistics_url = "https://gitlab.com/api/v4/projects/16345223/issues_statistics?access_token=JwP4Hobx5YpfUsW9jRpk"
boards_url = "https://gitlab.com/api/v4/projects/16345223/boards?access_token=JwP4Hobx5YpfUsW9jRpk"
issues_notes_url = "https://gitlab.com/api/v4/projects/16345223/issues/{}/notes?private_token=JwP4Hobx5YpfUsW9jRpk&simple=true"

def get_issues_url():
    issues_content = []
    for i in range(1):
        #做十次循环的目的是什么呢？ 
        url = issues_url.format(repository, p_token,i)
        #逐页保存 issue  不理解的是为什么不一次性保存再来处理呢？ 
        print(url)
        #以上十次循环将 token 课程仓库名，已经循环数字依次打印。
        r = requests.get(url)
        # 等于说这里的 Get 是随着循环的数量，每循环一次 get 一次
        if r.text != '[]':
            issues_content.append(r.json())
            #将json 数据写入 issues_content
        else:
            break
        #此时的 issue_content 变量中的数据类型是什么呢？
        print(issues_content)
    json.dump(issues_content, open('data.json', "w"))
    #print(type(issues_content))
    data3 = json.load(open('data.json'))
    issue_count = 0
    iid = []
    for i in data3:
        for s in i:
            issue_count += 1
            iid.append(s.get('iid'))

    print("一共{}个 issues".format(issue_count))
    return iid
get_issues_url()


