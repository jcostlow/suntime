#!/usr/bin/env python3
'''
Print the time of your favorite elevation of the sun.
'''

import argparse
import datetime
import pytz
import astral
import astral.sun
import ics

def main():
    args = parse_arguments()
    a = astral.Observer(latitude= args.latlong[0], longitude = args.latlong[1], elevation= args.altitude)
    thisday = datetime.datetime(args.year,args.month, args.day)
    lastday = thisday + datetime.timedelta(days = args.numdays)
    if args.icsfile:
        c=ics.Calendar()
    while thisday < lastday:
        suntime = astral.sun.time_at_elevation(a, date=thisday,
            elevation=args.elevation, tzinfo=args.timezone)
        print (suntime)
        thisday = thisday + datetime.timedelta(days=1)
        if args.icsfile:
            e=ics.event.Event(name='Sun time', begin = suntime, duration= {'minutes':10} )
            c.events.add(e)
    if args.icsfile:
        args.icsfile.write(str(c))



def parse_arguments():
    '''Parse arguments to print times when the sun is at your favorite elevation'''

    parser = argparse.ArgumentParser(
        description='Print times when the sun is at your favorite elevation.'
    )

    locationgroup = parser.add_mutually_exclusive_group(required=True)
    locationgroup.add_argument(
        '--city', action='store', help='Specify a city. TODO DOES NOT WORK YET'
    )
    locationgroup.add_argument(
        '--latlong', nargs=2, action='store', type=float, help='Latitude longitude', metavar=('Latitude', 'Longitude')
    )
    parser.add_argument(
        '--altitude', help='Altitude in meters at the location', default = 2
    )
    parser.add_argument(
        '--timezone', help='Local timezone', type=lambda tz: pytz.timezone(tz), default=pytz.timezone('US/Pacific')
    )
    parser.add_argument(
        '--year', '-y', help='Year', type=int, default=datetime.datetime.now().year
    )
    parser.add_argument(
        '--month', '-m', help='Month', type=int, default=datetime.datetime.now().month
    )
    parser.add_argument(
        '--day', help='Day', type=int, default=datetime.datetime.now().day
    )
    parser.add_argument(
        '--numdays', help='Number of Days to write', type=int, default=1
    )
    parser.add_argument(
        '--elevation', type=float, help='Elevation on the sun in degrees, dawn=0, dusk=180', default=174
    )
    parser.add_argument('--icsfile', type=argparse.FileType('w') )

    return parser.parse_args()


if __name__ == '__main__':
    main()
