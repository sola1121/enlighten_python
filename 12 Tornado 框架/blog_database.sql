# 在终端中help的帮助使用
# help create database;
# help create table;

create database blog_db default charset=utf8;

use blog_db;

# 用户表
create table tb_user(
	user_id int auto_increment primary key,
	user_name varchar(32) not null unique,
    user_pass varchar(64) not null,
    user_avatar varchar(128) default null,
    user_city varchar(32) not null,
    user_createdate datetime default current_timestamp,
    user_updatedate datetime default current_timestamp on update current_timestamp
)default charset=utf8;

# 博客表
create table tb_blog(
	blog_id int auto_increment primary key,
    blog_user_id int not null,
    blog_title varchar(256) not null,
    blog_content text not null,
	blog_createdate datetime default current_timestamp,
    blog_updatedate datetime default current_timestamp on update current_timestamp,
    foreign key(blog_id) references tb_user(user_id) on delete cascade on update cascade   -- 删除级联, 更新级联
)default charset=utf8;

# 标签表
create table tb_tag(
	tag_id int auto_increment primary key,
    tag_content varchar(16) not null unique
)default charset=utf8;

# 博客标签表
create table tb_blog_tag(
	bolg_tag_id int auto_increment primary key,
    rel_blog_id int not null,
    rel_tag_id int not null,
    foreign key(rel_blog_id) references tb_blog(blog_id) on delete cascade on update cascade,
    foreign key(rel_tag_id) references tb_tag(tag_id) on delete cascade on update  cascade
)default charset=utf8;

# 评论内容
create table tb_comment(
	comment_id int auto_increment primary key,
    comment_blog_id int not null,
    comment_user_id int not null,
    comment_content varchar(256) not null,
    comment_createdate datetime default current_timestamp,
    comment_updatedate datetime default current_timestamp,
    foreign key(comment_blog_id) references tb_blog(blog_id) on delete cascade on update cascade,
    foreign key(comment_user_id) references tb_user(user_id) on delete cascade on update cascade
)default charset=utf8;

# ==========插入数据===========
insert into tb_user(user_name, user_pass, user_city) value('luna','123','vitual_world');
insert into tb_user(user_name, user_pass, user_city) value('siro','123','computer_world');
insert into tb_user(user_name, user_pass, user_city) value('kizuna_ai','123','vitual_world');
insert into tb_user(user_name, user_pass, user_city) value('akari', '123', 'vitual_world');
insert into tb_user(user_name, user_pass, user_city) value('nora_cat', '123', 'vr_world');
insert into tb_user(user_name, user_pass, user_city) value('nojia', '123', 'supermarket');
insert into tb_user(user_name, user_pass, user_city) value('hinata', '123', 'cat_world');
insert into tb_user(user_name, user_pass, user_city) value('yomemi', '123', 'computer_world');
insert into tb_user(user_name, user_pass, user_city) value('tanaka', '123', 'vitual_world');
insert into tb_user(user_name, user_pass, user_city) value('moemi', '123', 'computer_world');

# -----------------------------------------------


# 查询city在computer_world或vr_world的用户
select * from tb_user where user_city in ('computer_world', 'vr_world');

# 查询表中2018-7-3 15:50:00 至 2018-7-3 15:54:00之间注册的用户
select * from tb_user where user_createdate between '2018-7-3 15:50:00' and '2018-7-3 15:54:00';  -- 日期格式字符会被转换

# 从用户表中找到最晚的注册时间
select max(user_createdate) from tb_user;

# 查询每个城市的最晚注册时间
select user_city, max(user_createdate) from tb_user group by 1;

# 查询用户表中最晚注册用户的信息
select * from tb_user where user_createdate = (select max(user_createdate) from tb_user);

# 从用户表中查询每个城市的最晚注册用户的信息
select * from tb_user where user_createdate in (select max(user_createdate) from tb_user group by user_city);

# 查询博客名和其对应作者名
select blog_title, user_name, b.blog_createdate from tb_blog b
join tb_user u on b.blog_user_id = u.user_id;

# 查询所有bolg机器作者信息, 查询时, 将同一作者的文章放在一行中
select user_name, group_concat(blog_title) from tb_blog
join tb_user on tb_user.user_id = tb_blog.blog_user_id
group by 1;

# 查询所有用户及其写的博客
select user_name, blog_title from tb_user u
left outer join tb_blog b on u.user_id = b.blog_user_id;

# 查询所有博客及其标签
select blog_title, group_concat(tag_content) from tb_blog b
left join tb_blog_tag bt on b.blog_id = bt.rel_blog_id
left join tb_tag t on t.tag_id = bt.rel_tag_id
group by 1;

# 查询所有的博客及其标签信息和作者信息
select user_name, blog_title, group_concat(tag_content) from tb_blog b
join tb_user u on u.user_id = b.blog_user_id
left join tb_blog_tag bt on b.blog_id = bt.rel_blog_id
left join tb_tag t on t.tag_id = bt.rel_tag_id
group by 1, 2;

# 查询对应博客的用户名, 博客标题, 博客内容, 评论数, 用户avatar, 更新时间, 并按更新时间由大到小排序
select user_name, user_avatar, blog_title, blog_content ,comm_count, blog_updatedate from tb_blog b
join tb_user u on u.user_id = b.blog_user_id
left join (select comment_blog_id, count(*) as comm_count from tb_comment group by comment_blog_id) com on com.comment_blog_id = b.blog_id;

# 查询对应博客的用户名, 博客标题, 博客内容, 评论数, 用户avatar, 更新时间, 标签
select user_name, user_avatar, blog_title, blog_content ,comm_count, tag_con, blog_updatedate from tb_blog b
join tb_user u on u.user_id = b.blog_user_id
left join (select comment_blog_id, count(*) as comm_count from tb_comment group by comment_blog_id) com on com.comment_blog_id = b.blog_id
left join (
	select blog_id, group_concat(tag_content) as tag_con from tb_blog b
	left join tb_blog_tag bt on bt.rel_blog_id = b.blog_id
	join tb_tag t on t.tag_id = bt.rel_tag_id
	group by blog_id
) tag on tag.blog_id = b.blog_id
order by blog_updatedate desc;

# 以上使用联合查询, 要点是将一个查询的结果当做一个临时表交给另一个查询