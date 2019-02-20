# 表连接查询
use test2;

# inner join
select s.s_name, c.c_name from sheng s
join city c on c.cfather_id = s.s_id;

# left join
select s.s_name, c.c_name from sheng s
left join city c on s.s_id = c.cfather_id;

# right join
select s.s_name, c.c_name from sheng s
right join city c on s.s_id = c.cfather_id;

# 显示市区详细信息, 要求市全部显示
select sheng.s_name, city.c_id, city.c_name, xian.x_name from city
left join sheng on sheng.s_id = city.cfather_id
join xian on xian.xfather_id = city.c_id;







