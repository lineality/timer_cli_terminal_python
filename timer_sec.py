import time

sec = 0
MARS_TO_EARTH = 1.02749125104

def timer():
    global sec 
    while True:
        earth_mins, earth_secs = divmod(sec, 60)
        mars_sec = sec * MARS_TO_EARTH
        mars_mins, mars_secs = divmod(mars_sec, 60)
        mars_hours, mars_mins = divmod(mars_mins, 60)
        print("\rEarth time elapsed: {} min {} sec | Mars time elapsed: {} min {} sec".format(earth_mins, int(earth_secs), int(mars_mins), int(mars_secs)), end="")
        time.sleep(1)
        sec += 1

try:
    timer()
except KeyboardInterrupt:
    total_mars_sec = sec * MARS_TO_EARTH
    total_mars_mins = total_mars_sec // 60
    total_mars_hours = total_mars_mins // 60
    print(f"\nTimer stopped, Earth total time: {sec//60} min {sec%60} sec, Mars total time: {total_mars_mins%60:.0f} min {total_mars_sec%60:.0f} sec")

