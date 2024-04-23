import random
import numpy as np
from colorama import Fore,Style
import time

num_simulations = 1 #num of cases
num_acquired = 0 #num of knife
most_num_acquired= 0 # most knifes acquired in a single run 
times_of_getting_nothing = 0 # total times of getting nothing from cases  
total_knifes_acquired = 0 # total knifes acquired from cases

simulations = 1

def acquire_item():
    # Generate a random number between 0 and 1
    probability = random.random()
    
    # Check if the probability falls within 0.26%
    if probability <= 0.0026: # 0.26% expressed as a decimal
        return True  # Item acquired
    else:
        return False  # Item not acquired
    
def simulate():
 global total_knifes_acquired 
 global times_of_getting_nothing 
 global simulations
 global num_simulations 
 global num_acquired 
 global most_num_acquired
 for i in np.arange(0,simulations+1): # number of simulation 
  total_knifes_acquired += num_acquired
  if num_acquired > most_num_acquired:
      most_num_acquired = num_acquired
  if num_acquired == 0 :
      times_of_getting_nothing += 1

  num_acquired = 0
 
 
  for _ in range(num_simulations):
      if acquire_item():
          num_acquired += 1
          


action = input('Would you rather open cases and simulate of getting knife or test the probabilty of getting knife (1-simulate / 2-test) (1/2)')


if action == '1' :

    num_simulations = int(input('Type Number of Cases you want to simulate --> '))

    simulations = 1
    start_time = time.time()  # Start timing
    simulate()
    end_time = time.time()  # End timing
    print('Case Simulating.')
    time.sleep(1)
    print('Case Simulating..')
    time.sleep(1)
    print('Case Simulating...')
    time.sleep(1)

    execution_time = end_time - start_time
    # Tablo başlıkları
    print( "=" * 80 + Style.RESET_ALL)
    print(Fore.MAGENTA + "{:<30} {:<30} {:<20}".format("Description", "Amount (Dollar)", "Frequency") + Style.RESET_ALL)
    print("=" * 80)

    # Tablo satırları

    print("{:<30} {:<30} {:<20}".format("Money spend on cases", num_simulations * 0.30, ""))
    print("{:<30} {:<30} {:<20}".format("The keys", num_simulations * 2.5, ""))
    print("{:<30} {:<30} {:<20}".format("Total amount spent", (num_simulations * 0.3) + (num_simulations * 2.5), ""))

    print("-" * 80)


    print("{:<30} {:<30} {:<20}".format("The item was acquired", total_knifes_acquired, "times"))

    print("-" * 80)

    print("Execution time:", execution_time, "seconds")
elif action == '2' :
   num_simulations = int(input('Type Number of Cases you want to simulate --> '))
   simulations = int(input('Type Number of simulations you want to try --> '))
   start_time = time.time()  # Start timing
   simulate()
   end_time = time.time()  # End timing
   print('Theory Simulating.')
   time.sleep(1)
   print('Theory Simulating..')
   time.sleep(1)
   print('Theory Simulating...') 
   time.sleep(1)

   execution_time = end_time - start_time

   # Tablo başlıkları
   print( "=" * 80 + Style.RESET_ALL)
   print(Fore.MAGENTA + "{:<30} {:<30} {:<20}".format("Description", "Amount (Dollar)", "Frequency") + Style.RESET_ALL)
   print("=" * 80)

   # Tablo satırları

   print("{:<30} {:<30} {:<20}".format("Money spend on cases", simulations*(num_simulations * 0.30), ""))
   print("{:<30} {:<30} {:<20}".format("The keys", simulations*(num_simulations * 2.5), ""))
   print("{:<30} {:<30} {:<20}".format("Total amount spent", simulations*(num_simulations * 0.3) + simulations*(num_simulations * 2.5), ""))

   print("-" * 80)


   print("{:<30} {:<30} {:<20}".format("The item was acquired", total_knifes_acquired, "times"))

   print("-" * 80)

   print("{:<30} {:<30} {:<20}".format("The best run return", most_num_acquired, "knifes out of"))
   print("{:<30} {:<30} {:<20}".format("Times of getting nothing", times_of_getting_nothing , "{(times_of_getting_nothing / simulations) * 100} %"))
   print("{:<30} {:<30} {:<20}".format("", "", "which means"))
   print("{:<30} {:<30} {:<20}".format("", "", f"{(times_of_getting_nothing / simulations) * 100} %"))

   print("-" * 80)

   print("{:<30} {:<30} {:<20}".format("Total knifes acquired", total_knifes_acquired, f"out of {simulations} simulation which means the average num of knifes you will get is {total_knifes_acquired / simulations} in {num_simulations} cases"))

   print("Execution time:", execution_time, "seconds")
else :
   print('Invalid Entry Try Again Please !')