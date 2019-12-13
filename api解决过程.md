- 基本信息
  - tokens:qAPAkSBPFz5LD8gGcBA9
  - 仓库代码：15105057
  - 标头的命令： curl --header "Private-Token: <your_access_token>" https://gitlab.example.com/api/v4/projects
  - 参数的命令：curl https://gitlab.com/api/v4/projects/15105057?private_token=qAPAkSBPFz5LD8gGcBA9
  - 新增两个单词  ：Repository（资料库）    branches(分支)
- 尝试修改
  - 修改后命令：curl --header "Private-Token: qAPAkSBPFz5LD8gGcBA9" https://gitlab.example.com/api/v4/projects

  如果直接运行修改后的命令显示结果为：curl: (6) Could not resolve host: gitlab.example.com
  （      无法解析主机，说明这行命令中的网址是有问题的，example是列子的意思：所以我要改为自己的网址）
  - 修改网址后的命令：curl --header "Private-Token: qAPAkSBPFz5LD8gGcBA9" https://gitlab.com/api/v4/projects
          再次执行后返回许多数据，问题是这些数据是哪里的数据？  

    > 列：{"id":15812018,"description":"Интернет технологии",
    > "name":"Inet Techs","name_with_namespace":"Max Dyrkach / Inet Techs","path":"inet-techs",
    > "path_with_namespa········


          
  - 将网址后缀改为issue：curl https://gitlab.com/api/v4/projects/15105057/issues?private_token=qAPAkSBPFz5LD8gGcBA9

  > {"id":28140164,"iid":62,"project_id":15105057,"title":"[ch2] \u003cZOO.R@tempovoid\u003e (平静地)","description":"## 综述\n- 周一所有成员开始阅读ch2全文并在微信群进行了讨论\n- 尝试获取issue数据并观察型式，以进一步确定采用何种形式保存\n\n## 分析\n- 首先针对3种需要获取的数据类型确定API，拿到返回数据\n    - 一共有多少is·········

  -  将网址后缀改为Repository：curl https://gitlab.com/api/v4/projects/15105057/Repository?private_token=qAPAkSBPFz5LD8gGcBA9
  > {"error":"404 Not Found"}gtdeMacBook-Pro:~ gt$ 


  - 将后缀改为branches：curl https://gitlab.com/api/v4/projects/15105057/branches?private_token=qAPAkSBPFz5LD8gGcBA9
          >{"error":"404 Not Found"}gtdeMacBook-Pro:~ gt$

  - 将后缀改为仓库id:15105057:curl https://gitlab.com/api/v4/projects/15105057?private_token=qAPAkSBPFz5LD8gGcBA9
    >{"id":15105057,"description":"4py 课程主仓库","name":"tasks","name_with_namespace":"101Camp / 4py / tasks","path":"tasks","path_with_namespace":"101camp/4py/tasks","created_at":"2019-10-31T07:38:01.528Z",·········
- 新一轮探索：
    - 分支：curl --header "Private-Token: qAPAkSBPFz5LD8gGcBA9" https://gitlab.com/api/v4/projects/15105057/repository/branches/
    >{"name":"19-pangzi-hello-world","commit":{"id":"dd7bb017958ad4b190b08721e3bdb6b252650bb1","short_id":"dd7bb017","created_at":"2019-11-07T03:15:12.000+00:00","parent_ids":null,"title":"👌 IMPROVE: issue templets","message":"👌 IMPROVE: issue templets","author_name":"ZoomQuiet","author_email":"zoomquiet+git@gmail.com"

    - events：curl --header "Private-Token: qAPAkSBPFz5LD8gGcBA9" https://gitlab.com/api/v4/projects/15105057/events
    > {"project_id":15105057,"action_name":"commented on","target_id":259096158,"target_iid":259096158,"target_type":"Note","author_id":4994689,"target_title":"不理解如何使用api","created_at":"2019-12-12T04:19:35.540Z","note":{"id":259096158,"



  

- 总结：
  - 基本上理解了api的使用，只是还是有一些命令显示404，可能是权限的问题
  - 相关命令：[API resources](https://gitlab.com/help/api/api_resources.md)
  - 下步开始探索基于python的信息获取操作