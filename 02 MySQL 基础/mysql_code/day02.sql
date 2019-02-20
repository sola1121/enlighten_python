select * from sanguo where name is null and sex='男' and country='蜀国';   -- 查看null(空值)

select * from sanguo where name="" and sex='女' and country='蜀国';   -- 查看空字符串

# 正则表达式
select * from sanguo where name regexp"[0-9]";   -- 匹配名字中带数字的
select * from sanguo where name regexp"^[0-9]";   -- 匹配名字以数字开头的
select * from sanguo where name regexp"[0-9]$";   -- 匹配名字以数字结尾的
select * from sanguo where name regexp"^司.*懿$";   -- 匹配以'司'开头'懿'结尾中间任何字符或无字符的名字
select * from sanguo where name regexp"^...&";   -- 匹配一个字符, ^.以一个字符开头, .$以一个字符结尾, 按照字节来

# order by
select * from sanguo order by fangyu;
select * from sanguo order by gongji desc;

select * from sanguo 
	where sex='男' and country in('魏国', '蜀国') and name like '___' 
    order by fangyu;

# limit
select * from sanguo
	where country='蜀国'
    order by fangyu
    limit 1, 3;   -- 防御倒数第二到第四的三个人

select name, fongji, country from sanguo 
	where name is not null and country='蜀国'
    order by gongji desc
    limit 0, 3;

# 聚合函数
select max(gongji) as 最高攻击 from sanguo;

select count(id) id数, count(name) name数 from sanguo;

select count(*) 蜀国中攻击大于200 from sanguo where gongji>200 and country='蜀国';

# group by
select country, count(*) 人数 from sanguo 
	group by country   -- 每个国中有几个人
    order by 2 desc
    limit 0, 2;   -- 显示最多前两名人数

select country, avg(gongji) 平均攻击 from sanguo group by country;

# having
select country, avg(gongji) 平均攻击 from sanguo   -- 平均攻击力大于105的国家的前2名, 显示国家名称和平均攻击力
	group by country
	having avg(gongji) > 105
    order by 2 desc
    limit 2;

# distinct
select distinct country from sanguo;

select count(distinct name) from sanguo where country="蜀国";   -- 蜀国中不重名有多少个人

# 使用索引试试
use indexdb;

select * from t1;


show variables like "%pro%";


