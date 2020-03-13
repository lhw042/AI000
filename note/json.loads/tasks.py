from invoke import task,run
import json
@task
def upt(c):
    """更新数据"""
    cmd = 'curl https://gitlab.com/api/v4/projects/16345223/issues/85/discussions/?private_token=EtSyPqsfw8C51RnojERA > issues.json'
    #`> branches.json`这条命令可以将 invoke 运行的内容保存到一个 josn 文件中
    # > branches 这个前啜可以任意指定，文件的数据会被覆盖。
    run(cmd)
@task
def brs(c):
    f = open("branches.json")
    #打开文件，这里考虑一下如果直接打印这个 f 会是什么 打印后是一个 f-8编码的文件
    with open("issues.json",'r') as f:
        name = f.read()
    list_n = json.loads(name)
    #  这个 json.loads 的功能是将 name这个变量转换为列表的形式
    # 用 print打印 name 这个变量的类型是 str，
    # 调用 loads这个功能后类型就变成了列表。
    print(name)
    print(type(name))
    print(type(list_n))