# Reverse star pattern
n = int(input("Enter the number of rows to generate the reverse star pattern:"))
for i in range(1, n+1):
   for j in range(n+1,i,-1):
        print("*", end="")
   print()
    
# Functions
# Prime check
def is_prime(n):
    if n <= 1:
        print("Not a prime.")
    else:
        for i in range(2,(n//2)+1):
            if n % i == 0:
                print("Not prime")
                return
        print("Prime")        
n = int(input("Enter a number: "))
is_prime(n)
# Armstrong number

def armstrong(n):
    temp = n
    digit_count = 0

    while temp > 0:
        digit_count += 1
        temp = temp // 10
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digit_count
        temp = temp // 10   
    if total == n:
        print("Armstrong")
    else:
        print("Not an Armstrong")
num = int(input("Enter a number: "))
armstrong(num)   		
#perfect number
n=int(input("Enter a number to check perfect or not:"))
total=0
for i in range(1,(n//2)+1):
	if n%i==0:
		total+=i
if total==n:
	print("Perfect number ")
else:
	print("Not a perfect number")	
#Strong number
n=int(input("Enter a number:"))
total=0
temp=n
while temp>0:
	digit=temp%10
	fact=1
	for i in range(1,digit+1):
		fact*=i
	total+=fact
	temp=temp//10
if total==n:
	print("Strong number.")
else:
	print("Not a strong number.")	
	
#automorphic number
n=int(input("Enter a number:"))
sq=n**2
digit_num=0
temp=n
while temp>0:
		digit=temp%10
		digit_num+=1
		temp=temp//10
if sq%(10**digit_num)==n:
		print("Automorphic number.")
else:
		print("Not a automorphic number.")			
#pattern
n=int(input("Enter a  number:"))
for i in range(1,n+1):
	for j in range(n-i,0,-1):
		print(" ",end="")
	for g in range(1,i+1):
			print("*",end="")
	print()																										