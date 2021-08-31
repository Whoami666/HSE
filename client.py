import commonTHEfirst
passbase = open("passwords", 'r')
number_of_clients = sum(1 for _ in passbase)
order_in_progress_empty = []
for i in range(number_of_clients+1):
    order_in_progress_empty.append([i, 0, 0, []])
passbase.close()
passbase = open("passwords", 'r')
#ордеринпрогресс[tag, дата, номер заказа, состав]


def pay(users_cart, users_tag, order_in_progress, history):
    for user_tag in history:
        if users_tag not in history:
            history[users_tag] = order_in_progress
        else:
            history[users_tag] += order_in_progress
    orders_number = order_in_progress[users_tag][2]
    order_in_progress[users_tag] = [0, 0, orders_number+1, []]
    users_cart = {}
    print("оплата прошла успешно")
    menu(users_cart, users_tag, order_in_progress, history)


def add_an_item(users_cart, users_tag, order_in_progress, history):
    print(commonTHEfirst.read_catalog())
    while True:
        print("выберите товары из каталога, вводя номер товара, введите 0, если закончили редактирование")
        item = input()
        if item.isdigit() and commonTHEfirst.count_overall_catalog() >= int(item) > 0:
            break
        elif item == "0":
            print("введите 1, чтобы оплатить заказ или введите любое другое значение, чтобы выйти")
            answer = input()
            if answer == "1":
                pay(users_cart, users_tag, order_in_progress, history)

            break
        else:
            print("введите корректные значения")
    if item != "0":
        while True:
            print("введите количество выбранного товара")
            possible_amount = commonTHEfirst.count_product(int(item))
            amount = input()
            if amount.isdigit() and possible_amount >= int(amount) > 0:
                if int(item) in users_cart:
                    if possible_amount - int(users_cart[int(item)]) - int(amount) < 0:
                        print("Недостаточно товара")
                    else:
                        print("товар добавлен в заказ")
                        users_cart[int(item)] += int(amount)
                        for good in users_cart:
                            order_in_progress[users_tag][3] += [good, users_cart[good]]
                    break
                else:
                    print("товар добавлен в заказ")
                    users_cart[int(item)] = int(amount)
                    for good in users_cart:
                        order_in_progress[users_tag][3] += [good, users_cart[good]]
                    break
            else:
                print("Введите корректные значения")
    menu(users_cart, users_tag, order_in_progress, history)


def menu(users_cart, users_tag, order_in_progress, history):
    print("_______________MENU_______________________")
    print("Введите 0, чтобы посмотреть каталог")
    print("Введите 1, чтобы пройти авторизацию")
    print("Введите 2, чтобы создать заказ")
    print("Введите 3, чтобы просмотреть свои старые заказы")
    print("Введите 4, чтобы редактировать созданный заказ")
    x = input()
    if x.isdigit():
        x = int(x)
        if x == 0:
            print(commonTHEfirst.read_catalog())
            menu(users_cart, users_tag, order_in_progress, history)
        elif x == 1:
            print("введите логин без пробелов")
            login = input()
            print("введите пароль без пробелов")
            password = input()
            if login == "root" and password == "toor":
                print("Поздравляю, вы админ")
                users_tag = 0
            else:
                profile = passbase.readline().split(";")
                while len(profile) == 3:
                    if profile[0] == login and profile[1] == password:
                        users_tag = int(profile[2])
                        break
                    else:
                        profile = passbase.readline().split(";")
            if users_tag == -1:
                print("Неверный логин или пароль")
                menu(users_cart, users_tag, order_in_progress, history)
            else:
                print("Добро пожаловать,", login)
                menu(users_cart, users_tag, order_in_progress, history)
        elif x == 2:
            if users_tag != -1:
                print("введите сегодняшнее число")
                probably_the_date = input()
                order_in_progress[users_tag][1] = probably_the_date
                add_an_item(users_cart, users_tag, order_in_progress, history)
            else:
                print("залогиньтесь")
                menu(users_cart, users_tag, order_in_progress, history)

        elif x == 3:
            if users_tag != -1:
                for orders in history:
                    print(history[orders])
                menu(users_cart, users_tag, order_in_progress, history)
            else:
                print("залогиньтесь")
                menu(users_cart, users_tag, order_in_progress, history)
            try:
                print(history[users_tag])
                menu(users_cart, users_tag, order_in_progress, history)
            except KeyError:
                print("у вас нет истории заказов")
                menu(users_cart, users_tag, order_in_progress, history)

        elif x == 4:
            if users_tag != -1:
                count_cart = 0
                for goods in users_cart:
                    print(commonTHEfirst.name_from_numbers(goods), users_cart[goods])
                    count_cart += 1
                if count_cart == 0:
                    print("у вас нечего редактировать =)")
                    menu(users_cart, users_tag, order_in_progress, history)
                else:
                    add_an_item(users_cart, users_tag, order_in_progress, history)
            else:
                print("залогиньтесь")
                menu(users_cart, users_tag, order_in_progress, history)
    else:
        print("некорректное значение")
        menu(users_cart, users_tag, order_in_progress, history)


menu({}, -1, order_in_progress_empty, {})
