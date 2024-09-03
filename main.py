import psycopg2
import requests
from dotenv import load_dotenv

from db import save_data_to_db, show_users_table


def main():
    load_dotenv()

    url = 'https://jsonplaceholder.typicode.com/todos/1'
    headers = {}
    payload = {}

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    raw_data = response.json()

    conn = psycopg2.connect(
        database="myproject",
        user="user",
        password="password",
        host="localhost",
        port=5432,
    )
    cur = conn.cursor()

    save_data_to_db(
        cur=cur,
        conn=conn,
        **raw_data,
    )
    show_users_table(cur=cur)

    conn.close()


if __name__ == '__main__':
    main()
