"""list不适用多线程"""
# import threading,time
#
# lst=[1,2,3,4,5]
# def f():
# 	while lst:
# 		a=lst[-1]
# 		print(a)
# 		time.sleep(2)
# 		lst.remove(a)
#
# t1=threading.Thread(target=f)
# t2=threading.Thread(target=f)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

"""
所以需要用到queue
"""
import threading,time,queue
q=queue.Queue(2)
q.put('a')
q.put('b')#默认block为True，表示如果队列已经满了就卡住，等待直到有人get
#q.put('c',block=False)#把block设为False。如果队列满了会报异常    raise Full
queue.Full
print('已经放了a,b,队列长度为:',q.qsize())
time.sleep(2)
foo1=q.get()
print(foo1)#queue是先进先出
foo2=q.get_nowait()
print(foo2)
print(q.empty())
#foo3=q.get(block=False)#同理，默认为True表示没有数据就阻塞直到有人put，设为False表示不阻塞遇到为空发生raise Empty
# q.get(block=False)等价于get_nowait()
#
