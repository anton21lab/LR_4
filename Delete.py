from clsSport import Sport

# создать объект базы данных
database_Sport = Sport()


# удаление по id спорта
def delete_command(id):
    database_Sport.delete(id)
    print(f"Данные по спорту  с id = {id} удалены")


# просмотр всех записей
def view_command():
    for row in database_Sport.view():
        print(row)


# основная программа
print("Список спорта")
view_command()

id_delete = int(input("Введите id спорта "))
delete_command(id_delete)

print("Список спорта")
view_command()
