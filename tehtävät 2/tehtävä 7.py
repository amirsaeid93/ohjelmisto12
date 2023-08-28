import random

def generate_3_digit_combination():
    return random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)

def generate_4_digit_combination():
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print("Random 3-digit combination:")
combo_3_digit = generate_3_digit_combination()
print(combo_3_digit)

print("\nRandom 4-digit combination:")
combo_4_digit = generate_4_digit_combination()
print(combo_4_digit)
