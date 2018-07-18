import random


for n in range(10):
    tab = {} # Cловарь для таблици сложения -> dict('term1 + term2' : int(ответ))
    term1 = random.randint(0, 10) # Первое слогаемое -> случайное целое число
    
    # формирование словаря с таблицей ключей и значений 
    for term2 in range(11): 
        sample = str(term1) + ' + ' + str(term2) # ключь словаря -> str(пример)
        tab[sample] = term1 + term2 # Добавление значений(решений)к ключам(примерам)
        
    # Выбор случайного примера из словаря
    example = random.choice(list(tab.keys())) # random.choice() - случайный элемент
                                              # непустой последовательности
    print(example) # Печать примера
    answer = int(input('Ответ: ')) # Спрашиваем ответ пользователя

    # Проверяем правельный ли ответ пользователя
    if answer == tab[example]: # Если ответ равен значению словаря(решению)
        print('Правельный ответ')
    else:
        print('Неверно ', example, '=', tab[example]) # Иначе вывести правельный ответ

print('The End!')
