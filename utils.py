# 1) petrova features:
#перевірка чи є число простим

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
      print("Введене число НЕ є простим")
