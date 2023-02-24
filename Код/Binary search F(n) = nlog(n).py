import random
import datetime

class stack:
    def __init__(self):
        self.spisok = []
    def create(self, n = 0):
        for i in range(n):
            self.spisok.append(random.randrange(1, 101))
    def mid(self):
        middle = len(self.spisok) // 2
        if (len(self.spisok) % 2) != 0:
            middle += 1
        return middle
    def lenght(self):
        len_spisok = 0
        for i in self.spisok:
            len_spisok += 1
        return len_spisok
    def pop(self, count = 0):# 2
        count += 2
        return self.spisok.pop()
    def append(self, i = None, count = 0):# 1
        count += 1
        self.spisok.append(i)
        return count





stack = stack()
stack_help1 = []
stack_help2 = []
stack_help3 = []
stack_help4 = []
stack_help5 = []
count = 0
def sort_vstav():
    for n in range(900, 1200, 300):
        stack.create(n)
        print(stack.spisok)
        for i in range(stack.lenght() // 2):
            stack_help1.append(stack.pop(count))
        for i in range(stack.lenght()):
            stack_help2.append(stack.pop(count))
        stack_help2 = stack_help2[::-1]
        start = datetime.datetime.now()
        ##################################################################################
        for i in range(n-1): # n * (2 +18 + 9n) = 20n+9n^2
            if len(stack_help3) == 0:
                element1 = stack_help1.pop()
                element2 = stack_help2.pop()
                if element1 > element2:
                    stack_help3.append(element1)
                    stack_help3.append(element2)
                else:
                    stack_help3.append(element2)
                    stack_help3.append(element1)
            else:
                if len(stack_help4) == 0:
                    element1 = stack_help1.pop()
                    element2 = stack_help2.pop()
                    if element1 > element2:
                        stack_help4.append(element1)
                        stack_help4.append(element2)
                    else:
                        stack_help4.append(element2)
                        stack_help4.append(element1)
                else:#2 + 2 *( 3 + 1+ n/2*(6)+ 3 + 1+ n/2*(6 +3) = 2 + 2 * (8 + 4,5n) = 18 + 9n
                    while len(stack_help3) > 0: #2 +2 *(
                        element3 = stack_help3.pop() # 3
                        for i in range(len(stack_help4)): # 1+ n/2 * (6
                            element_sort = stack_help4.pop() # 3
                            if(element3 < element_sort):#1
                                stack_help4.append(element_sort) #1
                                stack_help4.append(element3) #1
                                break
                            elif element3 == element_sort: #1
                                stack_help4.append(element_sort)#1
                                stack_help4.append(element3)#1
                                break
                            else:
                                stack_help5.append(element_sort)
                        if len(stack_help4) == 0:#2
                            stack_help4.append(element3)#1
                        while len(stack_help5) > 0:#2 + n*(
                            stack_help4.append(stack_help5.pop())#3
        #########################################################################################################
        for i in range(len(stack_help4)):
            stack.append(stack_help4.pop())
        end = datetime.datetime.now()
        print(start - end)
        print(stack.spisok)

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr

stack.create(1000)
print(insertion_sort(stack.spisok))


