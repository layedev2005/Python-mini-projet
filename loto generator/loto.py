import random

def generate_lotto_numbers():
  
    numbers = random.sample(range(1, 50), 6)
    numbers.sort() 
    return numbers


if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("Les numéros de loto générés sont : ", ' - '.join(map(str, lotto_numbers)))