import gi
from time import sleep
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import requests
import json
import serial
import datetime

from threading import Thread


# myRequest = None#= requests.get('http://35.192.186.196/tasks/tasks')
# rawJson = None#= myRequest.text
# print(myRequest.text)
# inJson = None#= json.loads(rawJson)

window = Gtk.Window(title="Hello World")
hbox = Gtk.VBox(spacing=6)
window.connect("destroy", Gtk.main_quit)
window.set_default_size(400, 200)

port = '/dev/ttyACM0'
ser = serial.Serial(port, 115200, timeout=5)
# ser.baudrate(115200)


# window.add(hbox)
# layout = QVBoxLayout()

# rawJson = '{ \
#     "tasks": [ \
#         { \
#             "id": "1", \
#             "name": "Water the tomatoes", \
#             "value": "5 kernels" \
#         }, \
#         {\
#             "id": "2",\
#             "name": "Pick the peas",\
#             "value": "10 kernels" \
#         }\
#     ]\
# }'
instance = False
checked = []

def waitForCard():
    while True:
        while not (ser.readline()):
            sleep(.1)
        if len(checked) > 0:
            for button in checked:
                button.finish()
                checked.remove(button)

class myButton(Gtk.CheckButton):
    def __init__(self, name, taskid, value):
        super(myButton, self).__init__(name)

        self.name = name
        self.taskid = taskid
        self.value = value
        super(myButton, self).connect("toggled", self.on_button_clicked)

    def on_button_clicked(self, button):
        checked.append(self)
        print("clicked button " + self.name)

    def finish(self):
        self.hide()
        sendRequest = requests.post('http://35.192.186.196/tasks/completeTask', json={'id': str(self.taskid),
                                                                                      'completed': datetime.datetime.today().strftime(
                                                                                          '%Y-%m-%d'), 'user_id': '1',
                                                                                      'value': self.value})
        print(sendRequest.status_code)

def getData():
    myRequest = requests.get('http://35.192.186.196/tasks/tasks')
    rawJson = myRequest.text
    inJson = json.loads(rawJson)
    for task in inJson['tasks']:
        taskName = str(task['name'])
        value = str(task['value'])
        taskid = str(task['task_id'])
        button = myButton(taskName, taskid, value)
        hbox.pack_start(button, True, True, 0)


def getDataThreading():
    while True:
        myRequest = requests.get('http://35.192.186.196/tasks/tasks')
        rawJson = myRequest.text
        inJson = json.loads(rawJson)
        print("threading")
        for element in hbox.get_children():
            print(element)
            hbox.remove(element)
            # element.hide()
            sleep(.5)
        for task in inJson['tasks']:
            taskName = str(task['name'])
            button = myButton(taskName, taskName)
            button.show()
            hbox.pack_start(button, True, True, 0)
            # hbox.show_all()

        sleep(2)

def start():
    window.add(hbox)
    getData()
    window.show_all()
    cardHander = Thread(target=waitForCard)
    cardHander.start()
    print("Done with start")
    Gtk.main()


if __name__ == "__main__":
    start()



