'''
n = int(input("Enter a positive number: "))
fact = 1
#mytuple = (12, 34, 56, 88)
while n > 0:
    fact *= n
    n -= 1
    
print(fact)
'''

'''
n=int(input("Enter a number: "))
fib = [1, 1]
while len(fib) < n:
    index = len(fib)
    fib.append(fib[index - 1] + fib[index - 2])
    print(fib)
'''
'''
words = "A common programming task is to access all of the elements in a container. Ex: Printing every item in a list. A for loop statement loops over each element in a container one at a time, assigning a variable with the next element that can then be used in the loop body. The container in the for loop statement is typically a list, tuple, or string. Each iteration of the loop assigns the name given in the for loop statement with the next element in the container."
count = 0

for letter in words:
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        count = count + 1
print(count)
'''   

myl = [12, 15, 72, 18, 92]
for number in myl:
    print(number)