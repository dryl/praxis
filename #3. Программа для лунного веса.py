def moon_weight():
    import sys
    import time
    print(time.asctime())
    print()
    print('Эта программа для расчета Вашего веса на луне')
    print('Введите ваш нынешний земной вес')
    ves = int(sys.stdin.readline())
    print('Введите ежегодный прирост вашего веса')
    kg = int(sys.stdin.readline())
    print('На какое количество лет расчитать')
    let = int(sys.stdin.readline())      
    for g in range(2018,(2018+let)):
        luna=ves*0.165
        print('Год %s = Вес %s' % (g,luna))
        ves=ves+kg
    print()
    print(time.asctime())
    
moon_weight()

