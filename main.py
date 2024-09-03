# I will give reasons for each line of code btw

import discord  # For getting the webhook object
import requests  # For deleting the webhook and sending the requests
from discord import SyncWebhook  # Allows you to send webhook messages
import keyboard  # Detects key presses for select menus
import time  # for waiting in case of ratelimits
import sys  # sys for exiting

status_codes = {  # define status codes
    404: 'Webhook does not exist or could not be found.',
    400: 'Bad Request',
    401: 'Unauthorized',
    408: 'Request Timeout',
    429: 'URL Had Too Many Requests',
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    508: 'Loop Detected'
}

# CLI writing time!
print("Webhook Tools 1.0")  # prints name and version
print("Options to select in questions are in square brackets.")  # its a print again

link = input("Please enter the webhook link. ")
if link == "":
    sys.exit()

option = input("Would you like to: [Spam] the webhook, [delete] it, or send a [fake] message impersonating Discord? ").lower()  # asks for input
if option == "":
    sys.exit()

def spam(webhook, message):
    r = requests.post(
        link,
        json={"content": message}
    )

    if r.status_code == 204:
        print("Sent!")
    elif r.status_code == 429:
        print("Rate limited!")
        return 429
    else:
        print("Error: Status Code ", r.status_code)
        for key, value in status_codes.items():
            if int(key) == int(r.status_code):
                print("Error: ", value)
                input("Press any key to exit.")
                sys.exit()

def fake(webhook):
    message = """
    @everyone

    **Hi**,

    We've noticed some suspicious activity on this webhook and we've decided to let you know.

    Our systems have detected an excessive amount of everyone pings sent on this webhook and to protect this community we may have to take further action to delete the webhook.

    We apologise for any inconvenience caused by this. Sorry!"""

    webhook.send(message, username="Discοrd", avatar_url="https://cdn.discordapp.com/avatars/643945264868098049/c6a249645d46209f337279cd2ca998c7")

# honestly just read the prints from here
if option == "delete":
    r = requests.delete(link)  # deletes the webhook
    if r.status_code == requests.codes.no_content:
        print("Successfully deleted the webhook!")
    else:
        print('Failed to delete the webhook with status code: ', r.status_code)
        print("Please try again later.")
elif option == "spam":
    webhook = SyncWebhook.from_url(link)  # defines webhook object
    message = input("What is the message you would like to spam the webhook with (default @everyone) ")
    if message == "":
        message = "@everyone"
    iterations = input("How many times would you like to spam the webhook? (default 10) ")
    if iterations == "":
        iterations = 10
    else:
        iterations = int(iterations)

    for i in range(iterations):
        spama = spam(webhook, message)
        if spama == 429:
            time.sleep(5.5)  # so we wait to not be rate limited

    time.sleep(5)
elif option == "fake":
    webhook = SyncWebhook.from_url(link)
    fake(webhook)










