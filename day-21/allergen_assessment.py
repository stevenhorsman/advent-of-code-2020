import re, collections

input_file = 'day-21/input.txt'

def parse_input(input):
  allergen_matches = {}
  ingredient_count = collections.defaultdict(int)

  for line in input.splitlines():
    ingredients, allergens = line.split('(contains', 1)
    ingredients = re.findall(r'\w+', ingredients)
    allergens = re.findall(r'\w+', allergens)
    for allergen in allergens:
      if allergen not in allergen_matches:
        allergen_matches[allergen] = set(ingredients)
      else:
        allergen_matches[allergen] &= set(ingredients) # &= does intersection
    for ingredient in ingredients:
      ingredient_count[ingredient] += 1
  return allergen_matches, ingredient_count

def part1(input):
  allergen_matches, ingredient_count = parse_input(input)
  candidate_allergens = set().union(*allergen_matches.values())
  return sum (count for ingred, count in ingredient_count.items() if ingred not in candidate_allergens)

def part2(input):
  allergen_matches, _ = parse_input(input)
  candidate_allergens = set().union(*allergen_matches.values())
  matched_allergens = {}

  while len(candidate_allergens) > 0:
    for allergen in sorted(allergen_matches.keys(), key=lambda k: len(allergen_matches[k])):
      allergen_matches[allergen] &= candidate_allergens
      if len(allergen_matches[allergen]) == 1:
        # Guranteed_match
        candidate_allergens ^= allergen_matches[allergen] # ^= does not intersection
        matched_allergens[allergen] = allergen_matches[allergen].pop()

  ordered_ingredients = []
  for allergen in sorted(matched_allergens.keys()):
    ordered_ingredients.append(matched_allergens[allergen])

  return ','.join(ordered_ingredients)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))