def factorial(n):
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a

<<<<<<< HEAD
def is_power_of_five(num):
    degree = 0
    while 5 ** degree <= num:
        if 5 ** degree == num:
            return True
        degree += 1

    return False

number = int(input("Введіть число: "))
result = is_power_of_five(number)

if result:
    print(f"{number} є степенем п'ятірки.")
else:
    print(f"{number} не є степенем п'ятірки.")

# 2) petrova features:
#перевірка чи є число простим


# 1) petrova features:
 cb34b2a (Add a code to utils.py (without pulll request))
#n = int(input())

def PrimeNum(n): #опис функції
    is_prime = True
    for i in range (2, (n//2) + 1):
        if n % i == 0:
            is_prime = False
        break
    if is_prime:
        print("Введене число є простим")
    else:
HEAD
      print("Введене число НЕ є простим")

      print("Введене число НЕ є простим")

# 2) petrova features: #add without pull request
#перевірка чи є число простим
def PrimeNum(n): #опис функції
    is_prime = True
    for i in range (2, (n//2) + 1):
        if n % i == 0:
            is_prime = False
        break
    if is_prime:
        print("Введене число є простим")
    else:
      print("Введене число НЕ є простим")



 cb34b2a (Add a code to utils.py (without pulll request))
