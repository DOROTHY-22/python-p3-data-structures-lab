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
    """
    Returns a list of strings with the names of each spicy food.

    Args:
        spicy_foods: A list of dictionaries, where each dictionary
                      represents a spicy food and contains the keys
                      "name", "cuisine", and "heat_level".

    Returns:
        A list of strings, where each string is the name of a spicy food.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of dictionaries where the heat level of the food is greater than 5.

    Args:
        spicy_foods: A list of dictionaries, where each dictionary
                      represents a spicy food and contains the keys
                      "name", "cuisine", and "heat_level".

    Returns:
        A list of dictionaries representing the spiciest foods.
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Outputs to the terminal each spicy food in the specified format.

    Args:
        spicy_foods: A list of dictionaries, where each dictionary
                      represents a spicy food and contains the keys
                      "name", "cuisine", and "heat_level".
    """
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary for the spicy food whose cuisine matches
    the cuisine being passed to the method.  If multiple foods match, returns the first.

    Args:
        spicy_foods: A list of dictionaries, where each dictionary
                      represents a spicy food and contains the keys
                      "name", "cuisine", and "heat_level".
        cuisine: The name of the cuisine to filter by (e.g., "American").

    Returns:
        A dictionary representing the spicy food of the specified cuisine.
        Returns None if no matching cuisine is found.
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Explicitly return None if no match is found

def print_spiciest_foods(spicy_foods):
    """
    Outputs to the terminal ONLY the spicy foods that have a heat level greater than 5,
    in the specified format.  Uses get_spiciest_foods().

    Args:
        spicy_foods: A list of dictionaries.
    """
    spiciest_foods_list = get_spiciest_foods(spicy_foods)  # Reuse get_spiciest_foods
    for food in spiciest_foods_list:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    """
    Returns an integer representing the average heat level of all the spicy foods.

    Args:
        spicy_foods: A list of dictionaries, where each dictionary
                      represents a spicy food and contains the keys
                      "name", "cuisine", and "heat_level".

    Returns:
        A float representing the average heat level of the spicy foods.
        Returns 0 if the input list is empty.
    """
    if not spicy_foods:
        return 0.0  # Handle empty list case
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    """
    Adds a new spicy_food to the original list and returns the modified list.

    Args:
        spicy_foods: A list of dictionaries, where each dictionary
                      represents a spicy food and contains the keys
                      "name", "cuisine", and "heat_level".
        new_food: A dictionary representing the new spicy food to add.
                  It should have the same keys: "name", "cuisine", and "heat_level".

    Returns:
        The original list with the new spicy food added.
    """
    spicy_foods.append(new_food)
    return spicy_foods #returning the list

# Example Usage
print("1. Get Names:")
print(get_names(spicy_foods))  # Output: ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

print("\n2. Get Spiciest Foods (Heat Level > 5):")
print(get_spiciest_foods(spicy_foods))
# Output: [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9},
#          {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]

print("\n3. Print Spicy Foods:")
print_spicy_foods(spicy_foods)
# Output:
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

print("\n4. Get Spicy Food by Cuisine (American):")
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
# Output: {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}

print("\n5. Get Spicy Food by Cuisine (Thai):")
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
# Output: {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}

print("\n6. Print Spiciest Foods (Again, using get_spiciest_foods):")
print_spiciest_foods(spicy_foods)
# Output:
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

print("\n7. Get Average Heat Level:")
print(get_average_heat_level(spicy_foods))  # Output: 6.0

print("\n8. Create Spicy Food:")
new_food = {"name": "Jollof Rice", "cuisine": "Nigerian", "heat_level": 7}
updated_foods = create_spicy_food(spicy_foods, new_food)
print(updated_foods)
# Output:
# [
#     {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9},
#     {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3},
#     {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6},
#     {'name': 'Jollof Rice', 'cuisine': 'Nigerian', 'heat_level': 7}
# ]
