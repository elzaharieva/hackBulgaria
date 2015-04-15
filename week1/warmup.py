def fibonacci(n):

    x=1
    y=1
    l=[]

    if n==1:
        l.append(x)
    elif n==2:
        l.append(x)
        l.append(y)
    else:
        l=[1, 1]
        for number in range (n-2):
            a=y
            y=x+y
            x=a
            l.append(y)
    return l

#print (fibonacci(5))

def factorial(n):
    result = 1

    for i in range (1, n+1):
        result = result * i
    return result

#print (factorial(5))

def fact_digits(number):
    result=0
    while number!=0:
        result+=factorial(number%10)
        number=number//10
    return result

#print (fact_digits(999))

def sum_of_digits(n):
    result = 0
    n=abs(n)
    while n!=0:
        result+=n%10
        n=n//10
    return result

#print (sum_of_digits(1325132435356))

def palindrome(obj):
    obj=str(obj)
    while len(obj)>=1:
        if obj[:1]==obj[len(obj)-1:]:
            obj=obj[1:len(obj)-1]
        else:
            return False
    return True

#print (palindrome("kapak"))

def to_digits(n):
    l=[]
    while n!=0:
        l.append(n%10)
        n=n//10
    return l[::-1]

#print (to_digits(123))

def to_number(digits):
    result=0
    while digits!=[]:
        result=result*10+digits[0]
        digits=digits[1:]
    return result

#print (to_number([1,2,3,4]))

def count(n):
    count=1
    while n!=0:
        n=n//10
        count=count*10
    return count

def fib_number(n):
    l= fibonacci(n)
    result=0
    while l!=[]:
        result=result*count(l[0])+l[0]
        l=l[1:]
    return result

#print (fib_number(10))

def count_vowels(str):
    count=0
    while str!="":
        x=str[:1]
        if x=='y' or x=='o' or x=='a' or x=='i' or x=='u' or x=='e' or x=='A' or x=='Y' or x=='O' or x=='U' or x=='I' or x=='E':
            count+=1
        str=str[1:]
    return count
#print (count_vowels("A nice day to code!"))

def count_all(str):
    count=0
    while str!="":
        x=str[:1]
        if (x>='A' and x<='Z') or (x>='a' and x<='z'):
            count+=1
        str=str[1:]
    return count

def count_consonants(str):
    return count_all(str)-count_vowels(str)
#print (count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

def string_to_list(str):
	l=[]
	while str!="":
		l.append(str[0])
		str=str[1:]
	return l

def char_histogram(string):
	lst=string_to_list(string)
	res={}
	for l in lst:
		key=l
		if key not in res:
			res[key]=1
		else:
			res[key]+=1
	return res
#print (char_histogram("AAAAaaa!!!"))

def p_score(n):
	if palindrome(n):
		return 1
	else:
		l=to_number(to_digits(n)[::-1])
		return 1 + p_score(n+l)

#print (p_score(198))

def is_increasing(seq):
	if len(seq)==1:
		return True
	elif seq[0]<=seq[1]:
		seq=seq[1:]
		return is_increasing(seq)
	else:
		return False

#print (is_increasing([1, 2, 3, 4, 2]))

def is_decreasing(seq):
	return (is_increasing(seq[::-1]))

#print (is_decreasing([1,1,1,1]))

def odd_ones(n):
	count=0
	while n!=0:
		if n%10==1:
			count+=1
		n=n//10
	if count%2==1:
		return True
	else:
		return False

def hack(n):
	binary_n=int((bin(n))[2:])
	if (palindrome(binary_n)) and (odd_ones(binary_n)):
		return True
	else:
		return False

def next_hack(n):
	if (hack(n+1)):
		return n+1
	else:
		return next_hack(n+1)

#print(next_hack(8031))	