# suntime

I have a favorite time of day when the sun illuminates the area around my house.

I created this program to build me a calendar file when the sun is at my favorite position.

# Usage:

    % ~/bin/suntime.py --latlong 47.608013 -122.335167  --altitude 20 --timezone US/Pacific --elevation 174
    2021-01-24 16:12:54.832778-08:00

By default, the script will print only today.

If you want to get the time for multiple days, add the `--numdays` option.

    % ~/bin/suntime.py --latlong 47.608013 -122.335167  --altitude 20 --timezone US/Pacific --elevation 174 --numdays 3
    2021-01-24 16:12:54.832778-08:00
    2021-01-25 16:14:38.547388-08:00

If you want to export an ICS file with calendary entries, use the `--icsfile` option with a filename. You can then import the ICS file into the calendar of your choice.