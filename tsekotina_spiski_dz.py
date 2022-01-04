print("Функции со списками")
s=input("Введите список: ")
slovo_list=list(s)
print(slovo_list)
while True:
    print("-----------------------------------------------------------------------")
    print("1-Определить длину строки ")
    print("2-Добавляет введеный пользователем элемент в конец списка ")
    print("3-Повторить строку ")
    print("4-Cоединить два списка ")
    print("5-Перевернуть список ")
    print("6-Очистить список ")
    print("7-Сортировка чисел ")
    print("8-Сортировка списка строк (по алфавиту) ")
    print("9-Удалить элемент в указанном индексе ")
    print("10-Добавить букву на выбиранную позицию ")
    print("11-Выход ")
    print("-----------------------------------------------------------------------")
    try:
        a=int(input("Какую функцию вы желаете использовать?: "))
        if a==1:
            d=len(slovo_list)
            print(f"Длина строки: {d}")
        elif a==2:
            b=input("Что вы желаете добавить?: ")
            slovo_list.append(b)
            print(slovo_list)
        elif a==3:
            b=int(input("Сколько раз вы желаете повторить строку?: "))
            slovo_list*=b
            print(slovo_list)
        elif a==4:
            b=input("Введите то, что желаете добавить к списку: ")
            slovo_list.extend(b)
            print(slovo_list)
        elif a==5:
            slovo_list.reverse()
            print(slovo_list)
        elif a==6:
            slovo_list.clear()
            print(slovo_list)
        elif a==7:
            slovo_list.sort(reverse = True)
            print(slovo_list)
        elif a==8:
            slovo_list.sort
            print(slovo_list)
        elif a==9:
            b=int(input("Какой элемент удалить?: "))
            slovo_list.pop(b)
            print(slovo_list)
        elif a==10:
            b=input("Введите букву: ")
            i=int(input("Введите позицию: "))
            slovo_list.insert(i-1,b)
            print(slovo_list)
        elif a==11:
            print("Хорошо, до встречи!")
            break
    except:
        ValueError
        print("Что-то не так")
