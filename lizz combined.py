
import pygame
import time
from notifications_folder import create_notifications
from Text_to_speech import Text_to_voice
from notifications_folder import check_notifications
from notifications_folder import combine_notifications
from notifications_folder import screenorder
from notifications_folder import notification_details
import threading
import datetime
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Lizz')
widthscreen = 500
heightscreen = 813
# Set up the display
screen = pygame.display.set_mode((widthscreen, heightscreen))

# Load the images
eyes_open = pygame.image.load(
    'Lizz/Liz images(NML)/faces & hands/Neutraal mond dicht.png').convert_alpha()
eyes_half = pygame.image.load(
    'Lizz/Liz images(NML)/faces & hands/Neutraal ogen halfdicht.png').convert_alpha()
eyes_closed = pygame.image.load(
    'Lizz/Liz images(NML)/faces & hands/Neutraal ogen dicht.png').convert_alpha()
hands = pygame.image.load(
    'Lizz/Liz images(NML)/faces & hands/Neutraal vlak.png').convert_alpha()
background = pygame.image.load(
    'achtergrond_Lizz.jpg')
front = pygame.image.load(
    'Lizz/Liz images(NML)/faces & hands/Liz front.png').convert_alpha()

height = heightscreen * 1.4
width = widthscreen * 1.4

# Rescale the images
eyes_open = pygame.transform.scale(eyes_open, (width, height))
eyes_half = pygame.transform.scale(eyes_half, (width, height))
eyes_closed = pygame.transform.scale(eyes_closed, (width, height))
hands = pygame.transform.scale(hands, (width, height))
background = pygame.transform.scale_by(background, 0.8)
front = pygame.transform.scale(front, (width, height))


white = (255, 255, 255)
black = (0, 0, 0)

notifications = []

current_time_hour = datetime.datetime.now().hour
current_time_minute = datetime.datetime.now().minute

# Initialize the timings of the notifications
timings = [[current_time_hour, current_time_minute + 5], [current_time_hour, current_time_minute + 16],
           [current_time_hour, current_time_minute + 28], [current_time_hour, current_time_minute + 40]]
for timing in timings:
    if timing[1] >= 60:
        timing[0] += 1
        timing[1] -= 60
    elif timing[1] == 59:
        timing[1] = 58


random.shuffle(timings)

print("timings", timings)

# Please fill in name
name = "Results/overig.txt" # File in which which the order of variants will be saved

order = []

for timing in timings:
    order.append(timing[0] * 60 + timing[1])

order_sorted = sorted(order)

notification_filenames = ["null u1", "new u1", "null u2", "new u2"]

f = open(name, "w") # write the order of versions into the file
for i in range(len(order_sorted)):
    index = order.index(order_sorted[i])
    f.write(str(i) + ': ' + notification_filenames[index] + '\n')
    print(notification_filenames[index])
f.close()

# select the right notifications

# screen version = v1
# notifications.append(
#     create_notifications.create_notification(timings[0][0], timings[0][1], timings[0][0], timings[0][1], 1, "weather", "De zon schijnt, heeft u misschien zin in een wandeling?", "original"))
# notifications.append(
#     create_notifications.create_notification(timings[0][0], timings[0][1], timings[0][0], timings[0][1], 1, "other", "Hoe heeft u geslapen?", "original"))
# notifications.append(
#     create_notifications.create_notification(timings[0][0], timings[0][1], timings[0][0], timings[0][1], 1, "other", "Hoe voelt u zich?", "original"))

notifications.append(
    create_notifications.create_notification(timings[1][0], timings[1][1], timings[1][0], timings[1][1], 1, "weather", "De zon schijnt, heeft u misschien zin in een wandeling?", "screen"))
notifications.append(
    create_notifications.create_notification(timings[1][0], timings[1][1], timings[1][0], timings[1][1], 1, "other", "Hoe heeft u geslapen?", "screen"))
notifications.append(
    create_notifications.create_notification(timings[1][0], timings[1][1], timings[1][0], timings[1][1], 1, "other", "Hoe voelt u zich?", "screen"))


