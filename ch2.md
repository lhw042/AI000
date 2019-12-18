
##### 目标：
获得所有课程 

- 有多少 Issue
- 各 Issue 有几个回复
- 每个 Issue / 回复, 分别是谁创建/回复的?
- 这种数据比较重要, 需要保存到本地,进一步分析

##### 过程
- 尝试获取issues中的数据:
                
                import requests
                r = requests.get('https://gitlab.com/api/v4/projects/15105057/issues', headers = {"PRIVATE-TOKEN": "qAPAkSBPFz5LD8gGcBA9"})
    
                q = r.json()
    
                for issues in q:
                    print('\n\n\n\n\n\n\n%s'% issues['author'])
  - 发现：得到的数据还是一组字典，需要进一步处理
  - 思考：如何将遍历得到的数据储存在一个变量中进行下一步处理。

- 解决如何将遍历得到的数据储存在一个变量中
        
       for i in range(0,len(q)):
            list.append(q[i].get('author'))
            
       for w in range(0,len(list)):
            name_list.append(list[w].get('name'))
       print(name_list) 
  - 发现：得到了issues的创建者列表
  - 思考：回复的字典内容找不到，怀疑是接口的网址不对

- 找到相关的命令：/projects/:id/issues/.../notes
  - /.../输入的是什么信息？
          
          import requests

          r = requests.get('https://gitlab.com/api/v4/projects/15105057/issues/71/notes', headers = {"PRIVATE-TOKEN": "qAPAkSBPFz5LD8gGcBA9"})
    
          q = r.json()
    
  - 分为两步解决：
    - 获取单个issues的创建回复信息
      
                    name_list = [] 
                    for w in range(len(q)): 
                         name_list.append(q[w].get('author').get('name'))
                    print(len(name_list))
    - 将iid进行循环遍历得出结果

                     for i in iid: 
                         r = requests.get('https://gitlab.com/api/v4/projects/15105057/issues/%d/notes'%(i), headers = {"PRIVATE-TOKEN": "qAPAkSBPFz5LD8gGcBA9"})  
                         
                         q1 = r.json() 
                              
                         for w in range(len(q1)): 
                              list.append(q1[w].get('author').get('name')) 
          发现：得到了一个全是id的列表，有100多个选项
          问题：现在的问题是要循环一个issues获得一个独立的列表，
       - 待解决： 1.在循环过程中将遍历的值保存在一个新列表中，2.遍历过程中将一个列表保存到另外一个列表中，列表套列表。
          - range:可以单独作为一个计数器，也可以在range内部len的一个函数值
             解决昨天的困惑，在使用range函数时要加上0-列表本身，就可以将列表中的数值全部增加到另外一个新列表中
          - 实现列表套列表  :在第一个循环定义一个空列表，在第二个循环将得到的数据append到空列表中，再回到第一个循环将第二个循环得到的列表增加到一个空列表中。

- 解决将得到的数据保存到本地

总结：整个过程中，总是一个小问题一个小问题的去解决，一定不是情绪化的探索，先将目标写下来，接着逐步找解决方案，尝试运行代码，反复这个过程，也就是大妈说的制造已知问题：![](https://i.loli.net/2019/12/18/pnWlokR813sa6eI.png)