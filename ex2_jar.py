class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return ("🍪"*self.size)

    def deposit(self, n):
        self.size=self.size+n


    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity > 0:
            self._capacity=capacity
        else:
            raise ValueError("Capacity was not a positive intenger")

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if 0<=size<=self.capacity:
            self._size=size
        else:
            raise ValueError("Jar overlodad")

#teste coco.....não tenho emogis
def main():
    jar=Jar()
    print(Jar)
    jar.deposit(7)
    print(jar)
    jar.withdraw(5)
    print(jar)
if __name__=="__main__":
    main()
