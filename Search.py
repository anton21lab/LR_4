from clsSport import Sport

# создать объект базы данных
database_Sport = Sport()


# просмотр всех записей
def view_command():
    for row in database_Sport.view():
        print(row)


# поиск по названию спорта
def search_command(name_sport):
    if len(database_Sport.search(name_sport)) > 0:
        for row in database_Sport.search(name_sport):
           print(row)
    else:
      print("Такого спорта нет")


# основная программа в консоли
# поиск по названию спорта
search_command(input("Название спорта? "))
