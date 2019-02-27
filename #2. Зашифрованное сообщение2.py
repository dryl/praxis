import time
a=(input("Введите шифр "))

# a="этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"
a=a.split(' ')
length = len(a)
a=(a[0:length:2])
print(' '.join(a))
print()
print(time.asctime())
input()

