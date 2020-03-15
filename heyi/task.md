- os.path.dirname(__file__)  这个函数的作用就是返回当前文件的路径
- os.path.join    这个函数的功能是把目录和文件合成一个路径
- open （1，2，'w'）创建写入并读取一个文件；
- 运行代码`with open(os.path.join(os.path.dirname(__file__), private_token_file_name),'r',encoding='utf-8') as f:pirnt(f)` 命令行提示文件未找到
- 整了半天没有明白的是，文件返回目录是做什么用的？join 是把文件和目录合成一个路径，而 open 又是打开一个文件，而且其实命令行以及多次提醒我`File Not Found Error`   始终视而不见呐~~~~ 
最终其实我是被这么多没有见过的函数给吓到了，最关键的执行函数还是 open 嘛，理解了这一点，后面的 file_name 文件名不正好就应该要创建一个与该变量中字符串相符的文件名吗？

- 开始解决字典结构的操作：
    `data['branches'][branch.name] = {'orphan_point_commit_ids': []}`
    #最困惑的是：这个 branch.name 是哪来的。经过调试后发现是gitlab 自带的一个函数。
    进一步想调试的是字典这种数据结构是怎么进行添加以及修改数据的。
     ```
     for branch in branch_list: 
            name['branches'][branch.name]
     ```
    name = {'branchs:{}'}
     创建一个新的字典列表来接收数据，如果字典中没有定义键的话，那么只能储存到一个数据，但是如果定义了一个空的 键的话，就可以储存很多数据了，因为
     `name[ branch.name]`会循环出所有的 name
     而字典的添加是
     >键不可以一样，但值可以相同，也就是说，我每次添加不同的 name 数据是可以被字典保存的
     但是 name[ branch.name],所循环出的结构只会添加到"branch"这个键的值中，要解决这个问题的方法就是，在 branchs 这个键中，每次循环都再添加一个字典，就能循环出所以的 name 了.
     ```
     for i in range(10): 
        name['a'][i]={}
    ```
    尝试自己写了个字典添加的循环，name['a']是对应的键，i是给定的值，但是谁说给定的值不能再是个字典呢
    其实就是在：'a'这个 键中添加了值而已，只不过这个值是一组字典。