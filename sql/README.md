# pages 表：页面表

表的示例数据：

| page_id | page_path    | page_name     |
|---------|-------------|---------------|
| 1       | /home       | 首页          |
| 2       | /product/123| 产品详情页     |
| 3       | /contact    | 联系我们页面    |

表字段介绍：

- page_id：页面 ID
- page_path：页面路径
- page_name：页面名称

# page_views 表：页面访问记录表

表的示例数据：

| view_id | page_id | view_date  | user_ip      | user_id |
|---------|---------|------------|--------------|---------|
| 1       | 1       | 2024-07-01 | 192.168.1.1  | 1       |
| 2       | 2       | 2024-07-01 | 192.168.1.2  | 2       |
| 3       | 1       | 2024-07-02 | 192.168.1.1  | 1       |

表字段介绍：

- view_id：访问记录 ID
- page_id：页面 ID
- view_date：访问日期
- user_ip：用户 IP
- user_id：用户 ID

# users 表：用户表

表的示例数据：

| user_id | user_name | registration_date | gender | age |
|---------|-----------|------------------|--------|-----|
| 1       | 张三      | 2024-01-01       | 男     | 28  |
| 2       | 李四      | 2024-02-15       | 女     | 24  |
| 3       | 王五      | 2024-03-20       | 男     | 30  |

表字段介绍：

- user_id：用户 ID
- user_name：用户名
- registration_date：注册日期
- gender：性别
- age：年龄

# customers 表：客户表

表的示例数据：

| customer_id | name | phone        | created_at           |
|-------------|------|--------------|---------------------|
| 1           | 张三  | 13800138000 | 2023-01-01 10:00:00 |
| 2           | 李四  | 13900139000 | 2023-02-15 14:30:00 |
| 3           | 王五  | 13700137000 | 2023-03-20 08:45:00 |

表字段介绍：

- customer_id：客户ID
- name：姓名
- phone：电话
- created_at：创建时间

# orders 表：订单表

表的示例数据：

| order_id | customer_id | order_date           | total_amount |
|----------|-------------|---------------------|--------------|
| 101      | 1           | 2023-01-15 13:45:00 | 150.00       |
| 102      | 2           | 2023-02-20 11:20:00 | 200.00       |
| 103      | 1           | 2023-03-25 16:10:00 | 120.00       |

表字段介绍：

- order_id：订单ID
- customer_id：客户ID
- order_date：订单日期
- total_amount：总金额

# order_items 表：订单商品表

表的示例数据：

| order_item_id | order_id | product_id | quantity | price  |
|---------------|----------|------------|----------|--------|
| 1001          | 101      | 1          | 2        | 50.00  |
| 1002          | 101      | 2          | 1        | 50.00  |
| 1003          | 102      | 3          | 4        | 50.00  |

表字段介绍：

- order_item_id：订单商品ID
- order_id：订单ID
- product_id：商品ID
- quantity：数量
- price：价格
