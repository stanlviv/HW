# 1.  Роздрукувати всі парні числа менші 100 
# (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

# i=0
# while i < 100:
#     if i%2==0:
#         print(i)
#     i +=1


# for x in range(0,100,2):
#     print(x)

# 2.  Роздрукувати всі непарні числа менші 100. 
# (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

# i=0
# while i < 100:
#     if i%2==1:
#         print(i)
#     i +=1


# 3.  Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)
# 1.  Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))

# if num1 > num2:
#     print("number {} is greater than number {}".format(num1, num2))
# else:
#     print("number {} is greater than number {}".format(num2, num1))

# 2.  Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# if num1 %2==0:
#     print("{} this is an even number".format(num1))
# else:
#     print("{} this is an even number".format(num2))

# 3.  Написати скрипт, який обчислить факторіал введеного числа.

numr = int(input("Enter Your number: "))
fctr = 1

for n in range(1,numr+1):
    fctr = fctr*n
    print(fctr)