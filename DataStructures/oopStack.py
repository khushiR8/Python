class Stack:
    def __init__(self):
        self.listStack = []

    def isEmpty(self):
        return len(self.listStack) == 0

    def push(self, data):
        self.listStack.append(data)
        self.printStack()

    def pop(self):
        if not self.isEmpty():
            self.listStack.pop()
        else:
            print("Stack is empty!")
        self.printStack()

    def printStack(self):
        print("Top\n")
        for i in reversed(self.listStack):
            print(i)
        print("\nEnd")

    def peek(self):
        if not self.isEmpty():
            return self.listStack[-1]
        else:
            return None

    def clear(self):
        self.listStack.clear()
        self.printStack()
def main():
    s=Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.pop()
    print(s.peek()) 
main()    