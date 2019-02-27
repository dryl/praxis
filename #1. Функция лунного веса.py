def moon_weight(ves,kg):    
    
    for g in range(2018, 2033):
        luna=ves*0.165
        print('Год %s = Вес %s' % (g,luna))
        ves=ves+kg

moon_weight(30, 0.25)
