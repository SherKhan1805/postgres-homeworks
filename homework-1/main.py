"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(host="localhost", database="north", user="postgres", password="alexia1456") as conn:
    with conn.cursor() as cur:
        with open("north_data/employees_data.csv", newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, "
                            "notes) VALUES (%s, %s, %s, %s, %s, %s);", (
                                item["employee_id"], item["first_name"], item["last_name"], item["title"],
                                item["birth_date"], item["notes"]))

        with open("north_data/customers_data.csv", newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s);",
                            (item["customer_id"], item["company_name"], item["contact_name"]))

        with open("north_data/orders_data.csv", newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                cur.execute(
                    "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                    "VALUES (%s, %s, %s, %s, %s);",
                    (item["order_id"], item["customer_id"], item["employee_id"], item["order_date"],
                     item["ship_city"]))

        conn.commit()

