
def get_names(spicy_foods):
  """
  Extracts and returns a list of names from a list of spicy foods.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.

  Returns:
      A list of strings containing the names of the spicy foods.
  """
  return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
  """
  Filters and returns a list of spicy foods with a heat level greater than 5.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.

  Returns:
      A list of dictionaries representing spicy foods with heat level > 5.
  """
  return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
  """
  Prints each spicy food in a specific format to the console.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.
  """
  for food in spicy_foods:
    heat_level_str = "" * food["heat_level"]
    print(
        f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_str}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
  """
  Finds and returns a single dictionary representing a spicy food with a matching cuisine.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.
      cuisine: A string representing the cuisine to search for.

  Returns:
      A dictionary representing the spicy food with the matching cuisine, or None if not found.
  """
  for food in spicy_foods:
    if food["cuisine"] == cuisine:
      return food
  return None


def print_spiciest_foods(spicy_foods):
  """
  Prints only the spicy foods with a heat level greater than 5, using previously defined functions.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.
  """
  spiciest_foods = get_spiciest_foods(spicy_foods)
  print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
  """
  Calculates and returns the average heat level of all the spicy foods.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.

  Returns:
      An integer representing the average heat level.
  """
  total_heat = sum(food["heat_level"] for food in spicy_foods)
  return total_heat // len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
  """
  Appends a new spicy food dictionary to the provided list and returns the modified list.

  Args:
      spicy_foods: A list of dictionaries representing spicy foods.
      new_food: A dictionary representing the new spicy food to add.

  Returns:
      A new list of dictionaries with the new spicy food added.
  """
  spicy_foods.append(new_food)
  return spicy_foods

