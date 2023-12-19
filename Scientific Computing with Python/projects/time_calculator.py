data = ("3:00 PM", "3:10")

def add_time(start, duration):
    # Split the start time into hours, minutes
    time_start, am_pm = start.split()
    [hours, mins] = [int(i) for i in time_start.split(":")]
    if "PM" in am_pm:
        hours += 12
    else:
        hours += 0
    # Split the duration into hours and minutes
    [hd, md] = [int(i) for i in duration.split(":")]

    # Add the minutes
    if mins + md >= 60:
        hours += 1
        mins = (mins + md) - 60
    else:
        mins += md
    
    # Add the hours
    hours += hd
    
    # Convert to 12 hour clock
    if hours > 12:
        hours -= 12
        am_pm = "PM"
    else:
        am_pm = "AM"

    
    new_time = f"{hours}:{mins} {am_pm}"



    return new_time

print(add_time(data[0], data[1]))
