from datetime import timedelta, datetime

def hours_minutes_seconds(time:timedelta):
    return time.seconds // 3600, (time.seconds // 60) % 60, time.seconds % 60

def o_timespan(time_str:str):
    tt, tf = time_str[:-1], time_str[-1]
    format = tt.isdigit() and tf.isalpha()
    if time_str.isdigit() or tf == "m" and format:
        return timedelta(minutes=int(time_str))
    elif ":" in time_str:
        h, m = time_str.split(":")
        h, m = int(h), int(m)
        n = datetime.now()
        t = n.replace(hour=h, minute=m)
        if t < n:
            t = t.replace(day=t.day+1)
        return t - datetime.now()
    elif tf == "s" and format:
        return timedelta(seconds=int(tt))
    elif tf == "h" and format:
        return timedelta(hours=int(tt))
    elif tf == "d" and format:
        return timedelta(days=int(tt))
    else:
        raise Exception("Unable to parse time argument")