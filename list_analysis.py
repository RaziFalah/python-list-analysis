#Made by Razi Falah
#Copyright (C) 2022 razifalah.com
#https://razifalah.com
#According to the applied license: LICENSE GNU General Public License v3.0
#You do not have the right to republish sell or edit this project, use it only for private use and educational purposes

from typing import Counter


print("|========================|")
print("|Welcome to list analysis|")
print("==========================")
mylist = list()
ask_for_creation_type = input("what data type do you want the list to hold? float/int/str: ")
x = ask_for_creation_type
x = x.strip()
x = x.upper()
if x == "STR":
    pass
elif x == "INT":
    pass
elif x == "FLOAT":
    pass
else:
    print("Error: unkown action")
    exit()
ask_for_creation = int(input("You should create a list now, how many values do you want your list to have? "))
ask_for_creation_holder = ask_for_creation
Counter = 1
while 0 < ask_for_creation:
    if x == "STR":
      ask_for_values = str((input(f"What is the value for value number {Counter}: ")))
    elif x == "INT":
        ask_for_values = int((input(f"What is the value for value number {Counter}: ")))
    elif x == "FLOAT":
        ask_for_values = float((input(f"What is the value for value number {Counter}: ")))
    mylist.append(ask_for_values)
    Counter += 1
    ask_for_creation -= 1
print("Well done your list have been created with the len of: " + str(ask_for_creation_holder))
print("===============")
print("|analysis menu|")
print("===============")

while 0 != 1:
  ask_for_command = input("run: ")
  ask_for_command = ask_for_command.strip()
  ask_for_command = ask_for_command.upper()
  
  if(ask_for_command == "LEN"):
      print(len(mylist))
  elif(ask_for_command == "TYPE"):
      print(type(mylist))
  elif(ask_for_command == "RM"):
      ask_for_index = int(input("what index do you want to remove? "))
      ask_for_index = ask_for_index.upper()
      ask_for_index = ask_for_index.strip()
      if(ask_for_index == "LAST"):
          mylist.pop()
          print(mylist)
      else:
          del mylist[ask_for_index]
          print(mylist)
  elif(ask_for_command == "INSERT"):
      ask_for_insert = input("What do you want to insert: ")
      ask_for_where_to_insert = int(input("What index do you want to insert to: "))
      mylist.insert(ask_for_where_to_insert, ask_for_insert)
      print(mylist)
  elif(ask_for_command == "CLEAR"):
      mylist.clear()
      print(mylist)
  elif(ask_for_command == "COUNT"):
      ask_for_count = input("Check count for: ")
      mylist.count(ask_for_count)
      print(mylist)
  elif(ask_for_command == "COPY"):
      mylist.copy()
      print(mylist)
  elif(ask_for_command == "EXTEND"):
      ask_for_extend = int(input("How many items you want to add: "))
      counter = 0
      while 0 < ask_for_extend:
          ask_for_extend = ask_for_extend - 1
          counter = counter + 1
          ask_for_value_extend = input(f"What is the value for item {counter}: ")
          mylist.extend(ask_for_value_extend)
      print(mylist)
  elif(ask_for_command == "INDEX"):
      ask_for_search = input("What value you want to locate: ")
      if ask_for_search in mylist:
          do_print = mylist.index(ask_for_search)
          print(str(do_print))
      else:
          print(f"{ask_for_search} is not in the list")
  elif ask_for_command == "POP":
      mylist.pop()
      print(mylist)
  elif ask_for_command == "REMOVE":
      ask_for_remove = input("What value you want to remove: ")
      if ask_for_remove in mylist:
          mylist.remove(ask_for_remove)
          print(mylist)
      else:
          print(f"{ask_for_remove} is not in the list!")
  elif ask_for_command == "REVERSE":
      mylist.reverse()
      print(mylist)
  elif ask_for_command == "SORT":
      mylist.sort()
      print(mylist)
  elif ask_for_command == "APPEND":
      ask_for_append = input("What value you want to add: ")
      mylist.append(ask_for_append)
      print(mylist)
  elif ask_for_command == "EXIT":
      print("Ok, bye.")
      exit()
  elif ask_for_command == "CLEAR CLI":
      import os
      os.system('cls' if os.name == 'nt' else 'clear')
  else:
      print("Error: action is unkown, try again")
