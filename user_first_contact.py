#!/usr/bin/python3
def get_user_name():
  """Prompts the user for their name and returns it.

  Returns:
    The user's name.
  """
  user_name = input("What is your name? ")
  return user_name


def greet(user_name):
  """Greets the user by name.

  Args:
    user_name: The user's name.

  Returns:
    A greeting message.
  """
  greeting = f"Hello, {user_name}!"
  return greeting


def main():
  """The main function of the program."""
  user_name = get_user_name()
  greeting = greet(user_name)
  print(greeting)


if __name__ == "__main__":
  main()
