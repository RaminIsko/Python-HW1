print("Задание №8")

def check (a,b,c) :
    return c % a == 0 or c % b == 0

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

print(check(a,b,c))

