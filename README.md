### Scrapy产生步骤:

##### 1, create a scrapy project

> scrapy startproject <project_name>

##### 2, generate a scrapy spider in the project

> scrapy genspider cat domain

##### 3, configuration generated spider 

* scrapy.cfg: 部署scrapy爬虫的配置文件,把爬虫部署到特定的服务器上，并且在服务器配置好相关的操作接口
* settings.py: scrapy爬虫的配置文件
* allowed_domains: 只能爬取这个链接以下的域名链接
* start_urls: scrapy爬取的初始页面url
* parse: 对返回的页面处理响应，解析网页内容形成字典，从网页中发现新url爬取请求

##### 4,run spider

> scrapy runspider <spider_file_path>

#### Scrapy爬虫的使用步骤

* 创建一个工程和Spider模板
* 编写Spider
* 编写Item Pipeline
* 优化配置策略

#### Scrapy爬虫的数据类型

> Request(class scrapy.http.Request())类
    
* Request对象表示一个HTTP请求
* 由Spider生成，由Downloader执行

> Response(class scrapy.http.response())类

* response对象表示一个HTTP响应
* 由Downloader生成，由Spider处理

> Item(class scrapy.http.Item())类

* Item object表示从html页面中提取的信息内容
* 由spider生成，并且由Item Pipeline处理
* Item类似于字典类型，可以按照字典类型操作

#### Scrapy爬虫支持多种html信息提取方法

* BeautifulSoup
* lxml
* re
* CSS Selector(国际公认的html页面的提取方法)
* XPath Selector

#### CSS Selector基本使用

```html
<HTML>.css('a::attr(href)').extract()
            标签名称  标签属性
```

#### 优化爬虫速度

优化scrapy爬虫爬取的速度依赖与scrapy配置文件选项settings.py
一共有4个参数，这些参数都与并非连接有关系.通过改变请求数量改变爬取速率

CONCURRENT_REQUESTS

* Configure maximum concurrent requests performed by Scrapy (default: 16),DOWNLOADER最大并发请求数量

CONCURRENT_ITEMS

* (default value is 100),Item Pipeline最大并发item处理数量

CONCURRENT_REQUESTS_PER_DOMAIN

CONCURRENT_REQUESTS_PER_IP

### yield keyword

* 生成器是一个不断产生值的函数,
* 包含yield语句的函数是一个生成器
* 生成器每次产生一个值(yield语句)，函数被冻结，被唤醒后再产生一个值
* yield from将在一个协程中调用另一个协程，并且得到另一个协程的返回结果

#### generator

一个函数执行到某一个位置产生一个值，然后它被冻结，再次被唤醒的时候还是
从这个位置继续去执行，那么每次执行的时候就可能产生一个数据，这样这个函数
不停的执行就产生了源源不断的数据，这样的函数就叫generator.

generator一般和循环语句一起使用,generator相比一次列出所有内容的advantages

* 更节省存储空间
* 响应更加迅速
* 使用更加灵活

