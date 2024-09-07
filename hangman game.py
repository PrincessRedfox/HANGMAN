# program: Hangman game.py
# author: Sarina Saiyed
# email: 2338323@students.carmel.ac.uk
# student number: 2338323
#
# You have been asked to work on the first episode of the game
# which is a modern take on the game of Hangman.
#
# The publisher has sent you some requirements:
#   The game and word content must be appropriate for students of upper primary school age (8-10)
#   An alternative to the traditional hangman should be considered.
#   The game is for a single player only.
#   The player must be informed whether they have won or not.
#   Each time a letter has been chosen, you should not be able to choose it again.
#   The player should get no more than 10 chances to guess the word correctly.

########################################################################
# Design

# The computer is given a list of spelling words to choose from 
# The computer randomly chooses a word from the list:
#       [addition, breath, central, decorator, earthquake, fraction,
#       guess, ignore, judge,kept, ledge, mention, narrate, often, palm,
#       royal, shear, trouble, understand, vocal, wander] 
# The computer stores the word 
# The game will begin for the user 
# The user is met with a screen containing: 
# The alterative hangman design (Daisy flower hangman) 
# The computer will output the number of characters in the randomly generated word 
# An empty section, titled, ‘Incorrect Guesses’ 
# The user is told that they only have 10 chances to guess the word correctly and
#   to only use the characters between a – z 
# While the number of guesses is less than 10 and the user has not won
# The user will enter a character, once 
# That input character will be compared with all the characters in the random word 
# If the letter that the user has inputted is in the random word 
# The alternative hangman design is remained the same 
# The associated placeholder character is replaced with the input guess 
# The ‘Incorrect Guesses’ section remains the same 
# The user is no longer allowed to use the character 
# If the letter the user has inputted is not in the random word 
# The user loses a chance 
# The alternative hangman design ‘loses a limb’ (A petal falls off) 
# The associated placeholder character remains the same 
# The input character is stored and displayed in the ‘Incorrect Guesses’ section 
# The user is no longer able to use the character again  
# If the random word is guessed correctly 
# Output a message stating that the user has won the game 
# Print the amount of guesses it took for the user to guess the word correctly 
# If the number of guesses is > 10	 
# Display the final stage of the alternative hangman design (dead flower head) 
# Output a message that states the user has lost the game 
# Print the random word 

########################################################################
# Pseudocode
#
# IMPORT random 
#
# SPELLINGWORDS = [addition, breath, central, decorator, earthquake, fraction, guess, ignore, judge, kept, ledge, mention, narrate, often, palm, royal, shear, trouble, understand, vocal, wander] 
#
# Index = RANDINT (0, LEN(SPELLINGWORDS)-1) 
# Word = SPELLINGWORDS[Index] 
# Correct = [] 
# Incorrect = [] 
# 
# DEF has_won(): 
#	Won = TRUE 
#	FOR chr in word: 
#		IF chr not in correct: 
#			won = FALSE 
#		ENDIF 
#	ENDFOR LOOP 
#	RETURN won 
# 
# WHILE LEN(incorrect)  < 10 AND not has_won(): 
#       FOR chr in word: 
#           IF chr in correct: 
#               PRINT(chr, end=” ”) 
#           ELSE: 
#               PRINT (“_”, end=” ”) 
#           ENDIF 
#       ENDFOR LOOP 
#       PRINT(“Incorrect:”,” “ ”.join(incorrect)) 
#       PRINT("You only have ", 10 –LEN(incorrect), “lives left”) 
#       Guess = INPUT(“Enter a guess: ”) 
#       WHILE not LEN(guess) ==  1 AND guess.isalpha(): 
#           PRINT(“Invalid guess – enter a single letter”) 
#           Guess =  INPUT(“Enter a guess: ”) 
#       ENDWHILE LOOP 
# 
#       IF guess in word: 
#           IF guess not in correct: 
#               Correct.append(guess) 
#           ENDIF 
#       ELSE: 
#           IF guess not in Incorrect: 
#		Incorrect.append(guess) 
#	    ENDIF 
#       ENDIF 
# ENDWHILE LOOP 
# 
# 
# IF has_won(): 
#       PRINT(“You’ve guessed the correct word and it only took”, 10 – LEN(incorrect), “tries !!”) 
# ELSE: 
#       PRINT(“Out of tries, the word you were guessing was”, word, “try again next time”)	 
# 
# ENDIF

########################################################################
# Variables

# list SPELLINGWORDS
# int Index
# str Word
# list Correct
# list Incorrect
# int tries
# bool Won
# str Guess


########################################################################
# Functions

# display
# has_won

########################################################################
# Main

import random # Imports the libriary that allows randomisation


SPELLINGWORDS = ['addition','breath','central','decorator','earthquake','fraction','guess','ignore','judge','kept','ledge','mention','narrate','often','palm','royal','shear','trouble','understand','vocal','wander'] 
#constant, list of spelling words

Index = random.randint(0, len(SPELLINGWORDS)-1) # choses a random number between 0 and the last number of items in spelling words
Word = SPELLINGWORDS[Index] # uses the random number as a index and picks a random word from list

