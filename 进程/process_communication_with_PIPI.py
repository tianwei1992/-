"""
Pipe是multiprocessing下的一个模块，API和tcp_socket很像，有conn.send()和conn.recv(),conn.close()方法

和Queue的区别是：Queue是大家公用了一个队列在保存数据，put放到队列里，get从队列里取。而Pipe没有这个中间的保存数据的地方。直接把两端连起来。conn.send()就是直接把内容发到对方，如果需要保存，也是对方自己写代码保存
"""
from multiprocessing import Process,Pipe

def f(conn):
	conn.send(['a','b','c'])#可以send一个列表
	res=conn.recv()
	print('res:',res)
	conn.close()#注释掉也不报错呢

if __name__=='__main__':
	conn1,conn2=Pipe()#实例化一个Pipe对象，有两部分组成，对应管道的两端，conn 1发conn2就可以收，conn2发conn1可以收
	# 本来都在主进程里。通过把conn2作为参数传进新开的进程里，就实现跨进程通信
	p=Process(target=f,args=(conn2,))
	p.start()
	#conn1在主进程里，先收一个，再发一个
	print('conn1 recv:',conn1.recv())
	conn1.send('hi')
	p.join()