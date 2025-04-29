class Queue:
    def __init__(self):
        self.listq=[]
    def isEmpty(self):
        return len(self.listq)==0
    def enQueue(self,data):
        self.listq.append(data)
        self.printQ()
    def deQueue(self):
        removed = None
        if not self.isEmpty():
            removed=self.listq.pop(0)
        self.printQ()
        return removed
    def peek(self):
        return self.listq[0]
    def printQ(self):
        for i in self.listq:
            print(i)
    def clear(self):
        self.listq.clear()

def main():
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.deQueue()
    print("Peek:", q.peek())

main()