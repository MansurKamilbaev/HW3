#Сдаем бутылки
Summa_butilki1=0.10
Summa_butilki2=0.25

Butilka=int(input("Введите количество бутылок <=1 литра: "))
Butilka2=int(input("Введите количество бутылок >1 литра: "))
summa=(Butilka*Summa_butilki1)+(Butilka2*Summa_butilki2)
print(f'Сумма выручки: { summa } $')

#Налоги и чаевые
summa_zakaza=float(input("Введите сумму заказа: "))
raschet_naloga=summa_zakaza * 0.12
raschet_chaevih=(summa_zakaza - raschet_naloga)*0.18
itogo=summa_zakaza+raschet_naloga+raschet_chaevih
print(f'Налог: {raschet_naloga} $')
print(f'Сумма чаевыех: {raschet_chaevih} $')
print(f'Итоговая сумма: {itogo} $')

#Сумма первых n положительных чисел
chislo=int(input("Введите натуральное положительное число: "))

if chislo<=0:
    print("Введенное число не положительное")
else:
    d=0
    for i in range(1,chislo+1):
        d+=1
    print(f'Сумма натуральных чисел от 1 до {chislo} : {d}')

#Сувениры и безделушки
suvenir=int(input("Введите количество сувениров: "))
bezdelushki=int(input("Введите количество безделушек: "))
ves=suvenir*75
ves2=bezdelushki*112
obshiy_ves=ves+ves2
print(f'Общий вес посылки составляет: {obshiy_ves} г')