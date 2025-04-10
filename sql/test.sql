1.查询访问记录表中所有页面的页面 ID 和访问日期
SELECT page_id, view_date FROM page_views;

2.查询页面表中页面路径为 '/home' 的页面名称
SELECT page_name FROM pages WHERE page_path="/home";

3.查询访问记录表中用户IP为 '192.168.1.1' 的所有记录
SELECT * FROM page_views WHERE user_ip="192.168.1.1";

4.查询用户表中性别为 '男' 的所有用户的用户名
SELECT user_name FROM users WHERE gender="男";

5.查询页面表中所有页面的页面 ID，并按页面 ID 升序排序
SELECT page_id FROM pages ORDER BY page_id ASC;

6.查询访问记录表中每个页面的总访问次数
SELECT page_id, COUNT(*) AS total_views FROM page_views GROUP BY page_id;

7.查询用户表中注册日期最早的 3 个用户的用户名和注册日期
SELECT user_name, registration_date FROM users ORDER BY registration_date ASC LIMIT 3;

8.查询访问记录表中每个用户的总访问次数
SELECT user_id, COUNT(*) AS total_visits FROM page_views GROUP BY user_id;

9.查询用户表中年龄在 25 岁及以下的所有用户的用户名和年龄
SELECT user_name, age FROM users WHERE age <= 25;

10.查询用户表中每个性别的用户数量
SELECT gender, COUNT(*) AS user_count FROM users GROUP BY gender;

11.查询用户表中年龄在 25 岁及以下且性别为 '女' 的用户的用户名
SELECT user_name FROM users WHERE age <= 25 AND gender="女";

12.查询用户表中注册日期在 2024 年 1 月 1 日之后的用户名和注册日期
SELECT user_name registration_date FROM users registration_date > "2024-01-01";

13.查询用户表中用户名包含 '张' 字的所有用户
SELECT * FROM users WHERE user_name LIKE "%张%";

14.查询所有用户中年龄最大的用户信息
SELECT user_name, registration_date, gender, age FROM users ORDER BY age DESC LIMIT 1;

15.查询用户表中每个性别的平均年龄，并按性别分组
SELECT gender, AVG(age) AS average_age FROM users GROUP BY gender;

16.查询用户表中，注册日期在 2024 年 1 月 1 日和 2024 年 6 月 30 日之间的所有用户
SELECT user_name, registration_date FROM users WHERE registration_date BETWEEN "2024-01-01" AND "2024-06-30";

17.查询每个页面的第一次访问日期
SELECT page_id, MIN(view_date) AS first_view_date FROM page_views GROUP BY page_id;

18.查询访问记录表中，每个页面最近一次访问的日期
SELECT page_id, MAX(view_date) AS last_view_date FROM page_views GROUP BY page_id;

19.查询所有订单的总金额和订单日期
SELECT tatal_amount, order_date FROM orders;

20.统计共有多少客户
SELECT COUNT(*) AS customer_count FROM customer;

21.查询总金额大于 100 的所有订单
SELECT * FROM orders WHERE total_amount > 100;

22.按创建时间升序查询所有客户
SELECT * FROM customers ORDER BY created_at ASC;

23.查询订单总金额的平均值
SELECT AVG(total_amount) AS average_total_amount FROM orders;

24.查询每个订单的总商品数量
SELECT order_id, SUM(quantity) AS total_quantity FROM order_items GROUP BY order_id;

25.查询最早的订单日期
SELECT order_id, MIN(order_date) AS earliest_order_date FROM orders;

26.查询创建时间在 2023 年 2 月份的所有客户
SELECT name, phone, created_at FROM customers WHERE created_at BETWEEN "2023-02-01" AND  2023-02-28 23:59:59;

27.查询价格最高的商品信息
SELECT product_id, MAX(price) AS hightest_price FROM order_items GROUP BY price; 这个需要确定
SELECT product_id, price FROM order_items ORDER BY price DESC LIMIT 1;

28.查询所有客户的姓名和创建时间，结果按照创建时间降序排序
SELECT name, created_at FROM customers ORDER BY created_at DESC;

29.查询每个订单的详细商品信息，包括商品 ID、数量、价格和总金额
SELECT oi.order_id, oi.product_id, oi.quantity, oi.price, (oi.quantity * oi.price) AS total_amount FROM order_items oi;

30.查询每个商品的销售总数量及其对应的订单总金额
SELECT oi.product_id, SUM(oi.quantity) AS total_quantity, SUM(oi.quantity * oi.price) AS total_amount FROM order_items oi GROUP BY oi.product_id;

31.查询所有客户的姓名，并将其姓名转换为大写
SELECT UPPER(name) AS upper_case_name FROM customers;

32.查询所有客户的姓名和电话
SELECT name, phone FROM customer;
