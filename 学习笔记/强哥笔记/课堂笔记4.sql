-- 创建视图
create view 视图名称 as 查询SQL语句

-- 查看视图
show tables;

-- 重命名视图
rename table 旧视图名 to 新视图名;

-- 修改视图的数据源
create or replace view 视图名称 as 查询SQL语句;

-- 删除视图
drop view 视图名;



-- 事务相关操作
-- 开启事务  以下两种方式都可以
start transaction;
begin;

-- 提交事务
commit;
-- 回滚事务
rollback;



-- 索引相关操作
-- 查看表的索引
show index from 表名;
-- 创建索引
create index 索引名称 on 表名(字段名称(长度))
alter table 表名 add index 索引名称(字段名称(长度))

-- 删除索引
drop index 索引名称 on 表名;


-- 开启时间检测  关闭把1改成0即可
set profiling=1;
-- 显示执行时间
show profiles;






-- 常用的索引有三种 主键索引、普通索引和唯一索引
-- 索引不是越多越好，哪些字段需要建索引呢？主键百分之百用到了索引，就是主键索引；

-- 普通索引key
create index 索引名称 on 表名(字段名称(长度))
alter table 表名 add index 索引名称(字段名称(长度))

-- 唯一索引，unique，保证这个字段只会有一个值；
alter table 表名 add unique index 索引名称(字段名称(长度))
create unique index 索引名称 on 表名(字段名称(长度))



-- 1.虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行insert、update和delete。
--   因为更新表时，不仅要保存数据，还要保存一下索引文件。
-- 2.建立索引会占用磁盘空间的索引文件。一般情况这个问题不太严重，但如果你在一个大表上创建了多种组合索引，
--   索引文件的会增长很快。
--   索引只是提高效率的一个因素，如果有大数据量的表，就需要花时间研究建立最优秀的索引，或优化查询语句。

-- https://www.cnblogs.com/luyucheng/p/6289714.html







-- 创建账号并授权 权限列表包含create、alter、drop、insert、update、delete、select
-- all privileges 表示所有权限
-- 数据库中的全部表则用  数据库.*  某张表用数据库.表名
grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';


-- 修改权限
grant 权限名称 on 数据库 to 账户@主机 with grant option;



-- 修改密码
-- 使用root登录，修改mysql数据库的user表
-- 使用password()函数进行密码加密

update user set authentication_string=password('新密码') where user='用户名';
-- 注意修改完成后需要刷新权限
flush privileges;



-- 备份数据库  注意：需要先退出MySQL客户端
mysqldump –uroot –p密码 数据库名 > 文件名.sql

-- 恢复
-- 连接mysql，创建“新的数据库”
-- 退出连接，执行如下命令
mysql -uroot –p密码 新数据库名 < 文件名.sql