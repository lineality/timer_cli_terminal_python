import time

count = 0
MARS_TO_EARTH = 1.02749125104

def timer():
    global count 
    while True:
        earth_tenths = count
        earth_secs, earth_tenths = divmod(earth_tenths, 10)
        earth_mins, earth_secs = divmod(earth_secs, 60)
        
        mars_tenths = count * MARS_TO_EARTH
        mars_secs, mars_tenths = divmod(mars_tenths, 10)
        mars_mins, mars_secs = divmod(mars_secs, 60)
        
        print("\rEarth Time: {} min {:.1f} sec  |  Mars Time: {} min {:.1f} sec".format(int(earth_mins), earth_secs + earth_tenths / 10, int(mars_mins), mars_secs + mars_tenths / 10), end="")
        time.sleep(0.1)  # Sleep for a tenth of a second
        count += 1

try:
    timer()
except KeyboardInterrupt:
    total_mars_tenths = count * MARS_TO_EARTH
    total_mars_secs = total_mars_tenths // 10
    total_mars_mins = total_mars_secs // 60
    
    print(f"\nEarth Time Total: {count//600} min {count%600/10:.1f} sec, Mars Time Total: {total_mars_mins:.0f} min {total_mars_secs%60 + total_mars_tenths%10 / 10:.1f} sec")

