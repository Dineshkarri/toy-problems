
class Lru_cache:
   
    def __init__(self):
        self.list1 = []

    def put(self,x):
        self.list1.append(x)
        

    def get(self):
        self.list1.pop()
    
    def get_cache(self):
        return self.list1 
        

class Lru_test:
    # cache = Lru_cache()
    

    # def testput(self):
    #     self.cache.put(2)
    #     val = self.cache.get_cache()
    #     assert val == [2]

    # def testget(self):
    #     val2 = self.cache.get()
    #     assert val2 == [2]
        
    # def testget_cache(self):
    #     var = self.cache.get_cache()
    #     assert var == [2]

	def __init__(self):
		self.cacheobj = Lru_cache()
		self.count = 0

	def testput(self):
		self.cacheobj.put(1)
		try:
			assert self.cacheobj.list1 == [1]
			self.count += 1
		except Exception as e:
			print("put function doesn't work.")

	def testget(self):
		self.cacheobj.get()
		try:
			assert self.cacheobj.list1 == []
			self.count += 1
		except Exception as e:
			print("get function doesn't work.")


	def testget_cache(self):
		c = self.cacheobj.get_cache()
		try:
			self.count += 1
			assert c == self.cacheobj.list1
		except Exception as e:
			print("get_cache function doesn't work.")
		

def main():
		testobj = Lru_test()
		testobj.testput()	
		testobj.testget()	
		testobj.testget_cache()	
		if testobj.count == 3:
			print("All tests passed.")

if __name__ == '__main__':
		main()

# if __name__==   "__main__":
#   Lru_test()