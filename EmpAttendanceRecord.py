#EmpNode class stores all nodes and relationship between them including data
class EmpNode:
    def __init__(self, EId):
        self.EmpId = EId
        self.attCtr =  1
        self.left = None
        self.right = None

#This class stores EMPId into queue and used for upheap and inorder traversal of tree.
class AttnRecord:
    num = 1000
    employee = []
    head = None
    tail = None

    def find_employee(self, EmpId):
        temp = self.tail
        print("Current self.tail.EmpID is " + str(temp.EmpId))
        while temp is not None and temp.EmpId != EmpId:
            temp = temp.right
        return temp

    def recordSwipeRec(self, Eid):
        print("record_swipe")
        if self.head is None:
            self.head = EmpNode(Eid)
            self.tail = self.head
            print(" Current Value for self.head = ", self.head)
            print(" Current Value for self.tail = ", self.tail)
            print(" Current Value for self.head.EmpId = ", self.head.EmpId)
            print(" Current Value for self.tail.EmpId = ", self.tail.EmpId)
            print("Current Value for self.head.right as " + str(self.head.right))
            print("Current Value for self.head.left as " + str(self.head.left))
            print("Current Value for self.tail.right as " + str(self.tail.right))
            print("Current Value for self.tail.left as " + str(self.tail.left))
            self.enqueue_Employee(self.head.EmpId)
        else:
            print(" Current Value for self.head = ", self.head)
            print(" Current Value for self.tail = ", self.tail)
            print(" Current Value for  self.head.EmpId = ", self.head.EmpId)
            print(" Current Value for  self.tail.EmpId = ", self.tail.EmpId)
            print("Current Value for self.head.right as " + str(self.head.right))
            print("Current Value for self.head.left as " + str(self.head.left))
            print("Current Value for self.tail.right as " + str(self.tail.right))
            print("Current Value for self.tail.left as " + str(self.tail.left))
            temp = self.find_employee(Eid)
            if temp:
                temp.attCtr = temp.attCtr + 1
                print("\nNext Employee for registration is: " + str(Eid) + " already exists with swipe count as " + str(temp.attCtr))
            else:
                #print("\nNext Employee for registration is: " + str(Eid))
                #print("OLD Value for self.tail.right as " + str(self.tail.right))
                self.head.right = EmpNode(Eid)##, attCtr, self.num + 1)
                #print("New Value for self.tail.right as " + str(self.tail.right))
                #print("Created a new object. New Value for self.head.right as " + str(self.head.right))
                #print("New Emp ID of self.head.right.EmpId :- " + str(self.head.right.EmpId))
                self.head.right.left = self.head
                #print("New Value for self.head.right.left as " + str(self.head.right.left))
                self.head = self.head.right
                #print("New Value for self.head as " + str(self.head))
                #print("New Value for self.head.EmpId as ", self.head.EmpId)# self.tail.EmpId)
                #print("New Value for self.head.right as " + str(self.head.right))
                #print("New Value for self.head.left as " + str(self.head.left))
                #print("New Value for self.tail as " + str(self.tail))
                #print("New Value for self.tail.EmpId as ", self.tail.EmpId)
                #print("New Value for self.tail.right as " + str(self.tail.right))
                #print("New Value for self.tail.left as " + str(self.tail.left))
                self.enqueue_Employee(self.head.EmpId)

    def enqueue_Employee(self, EmpId):
        self.employee.append(EmpId)
        print("value of array before heap is " + str(self.employee))
        self.upheap(self.employee)
        print("value of array after heap is " + str(self.employee))

    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

            # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

            # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, n, largest)

    def upheap(self, a):
        heap_size = len(a)
        i = heap_size-1
        if i % 2 == 0:
            parent = (i-2)//2
        else:
            parent = (i-1)//2
        while i > 0:
           print("value of a[parent] is " + str(a[parent]))
           if int(a[i]) > int(a[parent]):
                a[parent], a[i] = a[i], a[parent]
                i = parent
                if parent > 0:
                    if (parent % 2 == 0):
                        parent = (parent-2)//2
                        print("Value of new parent variable inside if is ", parent)
                        print("New parent value in if is " , a[parent])
                    else:
                        parent = (parent-1)//2
                        print("Value of new parent variable inside else is ", parent)
                        print("New parent value in else is " , a[parent])
           else:
                return

    def heap_sort(self, arr):
        n = len(arr)
        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        #for i in range(n // 2 - 1, -1, -1):
         #heapify(arr, n, i)
        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

        print("Employee list after heap sort  " + str(arr))

        for i in range(n - 1, -1, -1):
            temp = self.find_employee(arr[i])
            if temp:
                print("EmpID:-  ", arr[i])
                print("Total Swap:- " + str(temp.attCtr))

    def getSwipeRec(self,eNode):
        if eNode is not None :
            print("Value of EmpID is ", eNode.EmpId)
            return 1 + self.getSwipeRec(eNode.right)
        return 1

    def onPremisesRec(self, eNode):
        if eNode is not None:
            print("EmpID is ", eNode.EmpId)
            print("attCtr is ", eNode.attCtr)
            if eNode.attCtr % 2 == 0:
                print("EmpID " + str(eNode.EmpId)+ " is outside")
                return self.onPremisesRec(eNode.right)
            else:
                print("EmpID " + str(eNode.EmpId) + " is inside")
                return 1 + self.onPremisesRec(eNode.right)
        return 1

    def checkEmpRec(self, eNode, EId):
        if eNode is not None :
            if eNode.EmpId != EId:
                #print("Right Node address is ", eNode)
                print("EmpID is ", eNode.EmpId)
                return self.checkEmpRec(eNode.right,EId)
            else:
                return eNode.attCtr
        return 0



    def frequentVisitorRec(self,eNode,visit):
        if eNode is not None :
            if eNode.attCtr > visit:
                print("Emp ID ", eNode.EmpId," swiped ", eNode.attCtr)
                return [(eNode.EmpId, eNode.attCtr)] + self.frequentVisitorRec(eNode.right, visit)
            else:
                return self.frequentVisitorRec(eNode.right, visit)
        return []

