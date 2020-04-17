import requests
import sys

#this functions returns 
#a dictionary of arguments
#provided by user
#when opened from command line
#or when using the interactive console

def sysargs(sysargv, argsdictionary):
    sysarg = [sys.upper() for sys in sysargv]
    if sysarg[0] == '/?' or sysarg[0] == '/help':
        help()
        exit()
    else:
        print(sysarg)
        argsdict = {}
        for b in range(len(argsdictionary[0])):
            if (argsdictionary[0][b] in sysarg):
                argsdict[str(argsdictionary[1][b])] = sysarg[sysarg.index(argsdictionary[0][b])+1]
    return argsdict

def argsdictionary():
   return list([["/IN","/MOD","/LEC","/DAY","/DATE","/ST","/ET","/LOC"],["INTAKE","MODID","NAME","DAY","DATESTAMP","TIME_FROM","TIME_TO","LOCATION"]])

#main function
#if no arguments provided, it will be an interactive console.

def main():
    if (len(sys.argv)) < 2: 
        try:
            help()
            print("Enter commands without 'timetable.py'.")
            print("Press Ctrl+C to exit.")
            while(True):
                arguments = input(">>>\t")
                arguments = arguments.split(" ")
                print(arguments)
                parsing(sysargs(arguments,argsdictionary()))
        except:
            print("Error, Program exiting...")
            exit()
    else:
        parsing(sysargs(sys.argv[1:], argsdictionary()))
        exit()

#API Parser function
def parsing(argsdict):
    #api URL
    URL = "https://s3-ap-southeast-1.amazonaws.com/open-ws/weektimetable"
    #open URL
    data = requests.get(URL).json()
    return search(data, argsdict) #continues to search phase which takes API data and system arguments

#Search function based on flags,
#it will only take schedules
#that perfectly matches
#the arguments and value given
def search(schedules, argsdict):
    listofschedule = []
    for scheduledict in schedules:
        flag = int(0)
        for a,b in argsdict.items():
            for x,y in scheduledict.items():
                if (a == x):
                    if b in y:
                        flag = flag+1
                        if (flag == len(argsdict)):
                            listofschedule.append(scheduledict)
                        break
                    else:
                        break
    return formatter(listofschedule) #continues to format the values phase

#format and print function
def formatter(list):
    for v in list:
        print("~~~\t",v["MODID"],"\t~~~")
        print("Intake:",v["INTAKE"])
        print("Lecture Name:",v["NAME"])
        print("Module Code:",v["MODID"])
        print("Day and Date:",v["DAY"],v["DATESTAMP"])
        print("Time Start and Finish:",v["TIME_FROM"]+"-"+v["TIME_TO"])
        print("Location:",v["LOCATION"])

#help page function
#will be called upon
#no arguments provided or
#arguments such as /? or /help provided

def help():
    print('''
Asia Pacific University Timetable Command Line Interface v1.0
Usage: .\\timetable.py /arg value /arg value /arg value

        /? or /help: Show help page and exits.
        /in: Used to search a schedule based on the intake.
        /loc:                    ...                location.
        /lec:                    ...                lecturer name.
        /mod:                    ...                module code.
        /day:                    ...                day.
        /date:                   ...                date.
        /start:                  ...                start time.
        /end:                    ...                end time.

Example: timetable.py /in UC2F1908SE /mod dmtd /date 01
Output:  ~~~      CT015-3-2-DMTD-T-2     ~~~
        Intake: UC2F1908SE
        Lecture Name: CENSORED
        Module Code: CT015-3-2-DMTD-T-2
        Day and Date: FRI 01-MAY-20
        Time Start and Finish: 09:30 AM-10:30 AM
        Location: NEW CAMPUS
        ''')

if __name__ == '__main__':
    main()
