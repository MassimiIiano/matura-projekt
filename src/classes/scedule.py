import schedule
import time
import threading

def repeat_function(func: callable, timeout: int = 60, exe: bool = True):
    # ensure that the function is called every minute
    def wrapper():
        while True:
            func()
            time.sleep(timeout)

    # execute the function once
    if exe:
        func()
    
    # creates and starts a daemon thread
    t = threading.Thread(
        target=wrapper, 
        daemon=True
    )

    t.start()