# notifications.append(
#     create_notifications.create_notification(timings[2][0], timings[2][1], timings[2][0], timings[2][1], 2, "other", "Het is tijd om de bakplaat uit de oven te halen", "original"))
# notifications.append(
#     create_notifications.create_notification(timings[2][0], timings[2][1], timings[2][0], timings[2][1], 2, "other", "Het is tijd om uw medicatie te nemen", "original"))

# notifications.append(
#     create_notifications.create_notification(timings[3][0], timings[3][1], timings[3][0], timings[3][1], 2, "other", "Het is tijd om de bakplaat uit de oven te halen", "screen"))
# notifications.append(
#     create_notifications.create_notification(timings[3][0], timings[3][1], timings[3][0], timings[3][1], 2, "other", "Het is tijd om uw medicatie te nemen", "screen"))


# talking version v2
# notifications.append(
#     create_notifications.create_notification(timings[0][0], timings[0][1], timings[0][0], (timings[0][1]), 1, "weather", "De zon schijnt, heeft u misschien zin in een wandeling?", "original"))
# notifications.append(
#     create_notifications.create_notification(timings[0][0], timings[0][1], timings[0][0], (timings[0][1]), 1, "social", "Hoe heeft u geslapen?", "original"))
# notifications.append(
#     create_notifications.create_notification(timings[0][0], timings[0][1], timings[0][0], (timings[0][1]), 1, "other", "Het is tijd om naar uw kappersafspraak te gaan", "original"))

# notifications.append(
#     create_notifications.create_notification(timings[1][0], timings[1][1], timings[1][0], (timings[1][1]), 1, "weather", "De zon schijnt, heeft u misschien zin in een wandeling?", "talking"))
# notifications.append(
#     create_notifications.create_notification(timings[1][0], timings[1][1], timings[1][0], (timings[1][1]), 1, "social", "Hoe heeft u geslapen?", "talking"))
# notifications.append(
#     create_notifications.create_notification(timings[1][0], timings[1][1], timings[1][0], (timings[1][1]), 1, "other", "Het is tijd om naar uw kappersafspraak te gaan", "talking"))


# notifications.append(
#     create_notifications.create_notification(timings[2][0], timings[2][1], timings[2][0], (timings[2][1]), 2, "other", "Het is tijd om uw ademhalingsoefeningen te doen", "original"))
# notifications.append(
#     create_notifications.create_notification(timings[2][0], timings[2][1], timings[2][0], (timings[2][1]), 2, "other", "Het is tijd om uw beenoefeningen te doen", "original"))

# notifications.append(
#     create_notifications.create_notification(timings[3][0], timings[3][1], timings[3][0], (timings[3][1]), 2, "other", "Het is tijd om uw ademhalingsoefeningen te doen", "talking"))
# notifications.append(
#     create_notifications.create_notification(timings[3][0], timings[3][1], timings[3][0], (timings[3][1]), 2, "other", "Het is tijd om uw beenoefeningen te doen", "talking"))

