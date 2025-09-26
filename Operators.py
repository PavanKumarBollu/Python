#Operators
""""
operators are used to perform the mathematical operations inside the program like addition subtraction multiplication
greaterThan lessThan ...etc.
Operator and Operands
Eg: a+ b here + is an operator and a , b are operands
"""

#Types of operators

#Arithmetic Operators(Common)
#Comparision Operators(Common)
#Logical Operators(Common)
#Assignment Operators(Common)
#Identity Operators
#Bitwise Operators(Common)
#Membership Operators

#Arithmetic Operators

"""
+ add
- subtract
* multiply
/ division
// floor division
% modulos(will return the reminder)
** exponentiation

"""
#Examples
a=10
b=20
c=a+b
print(c)

s=20
d=10
f=s-d
print(f)

m=2
n=10
o=m*n
print(o)

# when you use the whole, decimal numbers the results will be always the decimal numbers and you can work with both
# decimal and whole number togther
j=120
k=2.3
l=j/k
print(l)

#when you use exponentiation operator that means it will do the power of that number
x= 2
y= 10
z=x**y
print(z)

#when you use the flor division that means it will give the quotient  62.5 -> 62 eg: 12.9 -> 12
r=250
s=4
t=r//s
print(t)


#modulos
q = 123
w = 4
e = q%w
print(e)


#Comparision Operators
"""
== Equals
< lessThan
> greaterThan
<= lessThan or equals 
>= greaterThan or equals 
!= not equals 

"""
#Examples
print(a==b)
print(m!=n)
print(j>k)
print(j<k)
print(l<=r)
print(l>=r)
print(" ")
print(2==2)#True
print(2>1)#True
print(2!=2)#False
print(12<11)#False
print(11>10)#True
print(9<=9)#True
print(123>=123)#True


# Logical Operators
"""
AND
OR
NOT

"""
print(" ")
#Examples
x = 5
y = 3
print(x > 3 and y < 5)#True
print(x > 10 and y < 5)#True


print("Or condition")
x=False
y=False
res= x or y
print(res)

print("logical not")
res1= x and y
print("res 1 result : " , res1)
res2 = not res1
print("res 2 result : " , res2)

# Assignment Operators

"""
=
+=
-=
*=
/=
%=
**=
//=

"""

#Example
print("Assignment Operators")
x = 25

x+=2 # x+=2 -> x = x+2 -> 27
#in this line the new value of x is 27 not 25 because we have updated the x values
print(x)
x-=2 # x-= -> x = x-2 -> 25
print(x)
x*=2 # x*= -> x = x*2 -> 50
print(x)


#Membership operators
"""
in (membership)
not in(negated membership)

"""
print("Membership Operators")
fruits = ["apple", "banana", "orange"]
print("fruits names" ,fruits)
fruit = "banana"
print("Fruit",fruit)
is_banana_in_list = fruit in fruits
print(is_banana_in_list)

fruit1 = "mango"
print("Fruit",fruit1)
is_bananas_in_list = fruit1 not in fruits
print(is_bananas_in_list)







