'''
#import math
print("hello World")
class pythoncode:

    def add(self,num1,num2):
        sum=num1+num2
        return sum


    def division1(self,num1,num2):
        return num1%num2

    def areaoftriangle(self,num1,num2):
        return 0.5*num1*num2

    def swapVar(self,a,b):
        a,b=b,a
        return a,b


pythoncode=pythoncode()
num1=2
num2=3
a=3
b=4
#result1=pythoncode.add(num1,num2)
#print(result1)
#result2=pythoncode.division1(num1,num2)
#print(result2)

#result=pythoncode.areaoftriangle(num1,num2)
#print(result)

#result=pythoncode.swapVar(a,b)
#print(result)

class equ_solve:
    def quadratic(self,a,b,c):
        delta= b*b-4*a*c
        root1 = (-b + (delta)**0.5) / (2 * a)
        root2 = (-b - (delta)**0.5) / (2 * a)

        if delta>=0:
            return root1,root2

        elif delta==0:
            return root1
        else:
            return False

equ_solve= equ_solve()
a=1
b=-3
c=2
result=equ_solve.quadratic(a,b,c)
#print(result)

class negative_positive:
    def no_check(self,k):
        if k>0:
            return "positive"
        else:
            return "negative"

negative_positive=negative_positive()
K=2
result2=negative_positive.no_check(K)
#print(result2)



class prime_check:
    def prime_no(self,num):
        for i in range(2,num):
            if num%i==0:
                return "not prime"
        else:
            return "prime"
prime_check=prime_check()
num=31
result3=prime_check.prime_no(num)
#print(result3)



class prime_in_range:
    def prime_no(self,min,max):
            for num in range(min,max+1):
                if num>1:
                  for i in range(2,num):
                      if num%i==0:
                          break
                  else:
                      return num
prime_in_range=prime_in_range()
min=1

max=10
result4=prime_in_range.prime_no(min,max)
print(result4)


#cube sum

def cube_sum(n):
    sum=0
    if n<=0:
        return sum
    else:
        for i in range(1,n+1):
            sum=sum+(i**3)
        return sum

n=190
result=cube_sum(n)
print(result)


#largest element in arrey

def largest_ele(arr):
    largest_element=arr[0]
    for i in arr:
        if i >largest_element:
            largest_element= i
    return largest_element
arr=(91,3,4489,2,3,31,44313)
result=largest_ele(arr)
print(result)
'''
#arrey rotation












