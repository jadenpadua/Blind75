def minConferenceRooms(intervals):
    start = [0] * len(intervals)
    end = [0] * len(intervals)

    for i in range(len(intervals)):
        start[i] = intervals[i][0]
        end[i] = intervals[i][1]

    start.sort()
    end.sort()

    end_index = 0
    minRooms = 0
    for i in range(len(intervals)):
        if start[i] < end[end_index]:
            minRooms += 1
        else:
            end_index += 1

    return minRooms


print(minConferenceRooms([[2,15], [36,45], [9,29], [16,23], [4,9]]))