Correct = [] # empty list to later on store the correct guesses of user
Incorrect = [] # empty list to later store the incorrect guesses of user
tries = 10 # allows the user to see how many tries they have using the flower visuals

def display(tries): # funtion that calls the stages of the hangman visuals depending on how many times the user has
    # incorrectly guessesd
    stages = ["""                                                   
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                    .-=====-.                     
                  -+=-------=+-                   
                 +=-----------=+                  
                :+-------------+-                 
                ==-------------==                 
                .*-------------*.                 
                 :+----------=+:                  
                   -=+==-==+=-                    
                      .:::.                       
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  

""",
              """                                                   
                      ::::                        
                     .:  :.                       
                     -    -                       
                     -    -                       
                     -    -                       
                     -    -                       
                     -    -                       
                     =:--:+                       
                  :=++=---=++=.                   
                .++-----------+=                  
                *=-------------+=                 
               :+---------------#                 
               -+---------------#                 
                *=-------------+=                 
                .+=-----------+=                  
                  :=++=---=++=.                   
                     .:---:.                      
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  

""",
              """                                                   
                                                  
                       -:-                        
                      -   -                       
                      -   -                       
      ::::           .:   :.                      
      -   .:::       -    .:                      
       ::     .::    -    .:                      
        .::      ::. :.   :.                      
           ::.     .::=---+:                      
             .::.  =++=----=+=:                   
                .+*-----------=+                  
                :*-------------=*                 
                +=--------------*:                
                ==--------------#                 
                 *=------------+=                 
                  =+---------=+:                  
                    -=++++++=:                    
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  

""",
              """        :                        
                       .- -.                      
                       -   -                      
                       -   -                      
        -...::.       .:   :                      
        .-    .::.    .:   :.                     
          ::      ::  .:   -                      
            .:.     .:.=.::=                      
              .::.  :=++====++-                   
                 .:*=----------+-                 
    .::.:.........*=------------+-                
   -.             *--------------*                
    .::::....:...:*-------------=+                
                  :+-----------=*.                
                   .=+=------=+-                  
                      :-===--:                    
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  

""",
              """                                                   
                       -::                        
                      -  .:                       
                      -   -                       
      .:::.          .:   -                       
      :.  .:::.      :    :.                      
       .:     .::    -    :.                      
         ::.     .:. :.   -                       
           .::     .:-+---+:                      
              :::..=+=-----=+=-                   
        .....:...=*-----------=+                  
  :::....       :*-------------=+                 
 ::             ==--------------#                 
   .::::::.:---:=*--------------*                 
       .::..     =+-----------=*.                 
    .::        ::::++-------=+=                   
  .:.     ..::.     .-=====-:                     
  ::..::::.                                       
                                                  
                                                  
                                                  
                                                  
                                                  

""",
              """                                                   
                                                  
                        :::                       
                       -  ::                      
                       -   -                      
        :.::.         .:   -                      
        ::   .::.     ..   -                      
         .:.    .::   :.   -                      
           .:.     .:..:   -                      
              ::.    -=+===+=-                    
                .::-+=-------=+=                  
      .:::.......:=+-----------=*                 
   .:.            *-------------+-                
    :..........:::*-------------==                
          .:::.   ==------------*                 
       .::.      .-++=--------++.                 
     ::      ..::-.  -=+++++=-.                   
    ::.....::. .:    .:                           
              :.    :.                            
             -.   ::                              
            :.  ::.                               
            ::::                                  
                                                  
                                                  
                                                  

""",
              
              """                                                   
                                                  
                         :::                      
                        :. .:                     
                        -   -                     
          :...:.        -   -                     
          .:    .:.     -   -                     
            ::     .:.  -   -                     
              ::.    .:.-.::=                     
                .::. .-++====+=-                  
            ........++----------+.                
      .:.....      -+------------*                
     .-.           +-------------+:               
        ..:.::---::-+------------*                
          ::..      ++---------=+.                
       .:.      ..:-. -=+===++=:                  
      .:  ....:. ::    -= .. -                    
       ...      :.   .: -    -                    
               -    :.  -    -                    
              -   ::    .:  :.                    
              :::.       -  -                     
                         .::                      
                                                  
                                                  

""",
              """                                                   
                     .::.                         
                     -  -                         
                     :  .:                        
       ::..::.      :.   -                        
        :.   .::.   :    -                        
         .:.    .:: :.   -                        
            ::.    :-=--==:                       
              .:.:=+=-----=+-                     
     ...........:*----------=+                    
   :.           +------------==                   
   .:........:::*------------=-                   
        .:...   .*----------=*                    
     .::.      .--=+=-----=+-..:.                 
    :.    ...:.:    =+---+-.    .::               
    ...:..   ::    : -   -  ::.    ::             
            :.   :.  -   -    .:..   :            
           :.  .:    -   -        ....            
           :..:      .. .:                        
                      :.:                         
                                                  

""",
              """                                                    
                       :::                        
                      :.  -                       
                      -   -                       
       :.::.          -   :.                      
       :.   :::.      :   .:                      
        ::     .::    :   .:                      
          ::.     ::. -   :.                      
            .::     :=+===+-:                     
               .:::++-------=+=.                  
      .:::::.::::-*------------*.                 
  .:..           *--------------*.:..:.::::.      
  .:....      ..:#--------------*           .::   
       ...:--::. +=------------+-        ...::    
      .::.       :#+----------++-::::.:..         
    ::.      .::-: .=++====++-   .::              
   -.   ...:.. :.    -=.:..-::.     ::.           
    ::..     .:    .: -    -  .::     .:          
            ::    :.  -    -     .::.   -         
           .:   ::    :    -         .:::         
           -..:.       -  :.                      
                       ::.:                       
                         .                        
                                                  

""",
              """                                                    
                                                  
                      .-::                        
                      -  :.                       
                     .:   -                       
      :::.           -    -                       
      -   .::.       -    -                      
       :.     ::.    -    -                       
        .::      ::  -    -              .:::.    
           ::.     ::-----+.       .:::...   =    
             .::. .=++-----=+=. :::.       ::     
          .......++-----------++       .::.       
  :::::.........=+-------------== ..:::           
 =              *---------------#-:.......::::.   
  .::::....:---:*=-------------=*            .-   
       .::..     *=-----------=#-....:..:.:::.    
    .::.       .:==+=--------+=.::.               
  ::.      .:::-:   -+++++=*+     .::             
  -...::::.  .:     -.-    -.::      ::           
            ::    .:  -    -   .::     ::         
           :.    :.   -    -      .::.. ::        
          ::   ::     =   :.          ...         
          -:::.       :.  -                       
                       -.-.                       
                                                  

 """,
              """                                                   
                                                  
                       ::.                        
                      :. :.                       
                      -   -      .::              
        .:.:.         -   -    .:. :.             
        .:   ..:.     :   -  .:   .:              
          ::    .::   :   - :.   .:               
            ::     .: - . =:    :. .:.:...::      
              .:.   -++===+==..-:..      ::       
            ......=+---------=*.     ..:.         
    .::.....    .-+-----------=+..:::.            
    -.           +=------------*...........:.     
      ..:..:---::-+-----------=+        ...:.     
        .:..      ++---------=+-:....:...         
     .:.      ..:-. -=++=+++=.  .::               
     =......:. :.    --   .:::     .:             
      ..      :    .: -   .:  .:.    ::           
             -    :.  -   :.     .:...::          
            -  .:.    :.  -                       
            .::.       -  :                       
                        ::


                """]
    return stages[tries] # returns the certain visual depending on what number tries is on

 

