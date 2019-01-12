# 以简单的斐波那契数列为例
def fab(max):
	n,a,b = 0,0,1
	while n < max:
		a,b = b, a + b
		print(a,b)
		n = n + 1
		
# 使用上面的函数结果没有问题，但是直接在fab函数中用print打印数字会导致该函数可复用性差，因为fab函数返回None,其他函数无法获得该函数生成的数列
# 第二个版本
def fab_two(max):
	n,a,b = 0,0,1
	L = []
	while n < max:
		L.append(b)
		a,b = b,a+b
		n = n + 1
	return L

# 改写后的fab函数通过返回List能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数max的增大而增大，如果要控制内存占用，最好不要用List
# 来保存中间结果，而是通过iterable对象来迭代。
# 如:
#	for i in range(1000):
#		pass

# 第三个版本
# Fab类通过next()不断返回数列的下一个数，内存占用始终为常数
class Fab(object):
	def __init__(self,max):
		self.max = max
		self.n,self.a,self.b = 0,0,1
	
	def __iter__(self):
		return self
	
	# python3需要使用__next__
	def __next__(self):
		if self.n < self.max:
			r = self.b
			self.a,self.b = self.b,self.a + self.b
			self.n = self.n + 1
			return r
		raise StopIteration()

# 上面的代码虽然解决了内存问题，但是，，不够简练
# 所以就有了下面的东西
def fab_iter(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		# 上面的一句相当于print(b)
		a,b = b,a + b
		n = n + 1
		
		
if __name__ == '__main__':
	# fab(1)
	
	# for n in fab_two(5):
	#	print(n)
	
	# for n in Fab(5):
	#	print(n)
	
	for n in fab_iter(5):
		print(n)