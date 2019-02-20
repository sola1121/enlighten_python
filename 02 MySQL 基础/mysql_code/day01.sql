# show databases;   # 显示所有库

# create database use_info default charset=utf8;   # 创建一个新库

# use use_info;   # 切换到新库

# show create database use_info;   # 查看创建库的命令

# select database();   # 显示当前库

# create database use_info1 default charset=utf8;   # 创建一个新库

# use use_info1;   # 切换到新库

# select database();   # 显示当前库

# show tables;   # 显示当前库中的表

# drop database use_info1;   # 删除库

# 创建表
# use use_info;
# select database();
-- CREATE TABLE hello (
--     stu_id INT PRIMARY KEY,
--     stu_name VARCHAR(20) NOT NULL,
--     stu_other VARCHAR(100)
-- )  DEFAULT CHARSET=UTF8;
# desc hello;   # 查看表结构
# drop table hello;   # 删除表

# 在表中插入数据
# use use_info; 
# insert into hello values(1, 'kizuna_ai', '天才');
# insert into hello values(2, 'siro', '海豚'), (3, 'luna', '仓鼠');
# insert into hello(stu_id, stu_name) values(4, 'akari'), (5, 'yomemi');

select * from hello;











