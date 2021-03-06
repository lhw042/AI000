# 什么是For循环？
- 基本格式：

                for i in (xx):
  - 疑问：第一个参数是什么意思？
    >for i in （xx）

    xx是作为一个循环的目标，如果在接下来继续打印这一函数，那么结果就是在这个打印这个列表中共有几个元素的次数；比如这个列表中有5个字符串，那么我将列表作为循环中的打印就是整个列表循环5次。
    那么现在再来思考第一个参数是什么意思呢？：第一个参数只是一个循环的条件，必须有一个变量名来让print函数打印，不然如果打印xx 那就重复了。
    - 思考：如果将i这个变量名换为一个空的列表名，那么循环过程中的函数会不会直接保存到这个空列表中？
    - 发现：结果不会得到整个列表，而是得到循环结束后的最后一个字符串
    - 总结：对for循环有了基础的了解，for循环就像星期一的内务卫生检查，会把每个柜子都打开来看看，如果是将整个列表都放到打印中去，那就是开整个房间和柜子的总数
  - 疑问：range函数是什么意思？
    - range可以创建一个整数列表 并且可以返回列表对应的值range(len(list))
    如果要返回的是列表对应的值就在list边上增加一个[x]
    - example:
    
                    for i in range(len(q)):
                        print(q[i])
                        #得到的结果就是i对应的编码内容，如果直接打印：
                        print(i)
                        #得到的就是对应的数字编码。
    - 总结：这个函数像一个编码器，将凌乱的柜子和对应的内容做了一个编排，方便后面的提取
  - 疑问 get在列表中的应用：

    Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值
    这里的get取值和字典列表取值有点不同，字典列表取值用的都是【】
    思考一个问题：列表取值是否可以用get方法
    发现：get是用来取字典中的值的，列表不用get来取值，因为get取值要输入key
    发现：get连用可以取到字典中的字典的值  example:

                    for i in range(len(q)): 
                        print(q[i].get('author').get('name')) 
                        #并且不会重复得到上一个的结果。