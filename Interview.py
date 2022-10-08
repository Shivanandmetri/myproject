# List Sorting
# l=[4,5,3,2,1,9,0,-1]
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j]>l[j+1]:
#             # using > symbol ascending order < decending order
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
# print(l)

########################################################

# Fibinaci Series
# n=int(input("enter the number: "))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
##########################################

# number Palindrome
# num=int(input("enter the nuber:"))
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rem+(rev*10)
#     num//=10
# if temp==rev:
#     print(f"{temp} is palindrome")
# else:
#     print(f"{temp} is not a palondrome")
##############################################

# mynum=9148071519
# mynum1=str(mynum)
# count=0
# for i in mynum1:
#     if i=="1":
#         count+=1
# print(count)
##########################################

# Reverse Word
# str1='who are you'
# str3=""
# str2=str1.split()
# for i in str2:
#     str3=i+" "+str3
# print(str3)

################################################
# swapping 2 nos without using temp
# a=4
# b=5
# a=a+b
# b=a-b
# a=a-b
# print("a value is",a)
# print("b value is",b)

#####################################################
# prime number
# num=int(input("enter the number: "))
# count=0
# if num==1:
#     print("we cannot check 1 is prime or not")
# else:
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print("prime number")
#     else:
#         print("not prime number")

##################################################################
# factorial number
# n=int(input("enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"factorial of {n} is {fact}")





















    







