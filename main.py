#https://www.peopleperhour.com/freelance-jobs/technology-programming/programming-coding/i-need-a-weather-python-program-coded-3729938
import os
import threading
import time
from server import app

def executeServer():
    #runs app 
    app.run(port=8000, debug=True, use_reloader=False, threaded=True, host="127.0.0.1")

def executeClient():
    #wait for server to start
    print("Waiting for server to start")
    time.sleep(5)
    os.system("start http://127.0.0.1:8000")

threading.Thread(target=executeClient).start()
threading.Thread(target=executeServer).start()

#exit with q
print ("Press q to exit all threads")
while True:
    time.sleep(1)
    if input() == "q":
        os._exit(0)



#q: how to distribute this code on a docker container?
#a: https://www.youtube.com/watch?v=Q5POuMHxW-0