"""1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию."""
import os

# os.help
import shutil

money = 0
shop_list = []
# kategory_shop = []
while True:
    print('1. Создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')
#    print(money)

    choice = input('Выберите пункт меню')
    if choice == '1':
        dir_name = input('введите название создаваемой папки')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    elif choice == '2':
        dir_name = input('введите название удаляемой папки/файла')
        if os.path.exists(dir_name):
            os.remove(dir_name)

    elif choice == '3':
        file_name = input('введите название копируемого файла')
        shutil.copy(file_name, f'copy_{file_name}')

    elif choice == '4':
        for dirpath, dirnames, filenames in os.walk("."):
            # перебрать каталоги
            for dirname in dirnames:
                print("Каталог:", os.path.join(dirpath, dirname))
            # перебрать файлы
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))

    elif choice == '5':
        for dirpath, dirnames, filenames in os.walk("."):
            # перебрать каталоги
            for dirname in dirnames:
                print("Каталог:", os.path.join(dirpath, dirname))

    elif choice == '6':
        for dirpath, dirnames, filenames in os.walk("."):
            # перебрать файлы
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))
    elif choice == '7':
        # info_os = int(os.name())
        # print(info_os)
    elif choice == '8':
        print('создатель программы Илдус')
    elif choice == '9':
        # Играть в викторину
    elif choice == '10':
        price = int(input('введите стоимость покупки'))
        if price < money:
            money = money - price
            kategory_shop = input('введите категорию товара')
            shop_list.append((kategory_shop, price))
            print(f'На счету осталось {money} рублей')
        else:
            print('Извините денег на счету не достаточно для покупки товара')
    elif choice == '11':
       # Сменить директорию
    elif choice == '3':
        print(f'Вами были совершены следующие покупки ', shop_list)
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')