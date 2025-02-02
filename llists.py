class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head 
        if self.length == 0:
            return None
        while temp is not None:
            print(temp.value)
            temp = temp.next
    

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node 
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.head
        pre = self.head
        while(popped_node.next):
            pre = popped_node
            popped_node = popped_node.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0: 
            self.head = None
            self.tail = None
        return popped_node


    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head 
            self.head = new_node
            self.length += 1


    def pop_first(self):
        if self.length == 0:
            return None
        pooped_node = self.head
        self.head = self.head.next
        pooped_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return pooped_node

            
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,value,index):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False


    def insert(self,value,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    

    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 1:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

    def reverse(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        



        
