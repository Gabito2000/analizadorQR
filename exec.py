
import os
import threading
import time
#opens the url in the default browser

def executeServer():
    os.system("python -m uvicorn main:app --reload")

def executeClient():
    #wait for server to start
    print("Waiting for server to start")
    time.sleep(5)
    os.system("start http://127.0.0.1:8000")


threading.Thread(target=executeClient, args=()).start()

executeServer()