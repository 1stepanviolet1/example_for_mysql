from pymysql import connect
from pymysql.cursors import DictCursor
from config import (
    host,
    port,
    user,
    pwd,
    db_name
)


def create_table(cursor: DictCursor):
    cursor.execute("CREATE TABLE users (id int AUTO_INCREMENT, username varchar(255), pwd varchar(255), PRIMARY KEY (id))")

def insert_data(cursor: DictCursor):
    cursor.execute("INSERT INTO users (username, pwd) VALUES ('root2', 'als2')")

def select_all_data(cursor: DictCursor):
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

def update_data(cursor: DictCursor):
    cursor.execute("UPDATE users SET pwd = 'alsals' WHERE username = 'root2'")

def delete_data(cursor: DictCursor):
    cursor.execute("DELETE FROM users WHERE pwd = 'pwd1'")

def delete_table(cursor: DictCursor):
    cursor.execute("DROP TABLE users")


def main():
    db = connect(
        host=host,
        port=port,
        user=user,
        passwd=pwd,
        database=db_name,
        cursorclass=DictCursor
    )

    with db.cursor() as cursor:
        # create_table(cursor)
        # insert_data(cursor)
        # select_all_data(cursor)
        # update_data(cursor)
        # delete_data(cursor)
        # delete_table(cursor)

        db.commit()

    db.close()


if __name__ == '__main__':
    main()
