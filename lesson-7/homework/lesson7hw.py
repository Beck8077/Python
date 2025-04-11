# 1. is_prime(n) funksiyasi

def is_prime(n: int):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False 

    return True 

print(is_prime(4))

# 2. digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(502))


# 3. Ikki sonning darajalari

def power_of_two(number):
    power_list = []
    for n in range(1, number):
        if 2 ** n >= number:
            break
        elif 2 ** n < number: 
            power_list.append(2**n)

    return power_list

print(power_of_two(20))