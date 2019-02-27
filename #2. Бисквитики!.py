t=int(input("количество бисквитов? "))

if t >= 100 and t <= 500:
    print("Норм")
elif t < 100:
    print('Мало')
elif t > 500:
    print('Много')
else:
    print("я хз")
