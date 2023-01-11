import schedule
import time
import threading

def schedule_loop(time_of_day, function_to_do):
    schedule.every().day.at(time_of_day).do(function_to_do)

    while True:
        schedule.run_pending()
        time.sleep(60)

def schedule_as_thread(function_to_do):
    thread = threading.Thread(target=schedule_loop, args=(function_to_do,), daemon=True)
    thread.start()