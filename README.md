# cruzzed-apu-timetable-cli
Asia Pacific University Timetable Command Line Interface v1.0
Depends: 'requests' or 'pip install requests'

Usage: .\\timetable.py /arg value /arg value /arg value ...

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

Output:  

        ~~~     CT015-3-2-DMTD-T-2      ~~~
        Intake: UC2F1908SE
        Lecture Name: CENSORED
        Module Code: CT015-3-2-DMTD-T-2
        Day and Date: FRI 01-MAY-20
        Time Start and Finish: 09:30 AM-10:30 AM
        Location: NEW CAMPUS
