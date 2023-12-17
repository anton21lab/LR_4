import sqlite3


# создание класса БД
class Sport:
    # конструктор класса
    def __init__(self):

                # Подключение к БД
                self.con = sqlite3.connect("Sport.db")
                # Создание курсора
                self.cur = self.con.cursor()
                # Создание таблицы БД
                self.cur.execute(
                "CREATE TABLE IF NOT EXISTS Sports "
                "(ID INTEGER PRIMARY KEY,"
                "name_sport TEXT,"
                "unit_of_measurement INTEGER,"
                "world_record TEXT,"
                "record_date INTEGER,"
                "The_athlete's_full_name TEXT)"

                )
                # сохранить изменения
                self.con.commit()

    def __del__(self):

                    # отключение от БД
     self.con.close()

    def view(self):

    # просмотр всех записей в таблице БД
     self.cur.execute("SELECT * FROM Sports")
    # список всех записей из таблицы
     rows = self.cur.fetchall()
     return rows

    def insert(self, name_sport

               , unit_of_measurement, world_record, record_date, The_athlete's_full ):

     # добавить запись
     self.cur.execute("INSERT INTO world_record "
                     "VALUES (NULL, ?, ?, ?, ?, ? )",
                     (name_sport,unit_of_measurement, world_record, record_date, The_athlete's_full ))
     self.con.commit()

    def update(self, id, name_sport, unit_of_measurement, world_record, record_date, The_athlete's_full):


     self.cur.execute("UPDATE world_record SET "
                     "name_sport=?, unit_of_measurement=?, world_record=?, record_date=?, The_athlete's_full=? "
                     "WHERE ID = ?",
                     (name_sport, unit_of_measurement, world_record,
                      record_date, The_athlete's_full,  id,))
     self.con.commit()

    def delete(self, id):

    # удаление записи
     self.cur.execute("DELETE FROM world_record "
                     "WHERE ID=?", (id,))
     self.con.commit()

    def search(self, name_sport):

        self.cur.execute("SELECT unit_of_measurement, world_record FROM world_record "
                         "WHERE name_sport=?", (name_sport,))
        rows = self.cur.fetchall()
        return rows
