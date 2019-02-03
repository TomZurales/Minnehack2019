from flask import Flask, jsonify, request, abort
import psycopg2
from Database import Database

app = Flask(__name__)

database = Database()
database.connect()
# @app.route('/tasks/tasks', methods=['GET'])
# def getTasks():
#     return getTasksFromDatabase()

@app.route('/tasks/completeTask', methods=['POST'])
def completeTask():
    print(request.json)
    if not request.json:
        abort(400)
    finishedTask = buildFinishedTask(request.json)
    addTaskToTaskHistory(finishedTask)
    return 201
    # removeTaskFromTodo(finishedTask["task_id"])
    # addCreditsToUser(finishedTask["user_id"], request.json["value"])

# @app.route('/users/userData/<int:user_id>', methods=['GET'])
# def getUserData(user_id):
#     pass
#     return getUserFromDatabase(user_id)

# @app.route('/users/id/<int:rfid_number>', methods=['GET'])
# def getUserIdByRFID(rfid_number):
#     pass
#     return getUserIdFromDatabase(rfid_number)
#
# @app.route('/taskHistory/tasks/<int:user_id>', methods=['GET'])
# def getTaskHistoryById(user_id):
#     return getTaskHistoryFromDatabase(user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

def getTasksFromDatabase():
    return jsonify({"tasks": database.getTasks()})

def buildFinishedTask(requestJson):
    finishedTask = {}
    try:
        finishedTask["task_id"] = requestJson["id"]
        finishedTask["time_completed"] = requestJson["time_completed"]
        finishedTask["user_id"] = requestJson["user_id"]
    except:
        print("Bad task data received")
def addTaskToTaskHistory(finishedTask):
    database.addTaskToTaskHistory(finishedTask)
