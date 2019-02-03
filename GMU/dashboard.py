from PyQt5.QtWidgets import *
import json

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

rawJson = '{ \
    "tasks": [ \
        { \
            "id": "1", \
            "name": "Water the tomatoes", \
            "value": "5 kernels" \
        }, \
        {\
            "id": "2",\
            "name": "Pick the peas",\
            "value": "10 kernels" \
        }\
    ]\
}'

inJson = json.loads(rawJson)

class myButton(QPushButton):
    def __init__(self, name, onClickValue):
        super(myButton, self).__init__(name)
        self.name = name
        self.onClickValue = onClickValue
        super(myButton, self).clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        # None
        alert = QMessageBox()
        alert.setText('You clicked ' + self.onClickValue)
        alert.exec_()



def main():
    buildTasks()
    window.setLayout(layout)
    window.show()
    app.exec_()

def buildTasks():
    for task in inJson['tasks']:
        taskName = str(task['name'])
        button = myButton(taskName, taskName)
        layout.addWidget(button)
        print("taskname: " + taskName)

    # print()


if __name__ == "__main__":
    main()