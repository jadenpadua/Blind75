def meetingScheduler(slots1, slots2, duration):

    slots1.sort(key=lambda a: a[0])
    slots2.sort(key=lambda a: a[0])s

    a = 0
    b = 0


    while True:
        lastStart = max(slots1[a][0], slots2[b][0])
        firstEnd = min(slots1[a][1], slots2[b][1])

        if firstEnd - lastStart >= duration:
            return [lastStart, lastStart + duration]
        
        else:
            if slots1[a][1] == firstEnd:
                a += 1 
            
            else:
                b += 1

            if a == len(slots1) or b == len(slots2):
                break
    
    return []

print(meetingScheduler([[10,50] , [60,120], [140,210]], [[0,15], [60,70]], 8))
