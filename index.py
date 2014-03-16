import sys
import traceback
import random

from exceptions import InvalidInputError, InvalidSelectionError
from helpers import string, num


class app():
    
    choices = {
        1: 'rock',
        2: 'paper',
        3: 'scissors',
        4: 'shotgun!'
    }
    
    weights = {
        1: 10,
        2: 10,
        3: 10,
        4: 10
    }
    
    rounds = 0
    
    user_win_count = 0
    computer_win_count = 0
    
    user_consec_win_count = 0
    computer_consec_win_count = 0
    
    def main(self):
        choice = input("""
So you want to challenge me at rock, paper, scissors; do ya?? Well choose an option:
            
[1] Rock
[2] Paper
[3] Scissors
            
: """)
            
        if(num.is_int(choice) is False):
            # Not a valid value
            raise InvalidInputError('Please actually enter a number')
        
        choice = int(choice)
        
        if(choice not in dict((i, self.choices[i]) for i in self.choices if i <= 3)):
            # Not a valid choice
            raise InvalidSelectionError('Please select a valid option from 1-3')
        else:
            # if all is okay let's get the computers choice
            computer = self.get_computer_move(choice)
        
        # Judge who wins
        if(computer == 4):
            
            print('Grrr....SHOTGUN TO THE FACE!!!')
            
            self.computer_wins()
        elif(computer == 1):
            
            print('I choose rock')
            
            if(choice == 1):
                self.draw()
            if(choice == 2):
                self.user_wins()
            elif(choice == 3):
                self.computer_wins()
        elif(computer == 2):
            
            print('I choose paper')
            
            if(choice == 1):
                self.computer_wins()
            if(choice == 2):
                self.draw()
            elif(choice == 3):
                self.user_wins()           
        elif(computer == 3):
            
            print('I choose scissors')
            
            if(choice == 1):
                self.user_wins()
            if(choice == 2):
                self.computer_wins()
            elif(choice == 3):
                self.draw()
                
        self.rounds += 1;
        
        print("Rounds: " + str(self.rounds))
        print("User wins: " + str(self.user_win_count) + " ( Consecutive: " + str(self.user_consec_win_count) + " )")
        print("Computer wins: " + str(self.computer_win_count) + " ( Consecutive: " + str(self.computer_consec_win_count) + " )") 
                
        answer = input('Soooo...wanna play again? (yes|no) ')
        if(string.is_string(answer) is False):
            # Throw exception here too  
            raise InvalidInputError('You need to enter yes or no')
        elif(answer == 'no'):
            raise KeyboardInterrupt
        elif(answer != 'yes'):
            # Throw exception that the user is a dumbass
            raise InvalidSelectionError('You need to enter yes or no')   

    def get_computer_move(self, user_choice):
        """
        This gets the computers move
        
        This works by weighting all choices apart from the users current choice and 
        "shotgun!" by 10x and then weighting shotgun by the number of times the user has won, 
        so as to get more likely the more the user wins, a.k.a the computer gets pissed off.
        
        It will weight the current users choice by 2x.
        
        After all this it will pick a random choice from the set.
        """
        
        weights = self.weights;
        weights[user_choice] = 5
        weights[4] = self.user_consec_win_count
        
        return random.choice([k for k in weights for x in range(weights[k])])
    
    def draw(self):
        # no increment of scores this time
        print('Hmm, no one won. Let\'s try again.')
    
    def computer_wins(self):
        self.computer_win_count += 1
        
        self.user_consec_win_count = 0;
        self.computer_consec_win_count += 1;
        
        print('I HAVE BEATEN YOU PUNY HUMAN!!!')
    
    def user_wins(self):
        self.user_win_count += 1
        
        self.user_consec_win_count += 1;
        self.computer_consec_win_count = 0;
        
        print('Hmmm, it may seem as though you beat me; let\'s try again shall we?')


application = app()

while(True):
    try:
        application.main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout));
        input('Error Printed')