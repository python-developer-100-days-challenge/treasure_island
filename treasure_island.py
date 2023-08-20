#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Treasure Island Adventure Game
# In this game, the player navigates through an island to find treasure.

# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
# First decision
treasure1 = input("what direction do you want to go Right or Left ").lower()

# Check first decision
if treasure1 == "left" or treasure1 == 'l':
  print("Next Adventure")

  # Second decision
  treasure2 = input("Will you like to swim or wait ").lower()
  
  # Check second decision
  if treasure2 == "wait":
    print("Next Wait Adventure")

    # Third decision
    treasure3 = input("What Color of door will you like to open ").lower()

    # Check third decision
    if treasure3 == "yellow":
      print(r'''
          Congratulations! You've found Ese's treasure!
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
    YOU WON!!! '-._'-.|| |' `_.-' ESE'S TREASURE!!!
                    '-.||_/.-'
''')
    elif treasure3 == "red":
      print("Burned by fire. \nGame Over")
    elif treasure3 == "Blue":
      print("Eaten by beasts. \nGame Over")
    else:
      print("Game Over")
  else:
    print("Attacked by trout. \nGame over")
else:
  print("Fall into a hole. \nGame Over")



