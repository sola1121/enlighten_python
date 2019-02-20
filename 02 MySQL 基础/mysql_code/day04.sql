# 创建用户
# 在配置文件中将bind-address注释掉后

create user 'leimilia'@'%' identified by 'leimilia';

create user 'monkey'@'%' identified by 'monkey';

drop user 'monkey'@'';

# 查看用户表
select user, host from mysql.user;
desc mysql.user;

# 给用户赋予权限
grant select on MOSHOU.* to 'monkey'@'%' with grant option;


use test2;
drop database test2;

create database test2; 

# 模拟银行转账
use test;
create table CCB(
	name varchar(20),
    money float8
);
insert into CCB values("zhuanzhang", 10000);

create table ICBC(
	name varchar(20),
    money float8
);
insert into ICBC values("shoukuan", 4000);

# 开始转账
start transaction;
update CCB set money=5000 where name='zhuanzhang';
update ICBC set money='断电了, 服务器宕机了';
select * from CCB;   -- 因为进入了事务, 所以这里查询到的CCB中的内容还没有更改
rollback;   -- 结束事务, 保证在宕机期间没有发生操作

select * from CCB;   -- 没变

# 存储引擎

show create table CCB;   -- 通过engine=...查看存储引擎

show engines;   -- 查看所有的存储引擎


















