create DATABASE jyoa CHARSET utf8;
use m;

-- 创建系统用户表
CREATE  TABLE sys_user(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) UNIQUE NOT NULL ,
  auth_string VARCHAR(100) NOT NULL ,
  email VARCHAR(50),
  phone VARCHAR(50)
);

-- 创建角色表
CREATE TABLE  sys_role(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE ,
  code VARCHAR(20) NOT NULL UNIQUE
);

-- 创建用户角色表
create TABLE  sys_user_role(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER,
  role_id INTEGER
);

use myhealth;


-- 插入初始管理系统的数据
INSERT INTO sys_user(name, auth_string) VALUES
  ('杨佳伟', '123456'),
  ('张健栋', '123456');

INSERT INTO sys_role(name, code) VALUES
  ('超级管理员', '杨佳伟'),
  ('管理员', '张健栋');

INSERT INTO sys_user_role(id, role_id) VALUES
  (1, 1),
  (2, 2);


-- 查询用户名和对应的角色信息
select
  u.name as user_name,
  r.name as role_name,
  r.code as role_code
from sys_user u
JOIN sys_user_role ur ON (u.id = ur.user_id)
JOIN sys_role r ON (r.id = ur.role_id);


-- 创建分类表（一级，二级）
create TABLE t_category(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) UNIQUE ,
  ord_sn INT,
  parent_id integer DEFAULT 0
);

-- 增加一级分类
insert INTO  t_category(name, ord_sn) VALUES
  ('少儿教育', 1),
  ('初中教育', 2),
  ('高等教育', 3),
  ('艺术教育', 4);

-- 增加二级分类
insert INTO  t_category(name, ord_sn, parent_id) VALUES
  ('少儿童书', 1, 1),
  ('少儿编程', 2, 1),
   ('少儿钢琴', 1, 4);



-- 增加产品表
CREATE TABLE t_product(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200) NOT NULL ,
  cover VARCHAR(200) COMMENT '封面图片路径',
  price FLOAT,
  summary TEXT,
  category_id INTEGER  COMMENT '所属分类ID'
);

insert into t_product(title, price, category_id) VALUES
  ('Python少儿编程基础20课时',2000, 6),
  ('1-3级少儿钢琴24课时',2880, 7);