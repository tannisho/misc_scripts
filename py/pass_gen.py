import random
import string

def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

# 5 letters and 3 digits
print("First random alphanumeric string is:", get_random_alphanumeric_string(6, 4))

# 6 letters and 2 digits
print("Second random alphanumeric string is:", get_random_alphanumeric_string(6, 2))
