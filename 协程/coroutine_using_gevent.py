"""
协程的3种实现：
Python中协程的实现：

yield（最原始的方法）
grennlet（模块）
√gevent（模块）

这是用yiled实现生产者消费者模型，这个模型也可以用多线程+线程队列实现，不过有点区别，在于：

yiled实现的c和p之间没有中介，通过send和yiled直接收发数据，一边发另一边同一时间收到，不存在一边先放到队列里，另一边再去取，队列里可以堆起来这样……产品不能保存，即使消费

这样假如p的生产速度很快，也是要等c消费以后才能继续下一个

"""

import requests,time
import gevent
start_time=time.time()

def f(url):
	res=requests.get(url)
	res.raise_for_status()
	data=res.text
	print('len(data)',len(data))



url1='http://www.baidu.com'
url2='http://www.taobao.com'
url3='http://www.sina.com'
# gevent.joinall([gevent.spawn(f,url1),
# 				gevent.spawn(f, url2),
# 				gevent.spawn(f, url3),
# 				gevent.spawn(f, url1),
# 				gevent.spawn(f, url2),
# 				gevent.spawn(f, url3),
# 				])


f(url1)
f(url2)
f(url3)
f(url1)
f(url2)
f(url3)
print('duration:',time.time()-start_time)


"""
用gevent的效果：

duration: 2.250128746032715

顺序执行的效果：

duration: 2.0931198596954346
顺序执行怎么还快一点？



"""