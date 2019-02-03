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
            taskDict['task_id'] = task[4]
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
    def getUser(self, userId):
        sql = "SELECT * FROM users WHERE id = %s"
        self.cur.execute(sql, ([userId]))
        user = self.cur.fetchone()
        print(user)
        return user
    def getUserIdByRfid(self, rfidNumber):
        sql = "SELECT * FROM users WHERE card_number = %s"
        self.cur.execute(sql, ([rfidNumber]))
        user = self.cur.fetchone()
        return user
    def getTaskHistory(self, userId):
        sql = "SELECT * FROM task_history WHERE user_id = %s"
        self.cur.execute(sql, ([userId]))
        history = self.cur.fetchall()
        return history
    
    def getAuctions(self):
        sql = "SELECT * FROM auctions"
        self.cur.execute(sql)
        auctions = self.cur.fetchall()
        auctionsList = []
        for auction in auctions:
            auctionsDict = {}
            auctionsDict['id'] = auction[0]
            auctionsDict['name'] = auction[1]
            auctionsDict['current_bid'] = auction[2]
            auctionsDict['highest_bidder'] = auction[3]
            auctionsDict['end_date'] = auction[4]
            auctionsList.append(auctionsDict)
        return auctionsList

    def bid(self, auction, ammount, user):
        sql = "UPDATE auctions SET current_bid = current_bid + %s, highest_bidder = %s WHERE id = %s"
        self.cur.execute(sql, (ammount, user, auction))
        self.conn.commit()
        sql = "UPDATE users SET balance = balance - %s WHERE id = %s"
        self.cur.execute(sql, (ammount, user))
        self.conn.commit()
