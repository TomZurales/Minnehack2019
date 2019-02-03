from flask import Flask, jsonify, request, abort
import psycopg2
import database

dbhost = 'http://35.192.186.196:5432'

# app = Flask(__name__)
#
# @app.route('/tasks/tasks', methods=['GET'])
# def getTasks():
#     pass
#     # return getTasksFromDatabase()
#
# @app.route('/tasks/completeTask', methods=['POST'])
# def completeTask():
#     if not request.json:
#         abort(400)
#     # task = buildHistoricalTask(request.json)
#     # addTaskToTaskHistory(task)
#     # removeTaskFromTodo(task)
#     # addCreditsToUser(task)
#
# @app.route('/users/userData/<int:user_id>', methods=['GET'])
# def getUserData(user_id):
#     pass
#     # return getUserFromDatabase(user_id)
#
# @app.route('/users/id/<int:rfid_number>', methods=['GET'])
# def getUserIdByRFID(rfid_number):
#     pass
#     # return getUserIdFromDatabase(rfid_number)
#
# @app.route('/taskHistory/tasks/<int:user_id>', methods=['GET'])
# def getTaskHistoryById(user_id):
#     pass
    # return getTaskHistoryFromDatabase(user_id)

database.connect()