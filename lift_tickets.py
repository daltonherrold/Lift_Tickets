import argparse
from time import sleep
from requests_html import HTMLSession
from datetime import datetime, timedelta
from getpass import getpass

from resorts import resorts, pretty_name
from message import send_email, send_text
from util import validate_args


parser = argparse.ArgumentParser(prog='lift_tickets.py', usage='%(prog)s [options] mountain date',
                                 description='Getting you sold out lift tickets.')

# Positional arguments
parser.add_argument('mountain', metavar='mountain', type=str,
                    help='The mountain you want to ski at. List avaliabe here _____.')
parser.add_argument('date', metavar='date', type=str,
                    help='Date in the format MM/DD/YYYY.')

# Optional Arguments
parser.add_argument('-e', '--email', metavar='email', type=str,
                    help='Emails the given email when tickets are avaliable.')
parser.add_argument('-p', '--phone', metavar='phone', type=str,
                    help='Texts the given phone when tickets are avaliable. Enter #########, no dashes.')
parser.add_argument('-c', '--carrier', metavar='carrier', type=str,
                    help=('Specifies the carrier of the phone. Necessary when using phone option. '
                          'Options are att, tmobile, verizon, or sprint.'))
parser.add_argument('-t', '--timeout', metavar='timeout', type=int, default=120,
                    help=('Timeout for email and text in seconds. Defult is 2 minutes (120 seconds).'))
parser.add_argument('-q', '--quiet', action='store_true',
                    help='Decreses the amount of output.')

args = parser.parse_args()

if not validate_args(args):
    print('Please enter a valid input. You can use -h to see all inputs.')
    exit(1)

date = args.date.split("/")
mountain = args.mountain
name = pretty_name[resorts.index(args.mountain)]
last_email = datetime.now() - timedelta(seconds=args.timeout)
last_text = datetime.now() - timedelta(seconds=args.timeout)

if args.email or args.phone:
    print()
    print('You need to enter your credentials for email/texting.')
    print('NOTE: You may need to enable less secure apps on gmail if it does not work')
    auth = (input("Email: "), getpass())

print()
print('#####################################')
print('mountain: {}'.format(name))
print('date: {}'.format(args.date))
print('email: {}'.format(args.email))
print('phone: {}'.format(args.phone))
print('carrier: {}'.format(args.carrier))
print('timeout: {} seconds'.format(args.timeout))
print('quiet: {}'.format(args.quiet))
print('#####################################')
print()

url = 'https://www.{}.com/plan-your-trip/lift-access/tickets.aspx?startDate={}&numberOfDays=1&ageGroup=Adult'.format(
      mountain, '%2F'.join(date))

session = HTMLSession()

while True:
    r = session.get(url)
    r.html.render(sleep=5)

    if 'Day Ticket' in r.html.text:
        message = 'Tickets for {} are avaliable on {}'.format(name, args.date)
        subject = '{} Tickets'.format(name)
        print('{} - {}'.format(datetime.now(), message))
        if args.email and datetime.now() - last_email > timedelta(seconds=args.timeout):
            last_email = datetime.now()
            send_email(auth, message, subject, args.email)
        if args.phone and datetime.now() - last_text > timedelta(seconds=args.timeout):
            last_text = datetime.now()
            send_text(auth, message, subject, args.phone, args.carrier)
    else:
        if not args.quiet:
            print('{} - Not avaliable'.format(datetime.now()))

    sleep(10)
