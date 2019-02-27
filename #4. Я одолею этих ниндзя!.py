ninjas = int(input('Сколько ниндзя против меня? '))
if ninjas >= 30 and ninjas <= 49 :
    print('«Их слишком много»')
elif ninjas >= 10 and ninjas <= 29 :
    print('«Будет непросто, но я с ними разделаюсь»')
elif ninjas <= 9:
    print('«Я одолею этих ниндзя!»')
else:
    print('я умру')
