"""Garden advice program.

Generates simple gardening advice based on the current season and the
type of plant being grown.
"""

# Default values used by the program.
# TODO: Replace with input() to allow user interaction.
SEASON = "summer"
PLANT_TYPE = "flower"


def get_season_advice(season):
    """Return gardening advice for the given season.

    Args:
        season (str): The season, e.g. "summer" or "winter".

    Returns:
        str: Advice for that season, ending with a newline. A default
        message is returned for unrecognised seasons.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        # Any other season has no specific advice yet
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice for the given plant type.

    Args:
        plant_type (str): The kind of plant, e.g. "flower" or "vegetable".

    Returns:
        str: Advice for that plant type. A default message is returned
        for unrecognised plant types.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        # Any other plant type has no specific advice yet
        return "No advice for this type of plant."


def main():
    """Build the combined advice and print it."""
    # Season advice ends in a newline, so plant advice appears on the next line
    advice = get_season_advice(SEASON) + get_plant_advice(PLANT_TYPE)
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
