create database test;

use test;

# 创建索引
create index id on hero(id);

# 查看索引
show index from hero;
desc hero;

# 删除索引
drop index id on hero;

# 创建唯一
	create table tt(
		id int,
        uname varchar(10),
        unique(id)
    );
    
# 创建主键
create table t1(
	id int primary key auto_increment,
    uname varchar(10)
);

create table t2(
	id int auto_increment,
    uname varchar(10),
    primary key(id)
) auto_increment = 1000;   -- 设置自增长起始值

# 删除主键
 -- 先删自增长
alter table t1 modify id int;
 -- 删除主键
alter table t1 drop primary key;

desc t1;
desc t2;

insert into t2 values(null, 'yui');

select * from t2;

# 在已有表中添加主键
alter table t1 add primary key(id);
alter table t1 modify id int auto_increment;

desc t1;


# 创建外键
create table f_t1(
	id int primary key auto_increment,
    f_t2_id int,
    foreign key(f_t2_id) references f_t2(id) on delete cascade on update cascade
);

create table f_t2(
	id int primary key auto_increment,
    uname varchar(10)
) auto_increment=999;

insert into f_t2 values(null, 'aaa'), (null, 'bbb'), (null, 'ccc');
insert into f_t1 values(null, 999), (null, '1000'), (null, 1001);

select * from f_t2;
select * from f_t1;

select * from f_t2
left join f_t1 on f_t2.id=f_t1.f_t2_id;

delete from f_t1 where id=1;
delete from f_t2 where id=999;

# 文件导入
# 1
create table etc_passwd(
	username varchar(20),
    passwd char(1),
    UID int,
    GID int,
    user_detail varchar(50),
    user_index varchar(100),
    user_shell varchar(50)
);

show variables like '%secure%';   -- 寻找secure_file_priv

load data infile "/var/lib/mysql-files/passwd"
into table etc_passwd
fields terminated by ':'
lines terminated by '\n';

select * from etc_passwd;

# 2
create table test_score(
	id int,
    stu_name varchar(20),
    score float,
    phone_num char(11),
    class varchar(7)
);

load data infile "/var/lib/mysql-files/AID1709.csv"
into table test_score
fields terminated by ','
lines terminated by '\n';

select * from test_score;


# 数据导出
select username, UID, GID from etc_passwd
into outfile "/var/lib/mysql-files/passwd_selected.txt"
fields terminated by '\t'
lines terminated by '\n';

# 表的复制
show create table tt;
insert into tt values(1, 'aaa'), (2, 'bbb'), (3, 'ccc'), (4, 'ddd');

create table tt_ select * from tt;   -- 复制 

select * from tt_;

create database test2;












