import datetime

def main():
    print("welcome to the alarm clock")
    userInput = input("Please enter current hour in HH format or type now to use the current time ")
    nowtime = datetime.datetime.now()
    if userInput.lower().strip() != "now":
        try:
            numHour = int(userInput)
            if numHour < 0 or numHour > 23:
                raise ValueError
        except Exception as e:
            print("Please enter a valid hour")
            return
    hoursUntilAlarm = input("Please enter the number of hours until the alarm goes off ")
    try:
        numHours = int(hoursUntilAlarm)
        if numHours < 0:
            raise ValueError
    except Exception as e:
        print("Please enter a valid number of hours")
        return

    timeAlarmWillGoOff = nowtime + datetime.timedelta(hours=numHours)
    print("The alarm will go off at: ", timeAlarmWillGoOff.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()



