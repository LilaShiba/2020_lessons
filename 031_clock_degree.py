'''
This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree,
 the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

'''

def clock_degree(time):
    hh,mm = int(time[:2]), int(time[3:5])


    times = {h*5:h for h in range(12)}
    times[0] = 12
    mins_to_hours = times[mm]
    ans = abs(hh - mins_to_hours)
    angle = ans * 30
    # 360 / 60 = 6 degrees
    # 360 / 60 = 6 degrees.
    return angle

def angle(hour, minute):
    h = 30 * hour
    m = 6 * minute

    return abs(h - m)

print(angle(12,45))
print(clock_degree('12:45'))
