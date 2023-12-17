from clsSport import Sport

# создать объект базы данных
database_Sport = Sport()


# обновление по id спортсменам
def update_command(id, name_sport, unit_of_measurement, world_record, record_date, The_athlete's_full_name ):
    (id, name_sport, unit_of_measurement, world_record, record_date, The_athlete's_full_name )
    print(f"Данные спорта  с id = {id} обновлены")


# просмотр всех записей
def view_command():
    for row in database_Sport.view():
        print(row)


# основная программа
print("Список спорта")
view_command()
id_update = int(input("Введите id спорта "))
print("Укажите новые данные: ")
name_sport = input("Название спорта")
unit_of_measurement = float(input("единица измерения"))
world_record = input("мировой рекорд")
record_date = float(input("дата рекорда"))
The_athlete's_full_name = input("ФИО спортсмена")
update_command(id_update, name_sport, unit_of_measurement, world_record, record_date, The_athlete's_full_name )
print("Список спорта ")
view_command()
