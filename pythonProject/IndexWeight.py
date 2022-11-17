class Man:

    while True:
         try:
             weight = float(input("Введите вес "))
             break
         except ValueError:
             print("Вы ввели не число!")

    while True:
         try:
             growth = float(input("Введите рост "))
             break
         except ValueError:
             print("Вы ввели не число!")

    index_of_weight = weight / (growth/ 100 * growth/100)

    print(f"Индекс массы тела равен: {index_of_weight}")

    if(index_of_weight< 18.5):
        print("Недостаточный вес")
    elif(index_of_weight< 25):
        print("Нормальный вес")
    elif(index_of_weight<30):
        print("Избыточный вес")
    else:
        print("Ожирение")



