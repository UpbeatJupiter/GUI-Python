import sqlite3


def create_database():
    conn = sqlite3.connect("gradebook.db")
    cur = conn.cursor()
    cur.execute("""
    create table GradeBook (
        gid   integer primary key autoincrement,
        fname text,
        lname text,
        grade integer
    );
    """)
    conn.commit()
    conn.close()


def fill_database():
    conn = sqlite3.connect("gradebook.db")
    cur = conn.cursor()
    data = [('Melissa', 'Bishop', 70),
            ('Linda', 'Scanlon', 55),
            ('Russel', 'Gruver', 60),
            ('Maria', 'Mayes', 100),
            ('Dennis', 'Hill', 95),
            ('Nathan', 'Martin', 40),
            ('William', 'Biggs', 85),
            ('Lois', 'Ballard', 60),
            ('Larry', 'Manning', 50),
            ('Dustin', 'Smalls', 30),
            ('Alice', 'Lucas', 70),
            ('John', 'Howell', 90)]

    for x in data:
        cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", [x[0], x[1], x[2]])

    conn.commit()
    conn.close()


create_database()
fill_database()
