def sum_of_divisors(n):
	result=0
	i=1
	while i<=n:
		if n%i==0:
			result+=i
		i+=1
	return result

#print (sum_of_divisors(8))

def is_prime(n):
	if sum_of_divisors(n)==1+n:
		return True
	else:
		return False
#print (is_prime(-12))

def number_of_divisors(n):
	count=0
	i=1
	while i<=n:
		if n%i==0:
			count+=1
		i+=1
	return count

def prime_number_of_divisons(n):
	if is_prime(number_of_divisors(n)):
		return True
	else:
		return False
#print (prime_number_of_divisons(7))

def to_digits(n):
    l=[]
    while n!=0:
        l.append(n%10)
        n=n//10
    return l[::-1]

def contains_digit(number, digit):
	return digit in to_digits(number)

#print (contains_digit(133653, 5))

def contains_digits(number, digits):
	for digit in digits:
		if contains_digit(number, digit)==False:
			return False
	return True

#print (contains_digits(402123, [0, 3, 5, 4]))

#resut = [x**2 for x in range(11)]

def sum_matrix(m):
	res=0
	for i in range(len(m)):
		res+= sum(m[i])
	return res

m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print (sum_matrix(m))

def last(l):
	lst=l[::-1]
	return lst[0]

def is_number_balanced(n):
	l=to_digits(n)
	l1=[]
	l2=[]
	while len(l)>1:
		l1.append(l[0])
		l2.append(last(l))
		l=l[1:-1]
	return sum(l1)==sum(l2)
#print (is_number_balanced(1231))

def string_to_list(str):
	l=[]
	while str!="":
		l.append(str[0])
		str=str[1:]
	return l


def count_substrings(haystack, needle):
	count=0
	while haystack!="": #ot 0 do 5
		if needle==haystack[:len(needle)]:
			count+=1
			haystack=haystack[len(needle):]
		else:
			haystack=haystack[1:]
	return count

#print (count_substrings(("babababa"), ("baba")))

def to_number(digits):
    result=0
    while digits!=[]:
        result=result*10+digits[0]
        digits=digits[1:]
    return result

def zero_insertion(n):
	l=to_digits(n)
	res=[]
	while l!=[]:
		if len(l)==1:
			res.append(l[0])
		elif l[0]==l[1] or (l[0]+l[1])%10==0:
			res.append(l[0])
			res.append(0)
		else:
			res.append(l[0])
		l=l[1:]
	return (to_number(res))
#print (zero_insertion(6446))

def matrix_to_dict(m):
	dict={}
	a=0
	b=0
	for lst in m:
		for l in lst:
			key=(a,b)
			dict[key]=l
			b+=1
		b=0
		a+=1
	return dict
#print (matrix_to_dict([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def bomb(x, y, m):
	d=matrix_to_dict(m)
	if (x-1, y-1) in d:
		d[(x-1,y-1)]-=d[(x,y)]
		if (d[x-1, y-1]<0):
			d[x-1, y-1]=0
	if (x-1, y) in d:
		d[(x-1,y)]-=d[(x,y)]
		if (d[x-1, y]<0):
			d[x-1, y]=0
	if (x-1, y+1) in d:
		d[(x-1,y+1)]-=d[(x,y)]
		if (d[x-1, y+1]<0):
			d[x-1, y+1]=0
	if (x, y-1) in d:
		d[(x,y-1)]-=d[(x,y)]
		if (d[x, y-1]<0):
			d[x, y-1]=0
	if (x, y+1) in d:
		d[(x, y+1)]-=d[(x,y)]
		if (d[x, y+1]<0):
			d[x, y+1]=0
	if (x+1, y-1) in d:
		d[(x+1, y-1)]-=d[(x,y)]
		if (d[x+1, y-1]<0):
			d[x+1, y-1]=0
	if (x+1, y) in d:
		d[(x+1,y)]-=d[(x,y)]
		if (d[x+1, y]<0):
			d[x+1, y]=0
	if (x+1, y+1) in d:
		d[(x+1, y+1)]-=d[(x,y)]
		if (d[x+1, y+1]<0):
			d[x+1, y+1]=0
	sum=0
	for i in d:
		sum+=d[i]
	return sum
#print (bomb( 1, 1, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def matrix_bombing_plan(m):
	dict={}
	for i in range(len(m)):
		for j in range(len(m[0])):
			dict[(i,j)]=bomb(i, j, m)
	return dict
#print (matrix_bombing_plan ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))