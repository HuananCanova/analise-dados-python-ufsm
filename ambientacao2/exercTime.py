def calcGameTIme(startHour, startMinute, endHour, endMinute):
    if (((startHour > 0 and startHour <= 24) and (startMinute >= 0 and startMinute < 60)) and (
            (endHour > 0 and endHour <= 24) and (endMinute >= 0 and endMinute < 60))):
        print((endHour - startHour), ":", (endMinute - startMinute), " total time game")
    else:
        return 0



startHour = int(input("Inform the START HOUR of the game: "))
startMinute = int(input("Inform the START MINUTE of the game: "))
endHour = int(input("Inform the END HOUR: "))
endMinute = int(input("Inform the END MINUTES: "))
calcGameTIme(startHour, startMinute, endHour, endMinute)