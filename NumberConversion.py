# A Number converter that converts decimals to binary, octal, or hexadecimal.
# You can also convert binary, octal, or hexadecimal to decimal.
# This is where I will dump any conversions that I want do.
# I'm hoping to continue putting more conversions such as from binary to hexa or oct to decimal or others.
# I'm also thinking of changing this file name and put arthematic operations in here as well.

import os
# clear screen
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# start text
def StartPage():
  print("Welcome to Number Converter")
  print("\n")
  print("Type 'A' to convert from Decimal to Binary ")
  print("Type 'B' to convert from Decimal to Octal ")
  print("Type 'C' to convert from Decimal to Hexadecimal ")
  print("Type 'Z' for more conversions ")
  print("\n")
# more conversions
def MoreConv():
  print("Type 'D' to convert from Binary to Decimal ")
  print("Type 'E' to convert from Octal to  Decimal")
  print("Type 'F' to convert from Hexadecimal to Decimal ")
  print("\n")

# Decimal to Binary
def DecToBin(decimal):
  answer = ''
  while decimal > 0:
    answer = str(decimal % 2) + answer
    decimal //= 2
  return answer

# Decimal to Octal
def DecToOct(decimal):
  answer = ''
  while decimal > 0:
    answer = str(decimal % 8) + answer
    decimal //= 8
  return answer

# Decimal to Hexadecimal
def DecToHex(decimal):
  answer = ''
  hexadict = {10: 'A', 11: 'B', 12: 'C', 13: 'D',14: 'E', 15: 'F'}
  while decimal > 0:
    if (decimal % 16) in hexadict:
      letter = hexadict[(decimal % 16)]
      answer = letter + answer
    else:
      answer = str(decimal % 16) + answer
    decimal //= 16
  return answer

# Binary to Decimal
def BinToDec(binn):
  answer = 0
  binlis = [int(x) for x in str(binn)]
  n = len(binlis)
  countdown = n
  for i in range(0,n):
      answer = binlis[i]*(2**(countdown-1)) + answer
      countdown -= 1
  return answer

# Octal to Decimal
def OctToDec(oct):
  answer = 0
  octlis = [int(x) for x in str(oct)]
  n = len(octlis)
  countdown = n
  for i in range(0,n):
    answer = octlis[i]*(8**(countdown-1)) + answer
    countdown -= 1
  return answer

# Hexadecimal to Decimal
def HexToDec(hexa):
  hexadict = {'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}
  answer = 0
  hexalis = [x for x in str(hexa)]
  n = len(hexalis)
  countdown = n
  for i in range(0,n):
    if hexalis[i] in hexadict:
      answer = hexadict[hexalis[i]]*(16**(countdown-1)) + answer
    else:
      answer = int(hexalis[i])*(16**(countdown-1)) + answer
    countdown -= 1
  return answer


# main place (where action takes place)
if __name__ == '__main__':
  Start = True
  # while loop so that it resets everytime and stops once user says no.
  while Start == True:
    StartPage()
    user_input = input("Type Here: ")
    if user_input == 'A' or user_input == 'a':
      decimal = int(input("Enter number: "))
      print(DecToBin(decimal))
    elif user_input == 'B' or user_input == 'b':
      decimal = int(input("Enter number: "))
      print(DecToOct(decimal))
    elif user_input == 'C' or user_input == 'c':
      decimal = int(input("Enter number: "))
      print(DecToHex(decimal))
    elif user_input == 'Z' or user_input == 'z':
      clear_screen()
      MoreConv()
      user_input = input("Type Here: ")
      if user_input == 'D' or user_input == 'd':
        binn = int(input("Enter binary: "))
        print(BinToDec(binn))
      elif user_input == 'E' or user_input == 'e':
        oct = int(input("Enter octal: "))
        print(OctToDec(oct))
      elif user_input == 'F' or user_input == 'f':
        hexa = str(input("Enter hexadecimal: "))
        print(HexToDec(hexa))
      else:
        print("Error 204: Wrong Input")
        break
    else:
        print("Error 204: Wrong Input")
        break
    reset = input("Do you want to convert a number again (Y/N)? ")
    if reset == 'Y' or reset == 'y':
      clear_screen()
    elif reset == 'N' or reset == 'n':
      print("Have a great day!")
      Start = False
    else:
      print("Error 204: Wrong Input")
    
    