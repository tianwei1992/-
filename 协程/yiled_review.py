#!/usr/bin/python
#coding=utf-8

"""
复习yield的用法，为写消费者生产者模型铺垫……

定义了一个生成器叫做gen。
调用gen.__next__()方法，运行到yiled 暂停，返回6
调用gen.send(1)方法，从上次yiled处继续运行，这个1给s，
运行直到下一个yield 5返回，5就是gen.send(1)的结果，所以res2=gen.send(1)，打印res2为5

"""
def f():
	print('ok')
	s=yield 6#s==6?不是，这里是返回6，s接收send的值
	print('s:',s)#s: 1
	yield 5

gen=f()

res=gen.__next__()
print('res:',res)#res: 6
res2=gen.send(1)
print('res2:',res2)#res2: 5