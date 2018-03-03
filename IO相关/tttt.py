嗯……我改下这个selector的参数把，让register直接注册一个回调函数。然后在select里面直接调那个回调。
大概就这样：
class Selector:
	def __init__(self):
		self.a_dic={}

	def register(self, fd, events, callback):
		self.a_dic.extend({fd:callback})


	def select(self):
		#当时间到
		events=[]
		for fd in a_dic:
			if (key对象处于高电平，满足触发条件):
				key.=new KeyObject()
				key.data=a_dic.get(fd)
				key.fileobj=fd
				mask=1
				events.append(key,mask)
		return events




grace
23: 0
8: 17