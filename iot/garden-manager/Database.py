import psycopg2
from dbconfig import config
from datetime import datetime, timedelta

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
        self.cur.execute('SELECT * FROM Tasks ORDER BY value')
        tasks = self.cur.fetchall()
        tasksArr = []
        for task in tasks:
            date = task[3]
            taskDict = dict() 
            taskDict['name'] = task[1]
            taskDict['value'] = task[0]
            if (date + timedelta(days=task[2])) <= datetime.today().date():
                tasksArr.append(taskDict)
        return tasksArr

    def addTaskToTaskHistory(self, finishedTask):
        print(finishedTask)
        sql = "INSERT INTO task_history(task_id, completed, user_id) VALUES(%s,%s,%s);"
        self.cur.execute(sql, (finishedTask["task_id"], finishedTask["completed"], finishedTask["user_id"]))
        self.conn.commit()
    def updateTaskDate(self, taskId):
        date = datetime.today().date()
        sql = "UPDATE tasks SET last_completed = %s WHERE id = %s"
        self.cur.execute(sql, (date, taskId))
        self.conn.commit()
    def addCreditsToUser(self, userId, value):
        sql = "UPDATE users SET balance = balance + %s WHERE id = %s"
        self.cur.execute(sql, (value, userId))
        self.conn.commit()
    
