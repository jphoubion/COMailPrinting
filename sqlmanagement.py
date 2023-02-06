import sqlite3


def setup_connection(db_name):
    db = sqlite3.connect(db_name, )
    cursor = db.cursor()
    return db, cursor

def data_exists(cursor):
    try:
        req = cursor.execute("SELECT * FROM customers")
        datas = req.fetchall()
        if len(datas) == 0:
            return None
        else:
            return True
    except sqlite3.OperationalError as e:
        return None

def get_result(conn, req):
    cursor = conn.cursor()
    cursor.execute(req)
    return cursor.fetchall()

def drop_create_tables(conn, cursor):
    cursor.execute("DROP TABLE IF EXISTS co")
    conn.commit()
    cursor.execute("DROP TABLE IF EXISTS customers")
    conn.commit()
    cursor.execute("DROP TABLE IF EXISTS companies")
    conn.commit()

    cursor.execute("CREATE TABLE 'co' ('id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \
                                    'co_name' TEXT NOT NULL UNIQUE, \
                                    'co_address'	TEXT NOT NULL, \
                                    'is_lawyer' INTEGER NOT NULL, \
                                    'is_cpas' INTEGER NOT NULL)")
    conn.commit()

    cursor.execute("CREATE TABLE 'customers' ( \
                    'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \
                    'customer_code'	TEXT NOT NULL UNIQUE, \
                    'customer_name'	TEXT NOT NULL, \
                    'co_id'	INTEGER, \
                    FOREIGN KEY('co_id') REFERENCES 'co'('id') ON DELETE RESTRICT );")
    conn.commit()

    cursor.execute("CREATE TABLE 'companies' ( \
                                'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \
                                'company_name'	TEXT NOT NULL UNIQUE, \
                                'company_type'	TEXT NOT NULL)")
    conn.commit()




