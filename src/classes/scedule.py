import schedule
import time
import threading

def schedule_loop(function_to_do: callable):
    schedule.every().hour.do(function_to_do)

    while True:
        schedule.run_pending()
        time.sleep(60)

def schedule_as_thread(function_to_do: callable):
    # TODO check if it works
    thread = threading.Thread(target=schedule_loop, args=(function_to_do,), daemon=True)
    thread.start()