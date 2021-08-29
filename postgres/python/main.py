import configparser

import psycopg2


if __name__ == "__main__":
    parser = configparser.ConfigParser()
    parser.read("pipeline.conf")

    dbname = parser.get("postgres_config", "database")
    user = parser.get("postgres_config", "username")
    password = parser.get("postgres_config", "password")
    host = parser.get("postgres_config", "host")
    port = parser.get("postgres_config", "port")

    conn = psycopg2.connect(
        f"dbname={dbname} user={user} password={password} host={host}",
        port=port
    )
    query = "SELECT * FROM store;"
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)

    query = "SELECT * FROM product;"
    cursor = conn.cursor()
    cursor.execute(query)
    for each in cursor:
        print(each)
