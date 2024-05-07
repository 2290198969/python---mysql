# python-成绩查询-mysql

华大爬取自己成绩：
需要request库和bs4库。
按照postman获取成绩的顺序：先在Login文件里输入自己的学号和密码，并从里面的url里获得cookie，再由之得到Cookie文件里地址的cookie，最后两个cookie一起使用于GradesSearch文件获得成绩。
将自己需要的数据提取到DB里输入好密码的自己的mysql库里。

注：
* 记得引用自己的文件的时候写'文件名.名'的前半部分。
* 记得自己建的表名是什么。
* 一步一步cv边学边写。
* 善用ai。
