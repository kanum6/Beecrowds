sec = int(input())
hour = 0
mins = 0
sec2 = 0

while sec != 0:
    if sec >= 3600:
        sec -= 3600
        hour += 1

    if sec >= 60 and sec < 3600:
        sec -= 60
        mins += 1

    else:
        sec -= 1
        sec2 += 1

print (f"{hour}:{mins}:{sec2}")