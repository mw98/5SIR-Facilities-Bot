from datetime import datetime
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from utilities import calendar, actions

'''
MYBOOKINGS CALLBACK FUNCTION
'''
@actions.send_typing_action
@actions.load_user_profile
def show_upcoming_user_bookings(update: Update, context: CallbackContext) -> None:
    
    bookings = calendar.find_upcoming_bookings_by_user(update.message.from_user.id)
    
    message = "Ok, here are your bookings:\n"
    
    if bookings['ongoing']:
        message += "\n*Ongoing*\n"
        for booking in bookings['ongoing']:
            booking_details = booking['extendedProperties']['shared']
            message += (
                f"[{booking_details['start_time']}-{booking_details['end_time']}]({booking['htmlLink']}) {booking_details['facility']}\n"
            )
    
    if bookings['later_today']:
        message += "\n*Later Today*\n"
        for booking in bookings['later_today']:
            booking_details = booking['extendedProperties']['shared']
            message += (
                f"[{booking_details['start_time']}-{booking_details['end_time']}]({booking['htmlLink']}) {booking_details['facility']}\n"
            )
    
    if bookings['after_today']:
        date = None
        for booking in bookings['after_today']:
            booking_details = booking['extendedProperties']['shared']
            booking_date = booking_details['date']
            if booking_date != date:
                date = booking_date
                message += f"\n*{datetime.strptime(booking_date, '%Y-%m-%d').strftime('%d %b %Y')}*\n"
            message += (
                f"[{booking_details['start_time']}-{booking_details['end_time']}]({booking['htmlLink']}) {booking_details['facility']}\n"
            )
    
    else:
        message = "You don't have any ongoing or upcoming bookings."
    
    update.effective_chat.send_message(
        text = message,
        parse_mode = ParseMode.MARKDOWN
    )
    
    return


'''
MYBOOKINGS HANDLER
'''
handler = CommandHandler('mybookings', show_upcoming_user_bookings)