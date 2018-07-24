#### Requests lib的7个主要方法

* requests.request(method, url, **kwargs)  构造一个请求，支撑以下各方法的基础方法
* requests.get() 获取HTML网页的主要方法，对应于HTTP的GET
* requests.head() 获取HTML网页头信息的方法，对应于HTTP的HEAD,获得该资源的头部信息
* requests.post() 向HTML网页提交POST请求的方法，对应于HTTP的POST,请求向URL位置的资源后附加新的数据
* requests.put() 向HTML网页提交PUT请求的方法，对应于HTTP的PUT,覆盖原URL位置的资源
* requests.patch() 向HTML网页提交局部修改请求，对应于HTTP的PATCH,局部更新URL位置的资源，即改变该处资源的部分内容
* requests.delete() 向HTML页面提交删除请求，对应于HTTP的DELETE,请求删除URL位置存储的资源

#### Response对象的属性

* r.status_code HTTP请求的返回状态， 200表示连接成功， 404表示失败
* r.text HTTP响应内容的字符串形式，即， url对应的页面内容
* r.encoding 从HTTP header中猜测的响应内容编码方式(不靠谱),如果header中不存在charset，则认为编码为ISO‐8859‐1
r.text根据r.encoding显示网页内容,所以这个猜测不靠谱
* r.apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式,比较靠谱）
* r.content HTTP响应内容的二进制形式

#### requests库的异常

* requests.ConnectionError 网络连接错误异常，如DNS查询失败、拒绝连接等
* requests.HTTPError HTTP错误异常
* requests.URLRequired URL缺失异常
* requests.TooManyRedirects 超过最大重定向次数，产生重定向异常
* requests.ConnectTimeout 连接远程服务器超时异常
* requests.Timeout 请求URL超时，产生超时异常
* r.raise_for_status() 如果不是200，产生异常 requests.HTTPError

#### PUT和PATCH的区别

    假设URL位置有一组数据UserInfo，包括UserID、 UserName等20个字段

* 需求：用户修改了UserName，其他不变
* 采用PATCH，仅向URL提交UserName的局部更新请求
* 采用PUT，必须将所有20个字段一并提交到URL，未提交字段被删除
* PATCH的最主要好处：节省网络带宽