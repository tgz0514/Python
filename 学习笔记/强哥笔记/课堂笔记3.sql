--mysql day03

-- 查询每种类型中最贵的电脑信息(下面两种方式都可以)
select * from (select cate_name, max(price) as max_price from `goods_new` group by cate_name) as g_new
left join `goods_new` as g on g.cate_name=g_new.cate_name and g.price=g_new.max_price;

-- 行级子查询  将多个字段合成一个行元素,在行级子查询中会使用到行元素
select * from `goods_new` where (cate_name, price) in (
	select cate_name,max(price) from `goods_new` group by cate_name
	);


-- 从商品表拆出来商品分类表需要做的工作
	-- 创建商品分类表
	create table if not exists goods_cates(
	    id int unsigned primary key auto_increment,
	    name varchar(40) not null
	);

	-- 向分类表goods_cates中插入已有数据(下面两种方式都可以)
	insert into goods_cates (name) select cate_name from goods group by cate_name;
	insert into goods_cates (name) select distinct cate_name from goods;

	-- 同步数据 把商品分类表中的id替换goods表中的分类名称
	update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;

	-- 向商品分类表goods_cates插入测试数据
	insert into goods_cates(name) values ('路由器'),('交换机'),('网卡');

	-- 修改商品表中的cate_name字段名为cate_id
	alter table goods change cate_name cate_id int unsigned not null;
	-- 修改商品表中的cate_id为分类表中的外键
	alter table goods add foreign key (cate_id) references goods_cates(id);


-- 从商品表中拆出来品牌表需要做的工作
	-- 创建商品品牌表
	-- 在创建数据表的时候一起插入数据
	-- 注意: 需要对brand_name 用as起别名，否则name字段就没有值
	create table goods_brands (
    	id int unsigned primary key auto_increment,
    	name varchar(40) not null) select brand_name as name from goods group by brand_name;

	-- 同步数据 把商品品牌表中的id替换goods表中的品牌名称
	update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name=b.id;

	-- 向品牌表goods_brands插入测试数据
	insert into goods_brands(name) values ('海尔'),('清华同方'),('神舟');

	-- 修改商品表中的brand_name字段名为brand_id
	alter table goods change brand_name brand_id int unsigned not null;

	-- 修改商品表中的brand_id为品牌表的外键
	alter table goods add foreign key (brand_id) references goods_brands(id);


