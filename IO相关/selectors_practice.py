#!/usr/bin/python
#coding=utf-8
import selectors,socket


def accept(sock,mask):

	conn,addr=sock.accept()
	print('accept')
	#conn.setblocking(False)按默认的为True好像也不影响，毕竟是select()已经监听到变化，不会阻塞了
	sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
	data=conn.recv(1024)
	if not data:
		conn.close()
		sel.unregister(conn)
		print('conn closed')
	else:
		print('reply')
		conn.send(data)










if __name__=='__main__':
	#首先定义一个socket对象
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind(('127.0.0.1',8080))
	s.listen(5)
	#s.setblocking(False)
	#接着创造一个DefaultSelector对象，用于监听
	sel = selectors.DefaultSelector()
	#把socket对象加入监听列表里，加入同时需要与一个函数绑定，
	sel.register(s,selectors.EVENT_READ,accept)
	"""
	#这里的accept就是一个回调函数。注册这一步就是在sel这个调用者这里提前写好，把s和accpet的对应关系写入事件队列。这样程序运行到后面，当s进数据这样一个事件发生，就会触发sel去调用accept这个函数（而不是别的什么函数）
	#如果没有提前注册，事件发生时sel根本不知道调用哪个函数，或者说不知道要调用的函数在哪里。
	#这里称作"回调"其实已经超越了狭义上“回调函数作为另一个函数的参数，在那个函数中被执行"，这是从广义上来讲的，"先注册-再调用"，所以叫回调。“回调函数作为另一个函数的参数，在那个函数中被执行"，应该只是在代码实现上的一种表现，但也可能是另外的表现，比如本例。
	为什么需要"先注册-再调用"？
	回调函数与触发事件的对应关系提前在调用者那里声明好（注册过程），之后在调用者发生事件时再去执行回调函数（发生的事件时无法提前预先知道的，因此执行哪个回调函数也是程序员无法用代码写死的。因此只能对所有的事件都写一个处理逻辑：如果发生事件1，就调用函数1；如果发生事件2，就调用函数2……如果没有时间发生，就不调用任何函数。
	
	
	
	"""

	while True:
		print('while True')
		#selcet()方法拿到有动静的对象，以key,mask的格式封装在events里面
		events=sel.select()
		for key,mask in events:
			#key.fileobj和key.data就是刚刚注册的两个东西：fd和一个函数
			print('key.data:',key.data)#<function accept at 0x0069D6A8>
			print('key.fileobj:',key.fileobj)#<socket.socket fd=208, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 80)>
			fn=key.data#<function accept at 0x0069D6A8>
			fn(key.fileobj,mask)#accept(s,1)




