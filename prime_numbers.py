# Define "prime checker" function to check numbers from 0, till 100 if they are divided with the chosen number without remainder.
def prime_checker(number):
  num_of_dividers = 0
  for number_counter in range(1, 100):
    if number%number_counter == 0:
      num_of_dividers += 1
  if num_of_dividers >= 3:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

# Input number to be checked if it is prime
n = int(input()) 
prime_checker(number=n)