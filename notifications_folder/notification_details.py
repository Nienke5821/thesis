details_dictionary = {
    "Het is tijd om uw medicatie te nemen": ["Oké"],
    "Het is tijd om naar uw kappersafspraak te gaan": ["Oké"],
    "Het is tijd om de bakplaat uit de oven te halen": ["Oké"],
    "Het is tijd om uw beenoefeningen te doen": ["Oké"],
    "De zon schijnt, heeft u misschien zin in een wandeling?": ["Ja", "Nee"],
    "Heeft u uw medicatie genomen?": ["Ja", "Nee"],
    "Het is tijd om uw ademhalingsoefeningen te doen": ["Oké"],
    "Hoe heeft u geslapen?": ["Slecht", "Oké", "Goed", "Geweldig"],
    "Hoe voelt u zich?": ["Slecht", "Oké", "Goed", "Geweldig"]
}


def get_details(message_content):
    """Gets the possible answers for the notification message that the user can give

    Args:
        message_content (str): The message of the notification

    Returns:
        list: the answers that the user can give
    """
    return details_dictionary[message_content]
