"""
Slack chat-bot Lambda handler.
"""

import os
import logging
import urllib
from botocore.vendored import requests
# Grab the Bot OAuth token from the environment.
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Define the URL of the targeted Slack API resource.
# We'll send our replies there.
SLACK_URL = "https://slack.com/api/chat.postMessage"


def lambda_handler(data, context):
    """Handle an incoming HTTP request from a Slack chat-bot.
    """
    if "challenge" in data:
        return data["challenge"]
    # Grab the Slack event data.
    slack_event = data['event']
    
    # We need to discriminate between events generated by 
    # the users, which we want to process and handle, 
    # and those generated by the bot.
    if "bot_id" in slack_event:
        logging.warn("Ignore bot event")
    else:
        # Get the text of the message the user sent to the bot,
        # and reverse it.
        text = slack_event["text"]
        
        headers = {
            'Content-Type': 'application/json',
        }

        postidata = "{\"hakusana\":\"" + text + "\",\"source\":\"larepro999@gmail.com\",\"destination\":\"larepro999@gmail.com\"}"

        response = requests.post('https://him63n2rxk.execute-api.eu-west-1.amazonaws.com/dev/send-email', headers=headers, data=postidata)

        
        reversed_text = response.text
        
        
        
        # Get the ID of the channel where the message was posted.
        channel_id = slack_event["channel"]
        
        # We need to send back three pieces of information:
        #     1. The reversed text (text)
        #     2. The channel id of the private, direct chat (channel)
        #     3. The OAuth token required to communicate with 
        #        the API (token)
        # Then, create an associative array and URL-encode it, 
        # since the Slack API doesn't not handle JSON (bummer).
        data = urllib.parse.urlencode(
            (
                ("token", BOT_TOKEN),
                ("channel", channel_id),
                ("text", reversed_text)
            )
        )
        data = data.encode("ascii")
        
        # Construct the HTTP request that will be sent to the Slack API.
        request = urllib.request.Request(
            SLACK_URL, 
            data=data, 
            method="POST"
        )
        # Add a header mentioning that the text is URL-encoded.
        request.add_header(
            "Content-Type", 
            "application/x-www-form-urlencoded"
        )
        
        # Fire off the request!
        urllib.request.urlopen(request).read()

    # Everything went fine.
    return "200 OK"