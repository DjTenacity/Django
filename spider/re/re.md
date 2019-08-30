Python 里 re 模块有两种方式:
#### 将正则表达式 编译成一个Pattern规则对象
pattern = re.compile("\d")

从起始位置开始往后面查找,返回第一个符合条件的
pattern.match("1234");

从任何位置开始往后查找,返回第一个符合规则的
pattern.search( );

所有的全部匹配,返回列表
pattern.findall( );
所有的全部匹配,返回一个迭代器
pattern.finditer( );

分割字符串,返回列表
pattern.split( );

替换
pattern.sub( );


re.I  忽略大小写
re.S   全文匹配

search(str ,begin ,end)
