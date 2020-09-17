# Author: Abigail Bowen aeb6095@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 6
# Breakout:
def sum_n(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if (n >= 1):
    print(s)
    print_n(s, n-1)


def run ():
  n = int(input("Enter an int: "))
  sum1 = sum_n(n) 
  print(f"sum is {sum1}.")
  s = input("Enter a string: ")
  print_n(s, n)

if __name__ == "__main__":
  run ()