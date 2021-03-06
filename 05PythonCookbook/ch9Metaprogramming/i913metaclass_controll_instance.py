class Spam:
    def __init__(self, name):
        self.name = name

a = Spam('abel')
b = Spam('stone')



class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

class Spam(metaclass=NoInstances):

    @staticmethod
    def grok(x):
        print('Spam.grok')

try:
    s = Spam()
except:
    print('error here')
    # raise


print("单例模式")
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")

a = Spam()
b = Spam()
print(a is b)
c = Spam()
print(a is c)

