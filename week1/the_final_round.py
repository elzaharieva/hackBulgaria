def unique_words_count(arr):
    return len(set(arr))

#print (unique_words_count(["apple", "banana", "apple", "pie"]))


def func(time, string):
    str = ""
    while time != 0:
        str += string
        time -= 1
    return str


def not_a_nan(times):
    str2 = "NaN"
    result = func(times, "Not a ")
    return result + str2
#print (not_a_nan(3))


def sum_of_divisors(n):
    result = 0
    i = 1
    while i <= n:
        if n % i == 0:
            result += i
        i += 1
    return result


def is_prime(n):
    if sum_of_divisors(n) == 1 + n:
        return True
    else:
        return False


def prime_divisors(n):
    list = []
    for i in range(n + 1):
        if is_prime(i) and n % i == 0:
            list.append(i)
    return list[::-1]
#print (prime_divisors(21))


def div(n, list):
    l = []
    for i in range(len(list)):
        count = 0
        while n >= list[i]:
            n = n // list[i]
            count += 1
            l.append((list[i], count))
    return l
#print (div (10, [5,2]))


def prime_factorization(n):
    return div(n, prime_divisors(n))
#print (prime_factorization(89))


def group(lst):
    l = []
    temp = []
    temp.append(lst[0])
    lst = lst[1:]
    while lst != []:
        if lst[0] == temp[-1]:
            temp.append(lst[0])
            lst = lst[1:]
        else:
            l.append(temp)
            temp = []
            temp.append(lst[0])
            lst = lst[1:]
    if lst == []:
        l.append(temp)
    return l
#print (group([1, 1, 1, 2, 3, 3, 1, 1, 1]))


def max_consecutive(items):
    l = group(items)
    d = 0
    for i in range(len(l)):
        if len(l[i]) > d:
            d = len(l[i])
    return d
#print (max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))


def groupby(func, seq):
    res = {}
    for x in seq:
        key = func(x)
        if key not in res:
            res[key] = [x]
        else:
            res[key] += [x]
    return res
#print (groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))


def three(n):
    count = 0
    while n % 3 == 0:
        count += 1
        n = n // 3
    return count

# def prepare_meal(number):


def func(time, string):
    str = ""
    while time != 0:
        str += string
        time -= 1
    return str


def prepare_meal(n):
    res = func((three(n)), "spam ")
    if n % 5 == 0:
        res += "and eggs"
    return res
#print (prepare_meal(7))


def path_to_list(path):
    l = []
    while path != "" and path != "/":
        if path[0] == '/':
            path = path[1:]
        else:
            i = 0
            while path[i] != '/':
                i += 1
            l.append(path[:i])
            path = path[i + 1:]
    return l
#print (path_to_list("/abc/aa//"))


def reduce_file_path(path):
    lst = path_to_list(path)
    str = "/"
    for i in range(len(lst)):
        if lst[i] == '.':
            lst.remove(lst[i])
        elif lst[i] == "..":
            lst.remove(lst[i - 1])
            lst.remove(lst[i-1])
        else:
        	i=i
    for i in lst:
        str += i
        str += '/'
    if str=="":
    	return "/"
    else:
    	return str[:-1]
print (reduce_file_path("/srv/../"))
