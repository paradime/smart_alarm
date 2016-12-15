from multiprocessing import Process, Queue
from flask import Flask
from AlarmController import AlarmController
app = Flask(__name__)

alarmController = AlarmController()
@app.route("/start")
def start():
    return alarmController.start()

@app.route('/stop')
def stop():
    return alarmController.stop()

if __name__ == "__main__":
    Process(target=alarmController.loop).start()
    app.run(host='0.0.0.0')