# locations on the screen that can be used to show notifications/messages
possible_positions_overview = {
    1: [[widthscreen // 2,  400]],
    2: [[widthscreen // 2,  400], [widthscreen // 2,  600]],
    3: [[widthscreen // 2,  350], [widthscreen // 2,  550], [widthscreen // 2,  750]],
    4: [[widthscreen // 2,  350], [widthscreen // 2,  483],
        [widthscreen // 2,  616], [widthscreen // 2,  750]]
}

possible_positions_details = {
    1: [[widthscreen // 2,  420]],
    2: [[widthscreen // 2,  420], [widthscreen // 2,  620]],
    3: [[widthscreen // 2,  400], [widthscreen // 2,  575], [widthscreen // 2,  750]],
    4: [[widthscreen // 2,  400], [widthscreen // 2,  518],
        [widthscreen // 2,  636], [widthscreen // 2,  750]]
}

one_notification = [[widthscreen // 2,  400]]
two_notifications = [[widthscreen // 2,  400], [widthscreen // 2,  600]]
three_notifications = [[widthscreen // 2,  350],
                       [widthscreen // 2,  550], [widthscreen // 2,  750]]
font = pygame.font.SysFont('arial.ttf', 24)
font_details = pygame.font.SysFont('arial.ttf', 26)

give_now = []
give_user = []
can_be_given = []


def show_notifications(notifications_to_show):
    """Shows the notifications on the screen

    Args:
        notifications_to_show (list): the notifications that need to be shown

    Returns:
        (list, list): the notifications in the order that they are given and the rectangles that are shown on the screen
    """
    notifications_to_give = screenorder.get_screenorder(notifications_to_show)
    notificationpositions = possible_positions_details[len(
        notifications_to_give)]
    rectangles = []
    screen.blit(background, (-150, 0))
    screen.blit(hands, (-100, -200))
    screen.blit(front, (-100, -200))

    # Show the message that the user has to select a message
    text_select_notification = font.render(
        "Selecteer een bericht", True, black, (222, 233, 207))
    pygame.draw.rect(screen, (222, 233, 207), pygame.Rect(
        23, 287, 450, 75))
    pygame.draw.rect(screen, black, pygame.Rect(
        23, 287, 450, 75), 2)
    text_rect = text_select_notification.get_rect(center=(500/2, 287 + 75/2))
    screen.blit(text_select_notification, text_rect)
    for i in range(len(notifications_to_give)):
        # Show the notification on the screen within a square box
        text = font.render(
            getattr(notifications_to_give[i], "message"), True, black, white)
        textRect = text.get_rect()
        textRect2 = pygame.Rect(
            100, 700, textRect.width + 60, textRect.height + 40)
        textRect.center = (
            notificationpositions[i][0], notificationpositions[i][1])
        textRect2.center = (
            notificationpositions[i][0], notificationpositions[i][1])
        rectangles.append(textRect2)
        pygame.draw.rect(screen, white, textRect2, border_radius=25)
        pygame.draw.rect(screen, black, textRect2, 2, border_radius=25)
        screen.blit(text, textRect)
    screen.blit(front, (-100, -200))
    pygame.display.update(pygame.Rect(0, 280, 500, 533)) # refresh the screen
    return notifications_to_give, rectangles


def show_details(message, poss_answers):
    """Shows the possible answers for a notification on the screen

    Args:
        message (str): the notification message
        poss_answers (list): the possible answers

    Returns:
        list: the rectangles that are shown on the screen
    """
    textmessage = font_details.render(message, True, black, (222, 233, 207))
    answerpositions = possible_positions_details[len(poss_answers)]
    rectangles = []

    screen.blit(background, (-150, 0))

    for i in range(len(poss_answers)):
        # show the possible answer in the screen within a square box
        text = font.render(
            poss_answers[i], True, black, white)
        textRect = text.get_rect()
        textRect.center = (
            answerpositions[i][0], answerpositions[i][1])
        textRect2 = pygame.Rect(
            100, 700, textRect.width + 60, textRect.height + 40)
        textRect.center = (
            answerpositions[i][0], answerpositions[i][1])
        textRect2.center = (
            answerpositions[i][0], answerpositions[i][1])
        rectangles.append(textRect2)
        pygame.draw.rect(screen, white, textRect2, border_radius=25)
        pygame.draw.rect(screen, black, textRect2, 2, border_radius=25)
        rectangles.append(textRect)
        screen.blit(text, textRect)

    # show the message
    pygame.draw.rect(screen, (222, 233, 207), pygame.Rect(
        23, 287, 450, 75))
    pygame.draw.rect(screen, black, pygame.Rect(
        23, 287, 450, 75), 2)

    text_rect = textmessage.get_rect(center=(500/2, 287 + 75/2))
    screen.blit(textmessage, text_rect)

    screen.blit(hands, (-100, -200))
    screen.blit(front, (-100, -200))

    pygame.display.update(pygame.Rect(0, 280, 500, 533)) # refresh the screen
    return rectangles


def show_lizz():
    """Show the face of Lizz
    """
    while True:
        screen.blit(eyes_open, (-100, -200))
        screen.blit(front, (-100, -200))

        pygame.display.update(pygame.Rect(0, 0, 500, 280)) # Show Lizz with open eyes

        # Wait for 2.5 seconds
        time.sleep(2.5)

        # Display the second image
        screen.blit(eyes_half, (-100, -200))
        screen.blit(front, (-100, -200))

        pygame.display.update(pygame.Rect(0, 0, 500, 280)) # Show Lizz with their eyes half open

        time.sleep(0.1)
        screen.blit(eyes_closed, (-100, -200))
        screen.blit(front, (-100, -200))

        pygame.display.update(pygame.Rect(0, 0, 500, 280)) # Show Lizz with their eyes closed

        time.sleep(0.3)
        screen.blit(eyes_half, (-100, -200))
        screen.blit(front, (-100, -200))

        pygame.display.update(pygame.Rect(0, 0, 500, 280)) # Show Lizz with their eyes half open
        time.sleep(0.1)


threadlizz = threading.Thread(target=show_lizz)
threadlizz.start() # Always let Lizz blink

# Keep the window open until the user closes it
# Show all "basic" images on the screen
screen.blit(background, (-150, 0))
screen.blit(hands, (-100, -200))
screen.blit(front, (-100, -200))
pygame.display.update(pygame.Rect(0, 280, 500, 533))
running = True
while running:
    updated = check_notifications.check_notifications_list(  # Check new notifications
        notifications, can_be_given, give_now)
    notifications = updated[0]
    can_be_given = updated[1]
    give_now = updated[2]

    updated = check_notifications.check_can_be_given(
        can_be_given, give_now)  # Check notifications that can be given
    can_be_given = updated[0]
    give_now = updated[1]
    if give_now and len(give_user) == 0:
        updated = combine_notifications.combine_have_to(  # Combine notifications that have to be given
            can_be_given, give_now)
        can_be_given = updated[0]
        give_now = updated[1]
        give_user = updated[2]

    if can_be_given and len(give_user) == 0:
        # Combine notifications that can be given
        updated = combine_notifications.combine_can(can_be_given)
        can_be_given = updated[0]
        give_user = updated[1]

    if give_user:  # Say the correct message
        show_type = getattr(give_user[0], "show_type")
        if show_type == "screen" or show_type == "talking":
            Text_to_voice.tell_message(give_user, show_type)
    while give_user: # Show the messages on the screen
        if show_type == "screen" or show_type == "talking":
            showing = show_notifications(give_user)
            notifications_to_give = showing[0]
            rectangles = showing[1]

            clicked = False
            while not clicked: # Check whether the user clicked on a certain message
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for rect in rectangles:
                            if rect.collidepoint(event.pos):
                                clicked = True
                                clicked_notification = notifications_to_give[rectangles.index(
                                    rect)]
                                clicked_on = getattr(
                                    clicked_notification, "message")
                                break
                    if event.type == pygame.QUIT:
                        pygame.quit()
            poss_answers = notification_details.get_details(clicked_on)
            detail_rectangles = show_details(clicked_on, poss_answers)
        else: # show_type == original
            Text_to_voice.tell_message(give_user, show_type)
            # showing = show_notifications([give_user[0]])
            poss_answers = notification_details.get_details(
                getattr(give_user[0], "message"))
            detail_rectangles = show_details( # show the possible answers on the screen
                getattr(give_user[0], "message"), poss_answers)
            clicked_notification = give_user[0]

        clickedDetails = False
        while not clickedDetails: # Check whether the user selected an answer
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for rect in detail_rectangles:
                        if rect.collidepoint(event.pos):
                            clickedDetails = True
                            break
                if event.type == pygame.QUIT:
                    pygame.quit()
        give_user.remove(clicked_notification)
        screen.blit(background, (-150, 0))
        screen.blit(hands, (-100, -200))
        screen.blit(front, (-100, -200))
        pygame.display.update(pygame.Rect(0, 280, 500, 533)) # Refresh the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Close the window

# Quit Pygame
pygame.quit()
