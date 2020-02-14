class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
class Stack:
    def __init__(self):
        self.Head = None

    def IsEmpty(self):
        return self.Head is None
    def MakeStackEmpty(self):
        self.Head=None
        return
    def lengthofstack(self, pile):
        temp=pile.Head
        if temp==None:
            return 0
        i=0
        while temp.Next is not None:
            temp=temp.Next
            i+=1
        return i
    def Push(self, Data):
        NewNode = Node(Data)
        if self.Head is None:
            self.Head=NewNode
            return
        temp=self.Head
        while temp.Next is not None:
            temp=temp.Next
        temp.Next=NewNode
    def top(self):
        if self.IsEmpty():
            return None
        temp=self.Head
        while temp.Next is not None:
            temp=temp.Next
        return temp.Data

    def DisplayStack(self):
        current = self.Head
        while current:
            print(current.Data.Display())
            current = current.Next

    def Size(self):
        count = 0
        current = self.Head
        while current:
            current = current.Next
            count += 1
        return count
    def get_last(self):
        if self.IsEmpty():
            return None
        current = self.Head
        while current.Next: 
            current = current.Next
        return current.Data
    def cut_off_at(self, node):
        """Cuts off the linked list at the given node, effectively removing all nodes after it."""
        if not node:
            return
        current = self.Head
        if self.Head.Data==node.Data:
            self.Head=None
        while current and current.Next != node:
            current = current.Next
        if current and current.Next == node:
            current.Next = None

    def RemoveFrom(self, card):
        current = self.Head
        removed_stack = Stack()
        while current and current.Data != card:
            current = current.Next
        if current:
            removed_stack.Head = current
            self.cut_off_at(current) 
        return removed_stack


    def PushStack(self, other_stack):
        if not other_stack.Head:
            return
        if not self.Head:
            self.Head = other_stack.Head
        else:
            current = self.Head
            while current.Next:
                current = current.Next
            current.Next = other_stack.Head
