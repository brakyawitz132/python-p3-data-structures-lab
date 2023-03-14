spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [n.get("name") for n in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    foods = [n for n in spicy_foods if n["heat_level"] > 5]
    return foods

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(f"{n['name']} ({n['cuisine']}) | Heat Level: " + ("🌶" * n["heat_level"]))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return [n for n in spicy_foods if n['cuisine'] == cuisine]
    for n in spicy_foods:
        if n['cuisine'] == cuisine:
            return n


def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        if n["heat_level"] > 5:
            print(f"{n['name']} ({n['cuisine']}) | Heat Level: " + ("🌶" * n["heat_level"]))

def get_average_heat_level(spicy_foods):
    sum = 0
    for n in spicy_foods:
        sum += n['heat_level']
    return sum / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
