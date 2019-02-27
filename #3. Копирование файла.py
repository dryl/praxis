import time
original = open('D:\\Андрей\\python\\программы\\упражнения\\origi.txt')
text = original.read()

copy = open('D:\\Андрей\\python\\программы\\упражнения\\copi.txt', 'w')
copy.write(text)
copy.close()
original.close()
copy = open('D:\\Андрей\\python\\программы\\упражнения\\copi.txt')
print(copy.read())
print()
print(time.asctime())
