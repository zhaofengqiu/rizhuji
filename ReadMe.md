# 部署方式
部署方式很简单

## 安装python
## 导入需求库

`pip install -r requirements.txt`

##修改配置文件
```
SMTPPASSWD = "asdfsfwe" 
EMAIL="xxxx@qq.com"
PRODUCT= ['product1'，'product2']
STOPTIME=30 
```
注意这里的邮箱只能qq邮箱。只能填写qq邮箱
`SMTPPASSWD` 这个是qq邮箱的smtp授权码，可以查看这里开启[https://laowangblog.com/qq-mail-smtp-service.html](https://laowangblog.com/qq-mail-smtp-service.html)
`EMAIL` 这个填写你自己的邮箱地址
`PRODUCT`这个是关键，比如你要监控`500G 限量版CN2 GIA`这款就写入`product1`,以此类推，将你需要关注的填入这里即可，下面是对应表

|商品|代码|
|  ----  | ----  |
|500G 限量版CN2 GIA|product1|
|1000G 推荐CN2 GIA|product2|
|1500G 进阶CN2 GIA|product3|
|2000G 高端CN2 GIA|product4|
|3000G 精品CN2 GIA|product5|
|5000G 顶级CN2 GIA|product6|
举个例子，比如我要监控500G 限量版CN2 GIA和1000G 推荐CN2 GIA，那么我只要将PRODUCT修改为`['product1'，'product2']`即可。
最后这个`STOPTIME`就是你每次间隔多久让程序看一次，默认为30，代表30秒
## 运行程序
`python main.py`，即可运行成功

# 效果
![image.png](https://i.loli.net/2020/03/17/7BuyL94tjezODvX.png)