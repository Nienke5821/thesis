import datetime


def create_time(hours, minutes):
    """Creates from hours and minutes a time

    Args:
        hours (datetime.datetime): the hour of the time
        minutes (datetime.datetime): the minutes of the time

    Returns:
        datetime.datetime: the final time
    """
    now = datetime.datetime.now()
    new_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    return new_time


class NotificationClass():
    """Represents the notifications that are given to the user
    """

    def __init__(self, dictionary):
        """Initializes the NotificationClass

        Args:
            dictionary (dict): dictionary that contains all attributes of the notification
        """
        for key, value in dictionary.items():
            setattr(self, key, value)


def create_notification(min_hours, min_minutes, max_hours, max_minutes, urgency, category, notification, show_type):
    """Creates a new notification

    Args:
        min_hours (datetime.datetime): the minimal hour at which the notification can be given
        min_minutes (datetime.datetime): the minimal minutes at which the notification can be given
        max_hours (datetime.datetime): the maximimum hour at which the notification can be given
        max_minutes (datetime.datetime): the maximum minutes at which the notification can be given
        urgency (int): the urgency level of the notification
        category (str): the category of the notification message
        notification (str): the message of the notification
        show_type (str): the method that is used to convey the notification to the user

    Returns:
        NotificationClass: a notification that has the arguments of the function as attributes
    """
    if min_hours == None:  # no time frame
        min_time = None
        max_time = None
    else:
        min_time = create_time(min_hours, min_minutes)
        max_time = create_time(max_hours, max_minutes)
    dictionary = {'min_time': min_time, 'max_time': max_time,
                  'show_type': show_type, 'urgency': urgency,
                  'category': category, 'message': notification
                  }
    new_notification = NotificationClass(dictionary)
    return new_notification
