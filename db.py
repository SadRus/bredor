import psycopg2


# conn = psycopg2.connect(
#     database="myproject",
#     user="user",
#     password="password",
#     host="localhost",
#     port=5432,
# )
# можно так
# conn = psycopg2.connect('postgres://sadrus:3095247@localhost:5432/myproject')

# cur.execute(
#     "CREATE TABLE users (id SERIAL PRIMARY KEY, userId VARCHAR(64), title VARCHAR(64), completed VARCHAR(64))"
# )
# conn.commit()


def save_data_to_db(cur, conn, id, userId, title, completed):
    cur.execute(
        "INSERT INTO users (id, userId, title, completed) "
        "VALUES (%s, %s, %s, %s)",
        [id, userId, title, completed])
    conn.commit()
    # cur.close()


def show_users_table(cur):
    cur.execute("SELECT * FROM users;")
    print(cur.fetchall())
    cur.close()


# conn.close()
