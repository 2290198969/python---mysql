# python-成绩查询-mysql

华大爬取自己成绩：<br>
需要request库和bs4库。<br>
按照postman获取成绩的顺序：<br>
先在<strong Login文件>里输入自己的学号和密码，并从里面的url里获得cookie，<br>
再由之得到<strong>Cookie文件<strong>里地址的cookie，<br>
最后两个cookie一起使用于<strong>GradesSearch文件<strong>获得成绩。<br>
将自己需要的数据提取到<strong>DB文件<strong>里输入好密码的自己的mysql库里。
<br>
<br>
注：<br>
* 记得引用自己的文件的时候写'文件名.名'的前半部分。
* 记得自己建的表名是什么。
* 一步一步cv边学边写。
* 善用ai。
