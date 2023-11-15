import sys
input = sys.stdin.readline

h = int(input())
m = int(input())


def num_to_string(num):
    twenty_string = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens_place = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty']
    if num < 20:
        return twenty_string[num]
    elif num >= 20:
        tens, ones = divmod(num, 10)
        if ones:
            return tens_place[tens] + ' ' + twenty_string[ones]
        else:
            return tens_place[tens]


string = ""
hour = num_to_string(h)
if m == 0:
    string = "{} o' clock".format(hour)
elif 1 <= m <= 30:
    minute = num_to_string(m)
    if m == 1:
        string = "{} minute past {}".format(minute, hour)
    elif m == 15:
        string = "quarter past {}".format(hour)
    elif m == 30:
        string = "half past {}".format(hour)
    else:
        string = "{} minutes past {}".format(minute, hour)
elif 30 < m:
    m = 60 - m
    if h == 12:
        hour = "one"
    else:
        hour = num_to_string(h + 1)
    minute = num_to_string(m)
    if m == 1:
        string = "{} minute to {}".format(minute, hour)
    elif m == 15:
        string = "quarter to {}".format(hour)
    else:
        string = "{} minutes to {}".format(minute, hour)
print(string)
