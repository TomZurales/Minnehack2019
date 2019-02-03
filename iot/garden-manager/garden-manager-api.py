from flask import Flask, jsonify, request, abort
import psycopg2
from Database import Database
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

database = Database()
database.connect()

def getTasksFromDatabase():
    return jsonify({"tasks": database.getTasks()})

def buildFinishedTask(requestJson):
    finishedTask = {}
    try:
        finishedTask['task_id'] = requestJson["id"]
        finishedTask['completed'] = requestJson["completed"]
        finishedTask['user_id'] = requestJson["user_id"]
        return finishedTask
    except:
        print("Bad task data received")

def addTaskToTaskHistory(finishedTask):
    database.addTaskToTaskHistory(finishedTask)

def updateTaskDate(taskId):
    database.updateTaskDate(taskId)

def addCreditsToUser(userId, value):
    database.addCreditsToUser(userId, value)
@app.route('/tasks/tasks', methods=['GET'])
def getTasks():
    return getTasksFromDatabase()

@app.route('/tasks/completeTask', methods=['POST'])
def completeTask():
    print(request.json)
    if not request.json:
        abort(400)
    finishedTask = buildFinishedTask(request.json)
    addTaskToTaskHistory(finishedTask)
    updateTaskDate(finishedTask["task_id"])
    addCreditsToUser(finishedTask["user_id"], request.json["value"])
    return ("",201,)

@app.route('/users/userData/<int:user_id>', methods=['GET'])
def getUserData(user_id):
    return jsonify({"user": database.getUser(user_id)})

@app.route('/users/id/<int:rfid_number>', methods=['GET'])
def getUserIdByRFID(rfid_number):
    return jsonify({"user": database.getUserIdByRfid(rfid_number)})

@app.route('/tasks/history/<int:user_id>', methods=['GET'])
def getTaskHistoryById(user_id):
    return jsonify({"history": database.getTaskHistory(user_id)})

@app.route('/auctions/auctions', methods=['GET'])
def getActiveAuctions():
    return jsonify({"auctions": database.getAuctions()})

@app.route('/auctions/bid', methods=['POST'])
def bid():
    if not request.json:
        abort(400)
    database.bid(request.json['auction'], request.json['ammount'], request.json['user'])
    return ("", 201,)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

