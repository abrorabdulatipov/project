while True:
    son1 = int(input('1-Soningizni kiriting'))
    i = 50
    if son1 > 0 and son1 %2 !=0:
        print(' toq son')
    elif (son1 <0) and (son1 %2 ==0):
        print(' juft son')
    elif son1 < 0 and son1 % 1 ==0:
        print(' toq son')
    elif son1 == 0 :
        print('son 0 teng')
    else:
        print('juft son')
        print(i)
