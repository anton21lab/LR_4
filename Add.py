from clsSport import Sport

# создать объект базы данных
database_Sport = Sport()


# логика
# добавление записи
def add_command(id, name_sport, unit_of_measurement, world_record, record_date, The_athlete's_full_name ):
    (id, name_sport, unit_of_measurement, world_record, record_date, The_athlete's_full_name )


# просмотр всех записей
def view_command():
    for row in database_Sport.view():
        print(row)


# основная программа в консоли
# добавление записи
for i in range(5):
    add_command(input("Название спорта:"),
                    float(input("единица измерения:")),
                    input("мировой рекорд:"),
                    float(input("дата рекорда:")),
                    input("ФИО спортсмена:"))
# просмотр всех записей
view_command()
