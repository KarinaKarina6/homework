def f(t):
    p1=1
    p2=1
    for i in range(2,t+1,1):
        p1+=1/i
        p2+=((-1)**(i-1))/i
    print('Через '+str(t)+' решений мужчина окажется в '+str(round(p2,2))+' км от дома')
    print('Мужчина пройдет ' + str(round(p1,2))+' км')
n=int(input("Введите количество решений: "))
f(n)
