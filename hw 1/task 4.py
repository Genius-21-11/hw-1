# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
S = int(input("Введите общее количество журавликов: ")) 
if not S % 6: 
    x = S // 6 
print(f'Катя сделала {x * 4} журавликов ') 
print(f'Сережа сделал {x} журавликов') 
print(f'Петя сделал {x} журавликов')
