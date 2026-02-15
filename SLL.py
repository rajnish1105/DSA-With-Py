class Node:
    def __init__(self, data = None):
      self.Data = data
      self.next = None

class SLL:
    def __init__(self):
        self.start = None

    def insert_at_start(self, data):
        t = Node(data)
        t.next = self.start
        self.start = t

    def insert_at_end(self, data):
        new = Node(data)
        if self.start == None:
            self.start = new
            return

        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_at_after(self, data):
        target = int(input("Enter the index after which you want to insert the data : "))
        i = 0
        temp = self.start
        

    def delete_at_start(self):
        if self.start == None:
            print("List is Empty")
        else:
            self.start = self.start.next

    def delete_at_end(self):
        if self.start == None:
            print("List is Empty")
            return

        if self.start.next is None:
            self.start = None
            return

        temp = self.start
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_after(self):
        target = int(input("Enter the index after which you want to delete the data : "))
        if self.start is None:
            print("List is Empty")
            return
            

    def printAll(self):
        temp = self.start
        while temp:
            print(temp.Data, end=" ")
            temp = temp.next
        print()

    def search(self, data):
        t = self.start
        while t:
            if t.Data == data:
                return True
            t = t.next
        return False


obj1 = SLL()
obj1.insert_at_start(10)
obj1.insert_at_start(20)
obj1.insert_at_start(30)
obj1.insert_at_start(40)
obj1.insert_at_start(50)
obj1.insert_at_start(60)
obj1.insert_at_after(90)
obj1.insert_at_end(70)
# obj1.delete_at_end()

obj1.printAll()

# print(obj1.search(13))
