"""
（4）Event同步事件对象-threading.Event
Event内置了一个flag，通过event.set()置位，event.clear()复位。event.wait()的行为依赖于这个flag，如果是set状态就do nothing，如果是clear，就会一直阻塞直到发生event.set。

"""
''
import threading,time

class Boss(threading.Thread):
	def run(self):
		print('BOSS:上班')
		#发生事件1，用event.set()让对方感知到
		event.set()
		time.sleep(5)
		print('BOSS:下班')
		# 发生事件2，再次用event.set()让对方感知到
		event.set()

class Worker(threading.Thread):
	def run(self):
		#一开始处于event.wait()状态，阻塞直到事件发生
		event.wait()
		print('Worker:开始工作……')
		time.sleep(2)
		#响应完成以后event.clear()以使对方能够设置下一个事件，event.wait()以使自己能够阻塞等待下一个事件
		event.clear()
		event.wait()
		print('Worker:好的呢')

if __name__=='__main__':
	event=threading.Event()
	l=[]
	for i in range(5):
		w=Worker()
		l.append(w)
	b=Boss()
	l.append(b)
	for t in l:
		t.start()
	for i in l:
		t.join()
