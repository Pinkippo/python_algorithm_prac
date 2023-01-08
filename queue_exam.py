#큐 : First In First Out 규직을 따른다
# front -> dequeue / rear -> append

class queue:  # 큐 구현
    def __init__(self):
        self.items = []
        self.front_index = 0
    def enqueue(self, val):
        self.items.append(val)
    def dequeue(self):
        if self.front_index == len(self.items):
            print("Q is Empty")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x
    def top(self):
        return self.items[-1]


def Josephus(n, k):
    x = queue()
    y = 0
    for i in range(1,n+1):
        queue.enqueue(x,i)
    
    while(queue.top(x)==y):
        z = queue.dequeue(x)

        if z % k != 0:
             y = z
             queue.enqueue(x,z)
    
    return queue.top(x)

print(Josephus(9,3))