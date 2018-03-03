import time
import threading

def mul():
	res=1
	for i in range(1,100000):
		res*=i
	print(res)

def add():
	res=0
	for i in range(100000000):
		res+=i
	print(res)


t1=threading.Thread(target=mul)
t2=threading.Thread(target=add)
start_time=time.time()
#1并发的方式
t1.start()
t2.start()
t1.join()
t2.join()

#2 顺序执行的方式


# t1.start()
# t1.join()
# t2.start()
# t2.join()

#3 不开线程，直接执行

# mul()
# add()
end_time=time.time()

duration=end_time-start_time
print('duration:',duration)#并发92.83730983734131#顺序94.48540425300598       #并发 9.245617628097534  #顺序 9.61101770401001 #不开线程10.319019556045532
#并发98.65457344055176 #顺序98.49857306480408 #不开线程101.71301054954529
