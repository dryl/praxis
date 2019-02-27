def moon_weight(ves,kg,let):    
    
    for g in range(2018,(2018+let)):
        luna=ves*0.165
        print('Год %s = Вес %s' % (g,luna))
        ves=ves+kg

moon_weight(90, 0.25, 5)
