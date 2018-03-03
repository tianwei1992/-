"""

"""
from multiprocessing import Manager,Process

def f(d,l,n):
	d[n]='a'
	l.append(n)





if __name__=='__main__':
	with Manager() as manager:
		d=manager.dict()
		l=manager.list(['a' for i in range(5)])#['a' for i in range(5)]是默认值
		print()
		lst=[]
		for i in range(5):
			p=Process(target=f,args=(d,l,i))
			p.start()
			lst.append(p)
		for p in lst:
			p.join()
		print('d:',d)#d: {2: 'a', 1: 'a', 0: 'a', 3: 'a', 4: 'a'}
		print('l:',l)#l: ['a', 'a', 'a', 'a', 'a', 2, 1, 0, 3, 4]