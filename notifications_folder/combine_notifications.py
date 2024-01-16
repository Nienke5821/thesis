def combine_have_to(can_be_given, give_now):
    """Checks which messages that have to be given now can be given at the same time

    Args:
        can_be_given (list): notifications that can be given
        give_now (list): notifications that must be given now

    Returns:
        (list, list, list): the updated lists of notifications that can be given, notifications that must be given now
                        and notifications that are shown to the user
    """
    give_user = []
    to_be_removed = []
    # urgency 3
    for notification in give_now:
        if getattr(notification, "urgency") == 3:
            give_user.append(notification)
            to_be_removed.append(notification)
            break

    if give_user:
        give_now.remove(give_user[0])
        return can_be_given, give_now, give_user

    # urgency 2
    not2 = None
    for notification in give_now:
        if getattr(notification, "urgency") == 2:
            not2 = notification
            break
    if not2 != None:
        give_user.append(not2)
        give_now.remove(not2)
        if give_now:
            updated = add_not_urg_2(give_now, give_user)

            give_now = updated[0]
            give_user = updated[1]

        if len(give_user) == 1 and can_be_given:
            # check can be given
            updated = add_not_urg_2(can_be_given, give_user)
            can_be_given = updated[0]
            give_user = updated[1]

        return can_be_given, give_now, give_user

    for i in range(3):  # max 3 items of urgency 1, none of urgency 2 or 3
        if give_now:
            give_user.append(give_now.pop(0))
        elif can_be_given:
            give_user.append(can_be_given.pop(0))

    return can_be_given, give_now, give_user


def add_not_urg_2(check_list, give_user):
    """Adds a notification of urgency level 2 to the list of notifications that is shown to the user

    Args:
        check_list (list): the list that is checked for a notification of urgency level 2
        give_user (list): notifications that are shown to the user

    Returns:
        (list, list): the updated lists of notifications that has been checked, 
                        and notifications that are shown to the user
    """
    not2_2 = None  # urgency 2
    not2_1 = None  # urgency 1
    for notification in check_list:
        if getattr(notification, "urgency") == 2:
            not2_2 = notification
            break
        elif getattr(notification, "urgency") == 1:
            not2_1 = notification
    if not2_2 != None:
        give_user.append(not2_2)
        check_list.remove(not2_2)
    elif not2_1 != None:
        give_user.append(not2_1)
        check_list.remove(not2_1)
    return check_list, give_user


def combine_can(can_be_given):
    """Checks which messages that can be given, can be given at the same time

    Args:
        can_be_given (list): notifications that can be given

    Returns:
        (list, list): an updated list of notifications that can be given and a list of notifications 
                        that will be shown to the user
    """
    give_user = []
    highest_urgency = 0
    highest_notification = None
    for notification in can_be_given:
        if getattr(notification, "urgency") > highest_urgency:
            highest_urgency = getattr(notification, "urgency")
            highest_notification = notification

    if highest_urgency == 3:
        give_user.append(highest_notification)
        can_be_given.remove(highest_notification)

    elif highest_urgency == 2 and len(can_be_given) >= 2:
        can_be_given.remove(highest_notification)
        give_user.append(highest_notification)

        updated = add_not_urg_2(can_be_given, give_user)
        can_be_given = updated[0]
        give_user = updated[1]

        if len(give_user) == 1:
            can_be_given.append(give_user.pop(0))

    if highest_urgency == 1 and len(give_user) == 0 and len(can_be_given) >= 3:
        for notification in can_be_given:
            if getattr(notification, "urgency") == 1 and len(give_user) < 3:
                give_user.append(notification)

        if len(give_user) == 3:
            for notification in give_user:
                can_be_given.remove(notification)
        else:
            give_user = []
    return can_be_given, give_user