def has_won(): # function that is carried out if player has guessed the word
    Won = True #won is initally set to true
    for ch in Word: # for loop will check each character in the chosen spelling word
        if ch not in Correct: #if that character is not in the list Correct
            Won = False # set to false untill all characters are in the list 
            
    return Won # return won when all characters in list (won set to true)

 

while len(Incorrect) < 10 and not has_won(): # main game 
    print("Let's play hangman !!") # while loop continues until length on incorrect list exceeds 10 and if the user has won
    for ch in Word: 
        if ch in Correct:
            print(ch, end=" ") #replaces _ with guessed character in the word
        else: # end=' ' allows for a space after the characters 
            print ("_", end=" ") #as the initial list for correct is empty that characters in the word are replaced with _
            
    print(display(tries)) #displays which current life they are on shown with flower and fallen petals
    print()# space
    print("Incorrect:"," " .join(Incorrect)) # incorrect guesses are shown here, joins the list in incorrect
    print("You only have", 10 - len(Incorrect), ("lives left")) # give a numeric visual of how many lives they have left

    guessed = False
    Guess = input("Enter a guess: ").lower() # allows the user to input their guess
    while not len(Guess) ==  1 or not Guess.isalpha(): # whille loop, if the guess is more than 1 character and is anything
                                                        #but a letter
        print("Invalid guess - enter a single letter") #outputs what they did wrong
        Guess =  input("Enter a guess: ").lower() # allows user to input their guess again
        # loop will end when correct character is inputted 

            
 
    if Guess in Word: # if the users guess is spelling word
        if Guess not in Correct: # only appends the guess if the guess hasnt been used 
            Correct.append(Guess)  # adds the users guess into the correct list
        else:
            print()
            print("== Dont repeat letters== ")

    else: # is the guess is not in the word
        if Guess not in Incorrect: # appends the list Incorrect is guess is not in list
            Incorrect.append(Guess) # adds the users guess in to the Incorrect list
            tries = tries - 1 #tries is decreased by one allowing the visul display to change
        else:
            print()
            print("== Dont repeat letters ==")

	 
 

if has_won(): #when won = true  
    print("You’ve guessed the correct word and it only took", len(Incorrect)+len(Correct), "tries !!") # user is told they are won
    # and how many tries it took for them to guess the word
    print(Word)# the word without the spaces are printed for the user to see

else:
    print(display(0)) #displays index 0 showing a visual display that the user has lost and did not win the game
    print("Out of tries, the word you were guessing was","'" +Word+"'", "try again next time") #tells user they have lost and what the word they were guessing is
    # lets them down gently lol
    
