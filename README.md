## Scrapy

### 产生步骤:

#### 1, create a scrapy project

> scrapy startproject <project_name>

#### 2, generate a scrapy spider in the project

> scrapy genspider cat domain

#### 3, configuration generated spider 

* scrapy.cfg: 部署scrapy爬虫的配置文件,把爬虫部署到特定的服务器上，并且在服务器配置好相关的操作接口
* settings.py: scrapy爬虫的配置文件
* allowed_domains: 只能爬取这个链接以下的域名链接
* start_urls: scrapy爬取的初始页面
* parse: 处理响应，解析网页内容形成字典，从网页中发现新url爬取请求

#### 4,run spider

> scrapy runspider <spider_file_path>