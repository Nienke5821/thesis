import datetime
import time


def check_notifications_list(notifications, can_be_given, give_now):
    """Checks which notifications have to be given and which can be given

    Args:
        notifications (list): notifications that are not categorized yet
        can_be_given (list): notifications that can be given
        give_now (list): notifications that must be given now

    Returns:
        (list, list, list): the updated lists of notifications that are not categorized, notifications that can be given,
                            and notifications that must be given now
    """
    to_be_removed = []
    while datetime.datetime.now().second >= 30:
        time.sleep(5)
    for notification in notifications:
        updated = check_notification_type(
            notification, can_be_given, give_now, to_be_removed)
        can_be_given = updated[0]
        give_now = updated[1]
        to_be_removed = updated[2]

    for notification in to_be_removed:
        notifications.remove(notification)
    to_be_removed = []

    return notifications, can_be_given, give_now


def check_can_be_given(can_be_given, give_now):
    """Checks whether notifications that can be given have to be given now

    Args:
        can_be_given (list): notifications that can be given
        give_now (list): notifications that must be given now

    Returns:
        (list, list): the updated lists of notifications that can be given and notifications that must be given now
    """
    to_be_removed = []
    while datetime.datetime.now().second >= 30:
        time.sleep(5)
    now = datetime.datetime.now()
    for notification in can_be_given:
        max_time = getattr(notification, "max_time")
        time_diff = max_time - now
        time_diff_minutes = time_diff.total_seconds() / 60
        if time_diff_minutes <= 5:
            give_now.append(notification)
            to_be_removed.append(notification)
    for notification in to_be_removed:
        can_be_given.remove(notification)
    return can_be_given, give_now


def check_notification_type(notification, can_be_given, give_now, to_be_removed):
    """Check the time frame of the notification and categorize it accordingly

    Args:
        notification (NotificationClass): the notification that has to be checked
        can_be_given (list): notifications that can be given
        give_now (list): notifications that have to be given now
        to_be_removed (list): notifications that have been categorized

    Returns:
        (list, list, list): the updated lists of notifications that can be given, notifications that must be given now,
                            and notifications that have been categorized
    """
    min_time = getattr(notification, "min_time")
    if min_time == None:  # no time frame
        can_be_given.append(notification)
        to_be_removed.append(notification)

    elif min_time == getattr(notification, "max_time"):  # specific time
        updated = check_specific_time(
            notification, give_now, min_time, to_be_removed)
        give_now = updated[0]
        to_be_removed = updated[1]

    else:  # time frame
        updated = check_time_frame(
            notification, can_be_given, give_now, min_time, to_be_removed)
        can_be_given = updated[0]
        give_now = updated[1]
        to_be_removed = updated[2]
    return can_be_given, give_now, to_be_removed


def check_specific_time(notification, give_now, min_time, to_be_removed):
    """Categorizes a notification that has to be given at a specific time

    Args:
        notification (NotificationClass): the notification that has to be categorized
        give_now (list): notifications that have to be given now
        min_time (time): the time at which the notification has to be given
        to_be_removed (list): notifications that have been categorized

    Returns:
        (list, list): the updated lists of notifications that must be given now
                        and notifications that have been categorized
    """
    now = datetime.datetime.now().replace(
        second=0, microsecond=0)
    if min_time <= now:
        give_now.append(notification)
        to_be_removed.append(notification)
    return give_now, to_be_removed


def check_time_frame(notification, can_be_given, give_now, min_time, to_be_removed):
    """Categorizes a notification that has to be given within a timeframe

    Args:
        notification (NotificationClass): the notification that has to be categorizedd
        can_be_given (list): notifications that can be given
        give_now (list): notifications that have to be given now
        min_time (time): the time from which point on the notification can be given
        to_be_removed (list): notifications that have been categorized

    Returns:
        (list, list, list): the updated lists of notifications that can be given, notifications that must be given now
                        and notifications that have been categorized
    """
    now = datetime.datetime.now()
    if min_time < now:
        max_time = getattr(notification, "max_time")

        time_diff = max_time - now
        time_diff_minutes = time_diff.total_seconds() / 60
        if time_diff_minutes <= 5:
            give_now.append(notification)
            to_be_removed.append(notification)

        else:
            can_be_given.append(notification)
            to_be_removed.append(notification)
    return can_be_given, give_now, to_be_removed
