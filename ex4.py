print("Задание №4 - Катя собрала в 2 раза больше журавликов чем Сережа и Петя вместе. Сережа и Петя собрали одинаковое кол-во журавликов. Сколько журавликов собрал каждый ребенок")

def eachChild (sum) :

    x = sum / 3
    
    array = [0.5 * x, 2 * x, 0.5 * x]

    return array 

sum = int(input("Введите кол-во пойманных журавликов: "))

if(sum % 4 == 0) :
    print(f"{sum} -> {eachChild(sum)}")
else :
    print("Введите число, которое делится на 4 ")
