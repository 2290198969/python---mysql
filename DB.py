import pymysql
import GradesSearch

# 创建连接
db = pymysql.connect(host='localhost', user='root', password='password',db='GSearch',charset='utf8')

# 创建游标对象
cursor1 = db.cursor() 

# 数据准备
data4 = GradesSearch.data2

# 建立数据表
create_table_sql = """
CREATE TABLE IF NOT EXISTS test10086 (
    id INT AUTO_INCREMENT,
    KCM CHAR(255) NOT NULL,
    XF FLOAT NOT NULL,
    ZCJ INT NOT NULL,
    XSZCJMC CHAR(255) NOT NULL,
    KCXZDM_DISPLAY CHAR(255) NOT NULL,
    PRIMARY KEY (id)
)  ENGINE=INNODB DEFAULT CHARSET=utf8;
"""
cursor1.execute(create_table_sql)

#遍历数据并插入库
for item in GradesSearch.values:
    insert_sql = "INSERT INTO test10086 (KCM, XF, ZCJ, XSZCJMC, KCXZDM_DISPLAY) VALUES (%s, %s, %s, %s, %s)"

    try:
       cursor1.execute(insert_sql, (item['KCM'], item['XF'], item['ZCJ'], item['XSZCJMC'], item['KCXZDM_DISPLAY']))
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()

#打印内容
select_sql = "SELECT * FROM test10086"
cursor1.execute(select_sql)

# 使用 fetchall() 方法获取所有数据.
results = cursor1.fetchall()
for row in results:
    kcm = row[1]
    xf = row[2]
    zcj = row[3]
    xszcjmc = row[4]
    kczdm_display = row[5]

    print(f"课程名={kcm}, 学分={xf}, 总成绩={zcj}, 评级={xszcjmc}, 选必修={kczdm_display}")

# 关闭游标和数据库连接
cursor1.close()
db.close()