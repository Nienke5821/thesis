from gtts import gTTS
from playsound import playsound
import os
import openai
import time
from mutagen.mp3 import MP3

openai.api_key = ""  # TODO: insert your own API key
model_engine = "gpt-3.5-turbo"


def play_message(message):
    """Says the message out loud

    Args:
        message (str): The message that has to be said out loud 
    """
    speaker = gTTS(text=message, lang="nl")
    speaker.save("notificatie.mp3")
    playsound("notificatie.mp3")
    os.remove("notificatie.mp3")


def say_nr_notifications(nr):
    """Says how many notifications there are

    Args:
        nr (int): The number of notifications that are given to the user
    """
    if nr == 1:
        text = "Er is 1 nieuwe melding"
    elif nr == 2:
        text = "Er zijn 2 nieuwe meldingen"
    elif nr == 3:
        text = "Er zijn 3 nieuwe meldingen"
    play_message(text)
    time.sleep(1)


def say_notification(notification):
    """Says the message of the notification out loud

    Args:
        notification (NotificationClass): the notfication of which the message has to be said out loud
    """
    play_message(getattr(notification, "message"))


def generate_combination(notifications):
    """Combines multiple notification messages into one message

    Args:
        notifications (list): the notifications of which the messages have to be combined

    Returns:
        str: the message in which all seperate messages have been combined
    """
    content = ""
    messages = []
    for notification in notifications:
        messages.append(getattr(notification, "message"))
    for message in messages:
        content += "\""
        content += message
        content += "\", "
    content = content[:-2]
    message_chatgpt = "please combine the following notifications into a coherent Dutch message that sounds like it is told by a human: " + content
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assitant."},
            {"role": "user", "content": message_chatgpt}
        ]
    )
    return response.choices[0]["message"]["content"]


def say_combination(notifications):
    """Says a message that consists out of multiple messages out loud

    Args:
        notifications (list): the notifications of which the messages have to be combined
    """
    speaker = gTTS(text=generate_combination(notifications), lang="nl")
    speaker.save("notificatie.mp3")
    playsound("notificatie.mp3")
    os.remove("notificatie.mp3")


def tell_message(give_user, show_type):
    """Says the correct message out loud according to the method that is used to convey the message

    Args:
        give_user (list): the notifications that have to be conveyed to the user
        show_type (str): the method that is used to convey the messages to the user
    """
    if show_type == "screen":
        say_nr_notifications(len(give_user))
    elif show_type == "talking":
        ordered = [[], [], []]
        for notification in give_user:
            ordered[getattr(notification, "urgency") - 1].append(notification)
        new_give_user = []
        for list in ordered:
            for item in list:
                new_give_user.append(item)
        # ordered.fl
        say_combination(new_give_user)
    else:  # original
        say_notification(give_user[0])
