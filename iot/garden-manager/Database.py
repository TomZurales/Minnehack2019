import psycopg2
from dbconfig import config

class Database:
    conn = None
    cur = None
    def connect(self):
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)

            # create a cursor
            self.cur = self.conn.cursor()

            # execute a statement
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
        print('Database connection closed.')

    def getTasks(self):
        self.cur.execute('SELECT * FROM Tasks LIMIT 10')
        tasks = self.cur.fetchone()
        print(tasks)

    def addTaskToTaskHistory(self, finishedTask):
        sql = "INSERT INTO task_history(task_id, completed, user_id) VALUES(%s,%s,%s);"
        self.cur.execute(sql, (finishedTask["task_id"], finishedTask["completed"], finishedTask["user_id"]))
        self.conn.commit()