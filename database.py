from sqlite3 import connect
from sqlite3 import Connection,Error


def connection() ->Connection:
    try:
            return connect("tasks.db")

    except Error as e:
            print("the database is not connected")

def create_table():
    conn=connection()
    cur=conn.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS tasks( 
        id INTEGER PRIMARY KEY, 
        title TEXT,
          description TEXT,
          priority TEXT, 
          status TEXT
          )""")
    
    conn.commit()
    conn.close()

def insert_task(title,description,priority,status):
    conn = connection()
    cur=conn.cursor()

    cur.execute(""" INSERT INTO tasks(title,description,priority,status)
    VALUES(?,?,?,?)""",
    (title,description,priority,status))

    conn.commit()
    conn.close()

def get_task():
      conn= connection()
      cur=conn.cursor()

      cur.execute("SELECT * FROM tasks")

      tasks=cur.fetchall()
      conn.close()
      return tasks

def get_task_by_id(task_id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))

    tasks=cur.fetchone()
    conn.close()
    return tasks

def update_task(task_id,status):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
    "UPDATE tasks SET status = ? WHERE id = ?",
    (status, task_id))

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM tasks WHERE id = ?",
    (task_id,))

    conn.commit()
    conn.close()




