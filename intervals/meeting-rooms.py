#Given an array of meeting time intervals consisting of start and end times
#[#s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def canAttendMeetings(arr):
    arr.sort(key=lambda a: a.start)
    
    for i in range(len(arr)-1):
        if arr[i].end > arr[i+1].start:
            return False

    return True


arr = []
arr.append(Interval(0,30))
arr.append(Interval(5,10))
arr.append(Interval(15,20))

print(canAttendMeetings(arr))
