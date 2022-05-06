from datetime import timezone, timedelta

# TELEGRAM BOT
TIMEZONE = timezone(timedelta(hours=8)) # UTC+8
BOT_TOKEN_FILE = 'keys/bot_token.txt'
BOT_COMMANDS = (
    'Interact with me using these commands:\n\n'
    '*Manage Facility Bookings*\n'
    '/book - Book facilities in 5 SIR\n'
    '/change - Change or cancel a booking\n'
    '/check - Check facility availability\n'
    '/list - List your upcoming bookings\n\n'
    '*Bot Settings*\n'
    '/profile - Update your user profile\n'
    '/help - Show this list of commands'
)


# GOOGLE CALENDAR API
SERVICE_ACCOUNT_SCOPES = ['https://www.googleapis.com/auth/calendar.events']
SERVICE_ACCOUNT_FILE = 'keys/service_account.json'
CALENDAR_ID = 'begpgae3aecell7h163qoek9l0@group.calendar.google.com'
EVENT_COLOUR_CODES = {
    'LT 1': '1',
    'LT 2': '7',
    'CONF ROOM': '2',
    'RTS': '5',
    'STINGRAY SQ': '6'
}
'''
GOOGLE CALENDAR API 
EVENT COLOR IDs:

ID | Name      | Hex Code
==========================
1  | Lavender  | #7886cb
2  | Sage      | #33b679
3  | Grape     | #8e24aa
4  | Flamingo  | #e67c73
5  | Banana    | #f6c026
6  | Tangerine | #f5511d
7  | Peacock   | #039be5
8  | Graphite  | #616161
9  | Blueberry | #3f51b5
10 | Basil     | #0b8043
11 | Tomato    | #d60000
'''

# DATABASE
USER_DB_NAME = 'data/users.db'