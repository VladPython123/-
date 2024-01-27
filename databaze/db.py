
import psycopg2 

host = "  "
user  = "  "
password = "  "
port = "  "


connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
try:
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
    """CREATE TABLE users(
        id1 serial PRIMARY KEY,
        name_id varchar(50)  ,
        user_id varchar(50) ,
        press_id varchar(50) ,
        zakaz_bot INTEGER DEFAULT 0 );""",
            )
except Exception as ex:
    pass
        
