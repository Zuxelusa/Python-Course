import time
def log_add_note(event, description = "none"):
    with open("log.txt", "a", encoding="utf-8") as log:
        line = f"{time.strftime('%d-%m-%Y %H:%M:%S')}\t{event}\n"
        log.write(line)