class Lru_cache:
   
    def __init__(self):
        self.list1 = []

    def put(self,x):
        pass

    def get(self,y):
        pass
    
    def get_cache(self):
        pass

cache = Lru_cache()


class Lru_test:

    def testput(self):
        val = cache.put(2)
        self.assertEqual(val,2)

    def testget(self):
        val1 = cache.get()
        self.assertEqual(val1,2)

    def testget_cache(self):
        var = cache.get_cache()
        self.assertEqual(var,[2])

if __name__==   "__main__":
  Lru_test()