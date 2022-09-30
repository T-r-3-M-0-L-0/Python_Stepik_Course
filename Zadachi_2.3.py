# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. 
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# Напишите программу, на вход которой даются четыре числа a a a, b b b, c c c и d d d, каждое в своей строке. 
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d] [c;d] [c;d].              
# Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. 
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

def f1():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    for h in range(c, d+1):
        print('\t', h, end='')
    print(end='\n')
    for i in range(a, b+1):
        print(i, '\t', end='')
        for j in range(c, d+1):
            print(i*j, end='\t')
        print(end='\n')
f1()


# Напишите программу, которая считывает с клавиатуры два числа a a a и b b b, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b] [a; b] [a;b], которые кратны числу 3 3 3.
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12] . Всего чисел, делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.

def f2():
    a = int(input())
    b = int(input())
    s = 0
    m = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            s += i
            m += 1
    print(s / m)
f2()