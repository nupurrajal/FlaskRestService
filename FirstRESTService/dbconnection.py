import MySQLdb


def get_cursor():
    try:
        db_conn = MySQLdb.connect(host="localhost", user="root", passwd="12345691@Nn", db="laptop_quotation")
    except:
        print("Error in connection to db")
        return 0
    print("Connection successful")
    cursor = db_conn.cursor()
    return cursor, db_conn
