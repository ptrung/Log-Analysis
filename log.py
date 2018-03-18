#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

q1 = """SELECT articles.title, count(*) AS num
        FROM articles JOIN log
        ON log.path = '/article/' || articles.slug
        GROUP BY articles.title
        ORDER BY num desc
        LIMIT 3"""

q2 = """SELECT author.name, sum(count.num) AS sum
        FROM (
            SELECT authors.name AS name, articles.title AS title
            FROM authors JOIN articles
            ON authors.id = articles.author
        ) AS author
        JOIN (
            SELECT articles.title AS title, count(*) AS num
            FROM articles JOIN log
            ON log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY num desc
        ) AS count
        ON author.title = count.title
        GROUP BY author.name
        ORDER BY sum desc"""

q3 = """SELECT data.date, round(data.percent, 2)
        FROM (
            SELECT error.date AS date,
                (error.count::NUMERIC / ok.count::NUMERIC * 100) AS percent
            FROM (
                SELECT date(time) AS date, count(status) AS count
                FROM log WHERE status = '404 NOT FOUND'
                GROUP BY date(time)
                ORDER BY date(time)
            ) AS error
            JOIN (
                SELECT date(time) AS date, count(status) AS count
                FROM log
                GROUP BY date(time)
                ORDER BY date(time)
            ) AS ok
            ON error.date = ok.date
            ORDER BY error.date
        ) AS data
        WHERE data.percent > 1
        ORDER BY data.date desc"""


def print_popular_articles():
    """Prints the 3 most popular articles with their views

    Conntects to the default news database and
    prints their title with their views.
    """

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    print("\nTHE 3 MOST POPULAR ARTICLE:")
    c.execute(q1)

    result = c.fetchall()

    count = 1
    for title, num in result:
        print(count, ".", title, "-", num, "views")
        count += 1

    db.close()


def print_popular_authors():
    """Prints the most popular authors with their views

    Connects to the default news database and prints the author names
    with the summarized views of all their articles
    """

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    print("\nTHE MOST POPULAR AUTHORS:")
    c.execute(q2)

    result = c.fetchall()

    count = 1
    for name, sum in result:
        print(count, ".", name, "-", sum, "views")
        count += 1

    db.close()


def print_request_error():
    """Prints the days on which more than 1% of the request lead to error

    Connects to the default news database and prints the date of the days
    on which more than 1% of the requests lead to error. Additionally,
    the percentage of the errors is displayed.
    """

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    print("\nDAYS ON WHICH MORE THAN 1% OF REQUESTS LEAD TO ERROR:")
    c.execute(q3)

    result = c.fetchall()

    count = 1
    for date, percent in result:
        print(count, ".", date, "-", percent, "%")

    db.close()


print_popular_articles()
print_popular_authors()
print_request_error()
