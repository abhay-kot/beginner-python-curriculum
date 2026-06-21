animals = ["cat", "dog", "cat", "bird", "dog", "cat", "cat", "dog", "cat", "cat"]
def count_animals(animal_list):
    animal_count = {}
    for animal in animal_list:
        if animal in animal_count:
            animal_count[animal] += 1
        else:
            animal_count[animal] = 1
    return animal_count

animal_counts = count_animals(animals)
print(animal_counts)
num_cats = animal_counts.get("cat", 0)
print(f"Number of cats: {num_cats}")
num_dogs = animal_counts.get("dog", 0)
print(f"Number of dogs: {num_dogs}")
def count_odd_numbers(number_list):
    odd_count = 0
    for number in number_list:
        if number % 2 != 0:
            odd_count += 1
    return odd_count
print(count_odd_numbers([13, 22, 8, 19, 6, 7]))
for I in range(len(animals)):
    print(I)

for I in range(len(animals)):
    item = animals[I]
    print(item)
def countnumbersaboveten(number_list):
    count = 0
    for number in number_list:
        if number > 10:
            count += 1
    return count
print(countnumbersaboveten([5, 12, 3, 20, 7, 15]))