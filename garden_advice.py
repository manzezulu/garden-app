# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.


def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms.\n"
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!\n"
    else:
        return "No advice for this type of plant.\n"


def main():
    advice = get_season_advice(season) + get_plant_advice(plant_type)
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
