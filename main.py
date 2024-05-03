import random
import string


def generate_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password


if __name__ == "__main__":
  password_length = 12  # You can adjust the length as needed
  password = generate_password(password_length)
  print("Day 1 Password:", password)
