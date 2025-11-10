#BFS

from collections import deque
locations = ['A', 'B', 'C', 'D']
location_index = {name: idx for idx, name in enumerate(locations)}
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def dfs_matrix(start):
    visited = [False] * len(locations)
    result = []

    def dfs(node):
        visited[node] = True
        result.append(locations[node])
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    dfs(location_index[start])
    return result


def bfs_list(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

def menu():
    print("----Menu----")
    print("1. DFS (using adjacency matrix)")
    print("2. BFS (using adjacency list)")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        start_location = 'A'
        dfs_result = dfs_matrix(start_location)
        print("DFS Traversal (using adjacency matrix):", dfs_result)
    elif choice == '2':
        start_location = 'A'
        bfs_result = bfs_list(start_location)
        print("BFS Traversal (using adjacency list):", bfs_result)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")







#Bubble sort , Selection sort


Salary=[]
size=int(input("Enter the array size:"));
for i in range(0,size):
 ele=float(input("Enter the element:"));
 Salary.append(ele)
 
def bubble_sort(Salary):
 for i in range(len(Salary)-1):
  for j in range(len(Salary)-i-1):
    if(Salary[j]>Salary[j+1]):
     temp=Salary[j];
     Salary[j]=Salary[j+1];
     Salary[j+1]=temp;
 return Salary;

def selection_sort(Salary):
 for i in range(0,size-1):
  for j in range(i+1,size):
    if(Salary[i]>Salary[j]):
     temp=Salary[i];
     Salary[i]=Salary[j];
     Salary[j]=temp;
 return Salary;

def menu():
    print("1.bubble sort:")
    print("2.selection sort:")
    print("3.Exit:")
while True:
    menu()
    choice=input("Enter your choice(1-3):")
    if choice=='1':
      sorted_bubblesort=bubble_sort(Salary)
      print("sorted_bubble sort is",sorted_bubblesort)
      len_b=len(sorted_bubblesort)
      print("The length of bubble sort is:",len_b)
      print("Sorted Salaries:",sorted_bubblesort)
      print("Top 5 salaries are:",sorted_bubblesort[-1:-6:-1])
    elif choice=='2':
      Sorted_SelectionSort=selection_sort(Salary)
      print("Sorted Selection sort is",Sorted_SelectionSort)
      len_b=len(Sorted_SelectionSort)
      print("The length of selection sort is:",len_b)
      print("Top 5 salaries are:",Sorted_SelectionSort[-1:-6:-1])
    elif choice=='3':
      print("Exit")
      break;
    else:
     print("Invalid Choice") 













#Linked list


class StudentNode:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
       self.head = None

    def add_student(self, roll_no, name, marks):
        new_node = StudentNode(roll_no, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(" Student record added.")

    def delete_student(self, roll_no):
        current = self.head
        prev = None
        while current:
            if current.roll_no == roll_no:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print("Student record deleted.")
                return
            prev = current
            current = current.next
        print("Student not found.")

    def update_student(self, roll_no, new_name, new_marks):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.name = new_name
                current.marks = new_marks
                print(" Student record updated.")
                return
            current = current.next
        print(" Student not found.")

    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print(f"Found: Roll No: {current.roll_no}, Name: {current.name}, Marks: {current.marks}")
                return
            current = current.next
        print(" Student not found.")

    def display_students(self, sort_by="roll_no", ascending=True):
        students = []
        current = self.head
        while current:
            students.append((current.roll_no, current.name, current.marks))
            current = current.next

        if sort_by == "roll_no":
            students.sort(key=lambda x: x[0], reverse=not ascending)
        elif sort_by == "marks":
            students.sort(key=lambda x: x[2], reverse=not ascending)

        if not students:
            print(" No records to display.")
            return

        print("\n Student Records:")
        for s in students:
            print(f"Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

def menu():
    system = StudentLinkedList()
    while True:
        print("\n--- Student Record Management Menu ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))
            system.add_student(roll, name, marks)
        elif choice == '2':
            roll = int(input("Enter Roll No to Delete: "))
            system.delete_student(roll)
        elif choice == '3':
            roll = int(input("Enter Roll No to Update: "))
            name = input("Enter New Name: ")
            marks = int(input("Enter New Marks: "))
            system.update_student(roll, name, marks)
        elif choice == '4':
            roll = int(input("Enter Roll No to Search: "))
            system.search_student(roll)
        elif choice == '5':
            sort_key = input("Sort by 'roll_no' or 'marks': ").strip()
            order = input("Order 'asc' or 'desc': ").strip()
            ascending = True if order == 'asc' else False
            system.display_students(sort_by=sort_key, ascending=ascending)
        elif choice == '6':
            print(" Exiting Student Record Management System.")
            break
        else:
            print("Invalid choice. Try again.")


menu()















#Hash Table


class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<DELETED>"

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash_function(key)
        original_index = index
        while self.table[index] not in (None, self.DELETED):
            if self.table[index] == key:
                print(f"Key {key} already exists at index {index}.")
                return
            index = (index + 1) % self.size
            if index == original_index:
                print("Hash table is full. Cannot insert.")
                return
        self.table[index] = key
        print(f"Inserted key {key} at index {index}.")
        
    def search(self, key):
        index = self._hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f" Key {key} found at index {index}.")
                return index
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f" Key {key} not found.")
        return None
        
    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.table[index] = self.DELETED
            print(f" Key {key} deleted from index {index}.")

    def display(self):
        print("\nHash Table Status:")
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")
        print("-" * 30)


ht = LinearProbingHashTable(size=10)

while True:
    print("\n===== MENU =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        ht.insert(key)
        
    elif choice == 2:
            key = int(input("Enter key to search: "))
            ht.search(key)
            
    elif choice == 3:
            key = int(input("Enter key to delete: "))
            ht.delete(key)

    elif choice == 4:
        ht.display()
        
    elif choice == 5:
        print("...Exiting program...")
        break
    else:
        print("Invalid choice. Try again!")

















#Binary search , Linear search


emp_id=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
  emp=int(input("Enter employee id:"))
  emp_id.append(emp)

def linear_search(emp_id,target):
 for i in range(0,len(emp_id)):
    if(emp_id[i]==target):
       return i;
       break;
 return-1
 
def binary_search(emp_id,key):
 low=0
 high=n-1
 while low<=high:
    mid=(low+high)//2
    if emp_id[mid]==key:
       return mid;
    if emp_id[mid]<key:
       low=mid+1
    else:
       high=mid-1
 return-1

def menu():
    print("1.linear:")
    print("2.binary:")
    print("3.Exit:")

while True:
   menu()
   choice=input("Enter your choice(1-3):")
   if choice=='1':
    key=int(input("Enter id to be search:"))
    result=linear_search(emp_id,key)
    if result!=-1:
     print("Element found at location",result)
    else:
     print("Employee Id is not found")
   elif choice=='2':
     sorted_id=sorted(emp_id)
     key=int(input("Enter id to be search:"))
     result=binary_search(sorted_id,key)
     if result!=-1:
      print("Element found",result)
     else:
      print("Element not found",result)
   elif choice=='3':
      print("Exit")
      break;
   else:
      print("Invalid Choice") 
      





#Queue


from collections import deque

class Q_deque:
    def __init__(self):
        self.q = deque()

    def add_event(self, event):
        self.q.append(event)
        print(f"Event '{event}' added")

    def process_event(self):
        if self.q:
            event = self.q.popleft()
            print(f"Event '{event}' is processed")
        else:
            print("No events to process")

    def cancel_event(self, event):
        if event in self.q:
            self.q.remove(event)
            print(f"Event '{event}' is removed")
            print("Remaining events:", list(self.q))
        else:
            print(f"Event '{event}' not found in queue")

    def display(self):
        if self.q:
            print("Events in queue:", list(self.q))
        else:
            print("No events in the queue")

    def menu(self):
        while True:
            print("\n=== MENU ===")
            print("1. Add event")
            print("2. Process event")
            print("3. Cancel event")
            print("4. Display events")
            print("5. Exit")
            choice = int(input("Enter a number: "))

            if choice == 1:
                event = input("Enter an event: ")
                self.add_event(event)
            elif choice == 2:
                self.process_event()
            elif choice == 3:
                event = input("Enter event to be deleted: ")
                self.cancel_event(event)
            elif choice == 4:
                self.display()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

obj = Q_deque()
obj.menu()







#Stack

class TextEditor:
 def __init__(self):
    self.document=""
    self.Undo_stack=[]
    self.Redo_stack=[]
    
 def make_change(self,change):
  self.Undo_stack.append(self.document)
  self.document+=change
  self.Redo_stack.clear()
  print("\n change made.")
  self.display_content()
  
  
 def undo_action(self):
  if  self.Undo_stack:
     self.Redo_stack.append(self.document)
     self.document=self.Undo_stack.pop()
     print("\n Undo performed")
  else:
     print("\n no more action to Undo")
   
 def redo_action(self):
  if self.Redo_stack:
     self.Undo_stack.append(self.document)
     self.document=self.Redo_stack.pop()
     print("\n redo performed")
  else:
     print("\n no more action to Redo")
      
 def display_content(self):
  print("the original document is :",self.document)
      
 def menu(self):
  while True:
   print("===menu===")
   print("1.Make a change")
   print("2.Undo")
   print("3.Redo")
   print("4.Display")
   print("5.Exit")
   choice=int(input("Enter your choice:"))
   if choice==1:
    change=input("Text to be added:")
    self.make_change(change)
   elif choice==2:
    self.undo_action()
   elif choice==3:
    self.redo_action()
   elif choice==4:
    self.display_content()
   elif choice==5:
    print(exit)

Editor=TextEditor()
Editor.menu()






#BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.key, end=' ')
            self.in_order(root.right)

    def pre_order(self, root):
        if root:
            print(root.key, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def menu(self):
        while True:
            print("\n--- Binary Search Tree Menu ---")
            print("1. Insert")
            print("2. Search")
            print("3. Delete")
            print("4. In-order traversal")
            print("5. Pre-order traversal")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                key = int(input("Enter key to insert: "))
                self.root = self.insert(self.root, key)
                print(f"Inserted {key}.")

            elif choice == '2':
                key = int(input("Enter key to search: "))
                result = self.search(self.root, key)
                if result:
                    print(f"Key {key} found in the BST.")
                else:
                    print(f"Key {key} not found.")

            elif choice == '3':
                key = int(input("Enter key to delete: "))
                self.root = self.delete(self.root, key)
                print(f"Deleted {key} if it existed.")

            elif choice == '4':
                print("In-order traversal:", end=' ')
                self.in_order(self.root)
                print()

            elif choice == '5':
                print("Pre-order traversal:", end=' ')
                self.pre_order(self.root)
                print()

            elif choice == '6':
                print("Exiting the program.")
                break

       


b = BST()
b.menu()

































