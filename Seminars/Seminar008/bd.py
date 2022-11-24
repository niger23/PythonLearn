import sqlite3


def create_table():
    try:
        sqlite_connection = sqlite3.connect('Seminars/Seminar008/monitors.db')
        sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    firm TEXT NOT NULL,
                                    model TEXT NOT NULL,
                                    resolution TEXT NOT NULL,
                                    size REAL NOT NULL,
                                    price REAL NOT NULL);'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


            # (firm,model,resolution,size,price)

def added_element (data):        
    sqlite_connection= sqlite3.connect('Seminars/Seminar008/monitors.db', timeout=20)
    cursor = sqlite_connection.cursor()

    cursor.executemany('INSERT INTO sqlitedb_developers (firm,model,resolution,size,price) VALUES (?, ?, ?, ?, ?)', [data])
    sqlite_connection.commit()
    cursor.close()

def delete_element (id_del):      
    sqlite_connection= sqlite3.connect('Seminars/Seminar008/monitors.db', timeout=20)
    cursor = sqlite_connection.cursor()

    cursor.execute('DELETE from sqlitedb_developers where id = ?', (id_del, ))
    sqlite_connection.commit()
    cursor.close()

def read_table ():
    all_data = []
    with sqlite3.connect('Seminars/Seminar008/monitors.db') as db:

        cursor = db.cursor()
        query = """SELECT * from sqlitedb_developers"""
        cursor.execute(query)
        all_data = cursor.fetchall()
    return all_data

def find_table (a,b,c,d):
    all_data = []
    with sqlite3.connect('Seminars/Seminar008/monitors.db') as db:

        cursor = db.cursor()
        sele = "SELECT * from sqlitedb_developers WHERE 1=1"
        if a != '':
            sele += " AND firm IN ('" + a + "')"
        if b != '':
            sele += " AND model IN ('" + b + "')"
        if c != '':
            sele += " AND resolution IN ('" + c + "')"
        if d != '':
            sele += " AND size IN ('" + d + "')"
        cursor.execute(sele)
        all_data = cursor.fetchall()
    return all_data
