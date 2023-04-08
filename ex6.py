print("Задание №3 - Проверка на счастливый билет: ")

def convertToArray (a) :
    array = []
    
    str = f"{a}"
    
    for i in str :
        array.append(int(i))
    
    return array 

def check (num) :
    
    array = convertToArray(num)

    sum1 = 0
    sum2 = 0

    for i in range(len(array) // 2) :

        sum1 += array[i]
        sum2 += array[len(array) - 1 - i]

    return sum1 == sum2


num = int(input("Введите число: "))
print(check(num))   

    
