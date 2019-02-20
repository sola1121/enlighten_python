create database MOSHOU;

use MOSHOU;
create table hero(
id int,
name char(15),
sex enum("男","女"),
country char(10)
)default charset=utf8;

use MOSHOU;
insert into hero values
(1,"曹操","男","魏国"),
(2,"小乔","女","吴国"),
(3,"诸葛亮","男","蜀国"),
(4,"貂蝉","女","东汉"),
(5,"赵子龙","男","蜀国"),
(6,"魏延","男","蜀国");

use MOSHOU;
create table sanguo(
id int,
name char(20),
gongji int,
fangyu tinyint unsigned,
sex enum("男","女"),
country varchar(20)
)default charset=utf8;

use MOSHOU;
insert into sanguo values
(1,'诸葛亮',120,20,'男','蜀国'),
(2,'司马懿',119,25,'男','魏国'),
(3,'关6羽',188,60,'男','蜀国'),
(4,'赵云666',200,66,'男','魏国'),
(5,'8孙权',110,20,'男','吴国'),
(6,'貂蝉',666,10,'女','魏国'),
(7,null,1000,99,'男','蜀国'),
(8,'',1005,88,'女','蜀国');
