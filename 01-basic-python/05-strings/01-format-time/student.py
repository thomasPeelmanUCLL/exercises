# Write your code here
def format_time(hours, minutes, seconds):
    hours = str(hours).rjust(2, '0')
    minutes = str(minutes).rjust(2, '0')
    seconds = str(seconds).rjust(2, '0')

    return "{}:{}:{}".format(hours, minutes, seconds)