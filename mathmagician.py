import math
import time
import random

class Mathmagician:

  def __init__(self):
    pass

  def show_menu(self):

    print("1. Print random number")
    print("2. Print Fibonacci Sequence")
    print("3. Print prime numbers")
    print("4. Exit Program")
    choice = input("> ")

    try:
      if int(choice) > 0 and int(choice) < 5:

        if choice != "4":
          print("")
          print("How many numbers?")
          count = input("> ")

      if (choice == "1"):
        print("Your choice was #1")
        ints = self.random_numbers(int(count))
        self.print_results(ints)

      if choice == "2":
        print("Your choice was #2")
        fibo = self.fibonacci_sequence(int(count))
        self.print_results(fibo)

      if choice == "3":
        print("Your choice #3")
        prime = self.generate_prime_numbers(int(count))
        self.print_results(prime)

      if (choice == "4"):
        print("See Ya!")
        raise SystemExit()

    except ValueError:
      print("Please enter your choice")
    self.show_menu()

  def random_numbers(self, count):
    some_random_numbers = list()

    for number in range(count):
      some_random_numbers.append(random.randint(0,100))

    print(some_random_numbers, 'Here are your random numbers')
    return some_random_numbers

  def fibonacci_sequence(self, count):
    result = list()

    #inner func that generates fib seq numb
    def fib():
      a,b = 0,1
      yield a #first __next__()
      yield b #second __next__()

      while True:
        a, b = b, a + b
        yield b # Third+ __next__()

      #Create instance of generator
    f = fib()

      #Call generator 'count' time and append the output to result list
    for a in range(count):
      result.append(f.__next__())
      #Return the list with 'count' numbers in it
    return result


  def generate_prime_numbers(self, count):
    result = list()
    i, x = 2, 1
    while x <= count:
      isPrime = True
      for n in range(2, int(math.sqrt(i) + 1)):
        if i % n == 0:
          isPrime = False
          break
      if isPrime:
        result.append(i)
        x += 1
      i +=1

    return result

  def print_results(self, nums):
    for n in nums:
      print(n)
      time.sleep(.5)


if __name__ == "__main__":
  menu = Mathmagician()
  menu.show_menu()
