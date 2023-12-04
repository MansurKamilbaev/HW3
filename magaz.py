sklad = {'Яблоко': 10, 'Апельсин': 20, 'Мандарин': 15, 'Банан': 13, 'Киви': 18}
cart = {}

while True:
    choice = input(
        '1)Добавить в корзину\n2)Удалить из корзины\n3)Заменить в корзине\n4)Посмотреть корзину\nКакое действие хотите выбрать? ')

    if choice == "1":
        print(sklad)
        product = input('Выберите товар: ')
        if product in sklad:
            count = int(input('Введите кол-во товара: '))
            if sklad[product] >= count:
                sklad[product] -= count
                cart[product] = count
                print(f'Товар {product} успешно добавлен в корзину')
            else:
                print('На складе нету такого кол-во товара!')

        else:
            print("Такой товар отсутcвует в складе!")


    elif choice == "2":
        print(cart)
        product = input('Какой товар хотите удалить: ')
        cart.pop(product)
        print('Ваш товар удален из корзины ! ')

    elif choice == "3":
        print(cart)
        product = input("Выберите товар,который хотите заменить: ")
        cart.pop(product)
        print(sklad)
        new_product = input("Выберите товар,который хотите добавить вместо другого вами выбранного товара: ")
        new_count = int(input("Введите кол-во товара: "))
        if sklad[new_product] >= new_count:
            sklad[new_product] -= new_count
            cart[new_product] = new_count
            print("Ваш товар успешно заменен!")

        else:
            print("Ошибка")



    elif choice == "4":
        print(cart)