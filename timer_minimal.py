import time

sec = 0

def timer():
    global sec 
    while True:
        mins, secs = divmod(sec, 60)
        print("\rTime elapsed: {} minutes {} seconds".format(mins, secs), end="")
        time.sleep(1)
        sec += 1

try:
    timer()
except KeyboardInterrupt:
    print(f"\nTimer stopped, total time: {sec//60} minutes {sec%60} seconds")
