def get_screenorder(notifications):
    """Orders the notifications according to the order in which they have to be shown on the screen

    Args:
        notifications (list): the notifications that have to be ordered

    Returns:
        list: the notifications ordered in the correct way
    """
    social_notifications = []
    weather_notifications = []
    other_notifications = []

    for notification in notifications:
        category = getattr(notification, "category")
        if category == "social":
            social_notifications.append(notification)
        elif category == "weather":
            weather_notifications.append(notification)
        else:
            other_notifications.append(notification)

    ordered_notifications = [social_notifications,
                             other_notifications, weather_notifications]
    to_be_returned = []
    for category in ordered_notifications:
        for notification in category:
            to_be_returned.append(notification)
    return to_be_returned
