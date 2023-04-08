print("Задание №2 - сумма цифр трехзначного числа")

def digitsSum (a) :
    
    sum = 0
    
    while(a > 0) :

        sum += a % 10
        
        a //= 10

    return sum

number = int(input("Введите трехзначное число: "))

if(number >= 100 and number <= 999) :
    print(f"Сумма цифр числа {number} -> {digitsSum(number)}")
else :
    print("Введите трехзначное число: ")


