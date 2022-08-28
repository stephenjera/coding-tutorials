from game_gui import *
import random

class Hangman(App):
    # Global instance variables
    attempts = 9
    total_guesses = 0
    games_won = 0
    guessed_letters = []
    play_again_state = False

    def __init__(self):
        super().__init__()
        self.word_to_guess = self.get_word()
        self.correct_letters = list('_'*len(self.word_to_guess))

        self.title('Hangman')

        # ============ frame_left ============
        self.label_guesses_var = tk.StringVar(value='Total Guesses: 0')
        self.label_guesses = ctk.CTkLabel(master=self.frame_left,
                                           textvariable=self.label_guesses_var)
        self.label_guesses.grid(row=2, column=0, pady=10, padx=20)

        self.label_games_won_var = tk.StringVar(value='Games Won: 0')
        self.label_games_won = ctk.CTkLabel(master=self.frame_left,
                                            textvariable=self.label_games_won_var)
        self.label_games_won.grid(row=3, column=0, pady=10, padx=20)

        # ============ frame_info ============
        # Overwriting the label defined in App
        self.label_info_1 = ctk.CTkLabel(master=self.frame_info,
                                                text='Type a letter in the entry box,\n' +
                                                    'then press <enter> or hit submit',
                                                height=100,
                                                corner_radius=6,  # <- custom corner radius
                                                fg_color=('white', 'gray38'),  # <- custom tuple-color
                                                justify=tk.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky='nwe', padx=15, pady=15)

        #self.entry_text = StringVar()
        vcmd = (self.register(self.validate), '%P')
        self.entry = ctk.CTkEntry(master=self.frame_right,
                                            width=120,
                                            validate='key',
                                            validatecommand=vcmd,
                                            placeholder_text='Enter your guess here')
        self.entry.focus_set()
        self.entry.grid(row=8, column=0, columnspan=1, pady=20, padx=5, sticky='we')
       
        # Update user
        self.label_output_var = tk.StringVar(value='Output goes here')
        self.label = ctk.CTkLabel(
            master=self.frame_info, textvariable=self.label_output_var)
        self.label.grid(row=2, column=0, pady=10, padx=20)

        # Show correct letters guessed
        self.label_word_var = tk.StringVar(value='')
        self.label = ctk.CTkLabel(
            master=self.frame_info, textvariable=self.label_word_var)
        self.label.grid(row=4, column=0, pady=10, padx=20)

        self.label_guessed_letters_var = tk.StringVar(value='Guessed letters: ')
        self.label_guessed_letters = ctk.CTkLabel(master=self.frame_info,
                                            textvariable=self.label_guessed_letters_var)
        self.label_guessed_letters.grid(row=5, column=0, pady=10, padx=20)

        # ============ frame_right ============
        self.submit = ctk.CTkButton(master=self.frame_right,
                                    text='Submit',
                                    border_width=2,  # <- custom border_width
                                    fg_color=None,  # <- no fg_color
                                    command=self.check_guess)
        self.submit.grid(row=8, column=1, columnspan=1,
                         pady=5, padx=5, sticky='we')
    
        self.start_game()

    @staticmethod
    def get_word():
        """Get list of words to guess from text file""" 
        with open(r'words.txt', 'r') as file:
            words = [line.strip() for line in file]
        #print(len(words))
        word = words[random.randint(0, len(words) - 1)]
        #print(word)
        return word

    @staticmethod
    def validate(entry_input):
        """
        Takes the entry input and validate it's the correct type 

        Args:
            entry_input (any): input from entry box

        Returns:
            bool: valid or invalid entry
        """
        if len(entry_input) == 0:
            # empty Entry is ok
            # required to change the character 
            return True
        elif len(entry_input) == 1 and entry_input.isalpha():
            # Entry with 1 letter is ok
            return True
        else:
            # Anything else, reject it
            return False

    def start_game(self):
        """Set up parameters to start the game"""
        if self.play_again_state:
            self.play_button.destroy() # only destroy if created 

        self.submit.configure(state="normal")
        
        self.label_output_var.set('Guess the word')
        self.label_word_var.set(self.correct_letters)

        self.bind('<Return>',lambda event:self.check_guess())

        self.label_word_len = ctk.CTkLabel(master=self.frame_info,
                                            text=f'Word length {len(self.word_to_guess)}')
        self.label_word_len.grid(row=1, column=0, pady=10, padx=20)
        self.label_guessed_letters_var.set(f'Guessed letters: ')

    def play_again(self):
        """ Set up parameters to play the game again"""
        self.submit.configure(state="disabled")
        self.play_button = ctk.CTkButton(master=self.frame_info,
                                    text="Play again?",
                                    command=self.start_game)
        self.play_button.grid(row=3, column=0, pady=10, padx=20)

        self.unbind('<Return>')

        self.attempts = 9

        self.correct_letters = list('_'*len(self.word_to_guess))
        self.guessed_letters = []
        self.word_to_guess = self.get_word()
        self.play_again_state = True

    def check_guess(self):
        """Check the user guess and update interface based on user actions"""
        # Make sure a space is ignored
        if str(self.entry.get()).isalpha():
            self.user_input = str(self.entry.get())

            # Stop same letter counting as another guess 
            if str(self.guessed_letters).find(self.user_input) == -1:
                self.guessed_letters.append(self.user_input)
                self.label_guessed_letters_var.set(f'Guessed letters: {", " .join(self.guessed_letters)}')

                # Process guess if user has attempts left
                if self.attempts > 0:
                    # Check letter guessed is in word to guess
                    if self.word_to_guess.find(self.user_input) != -1:
                        #print(f' got word {self.word_to_guess.find(self.user_input)}')
                        msg = f'{self.user_input} is in the word.'
                        self.total_guesses += 1
                        self.label_guesses_var.set(f'Total Guesses: {self.total_guesses}')

                        # Get all indices for correct letter guessed and replace underscores  
                        indices = [i for i, c in enumerate(self.word_to_guess) if c == self.user_input]
                        for i in indices: self.correct_letters[i] = self.user_input
                        self.label_word_var.set(self.correct_letters)

                        # The game is won once all underscores have been replaced 
                        if str(self.correct_letters).find('_') == -1:
                            self.games_won += 1
                            self.label_games_won_var.set(f'Games Won: {self.games_won}')
                            msg = f'The word is {self.word_to_guess}.'
                            self.play_again()

                    # Prevent user having to hit enter to find out if they have lost
                    elif self.attempts == 1:
                        # if they haven't won when attempts is 1 they've lost
                        msg = f'You Lost! you have {self.attempts-1} attempt left.\n The word is {self.word_to_guess}.'
                        self.play_again()

                    # Process incorrect guess
                    elif self.word_to_guess.find(self.user_input) == -1:
                        print(f'not got word {self.word_to_guess.find(self.user_input)}')
                        self.attempts -= 1
                        self.total_guesses += 1
                        self.label_guesses_var.set(f'Total Guesses: {self.total_guesses}')
                        msg = f'{self.user_input} is not in the word. You have {self.attempts} attempt left.'
                    else:
                        msg = 'Something went wrong!' # Should never reach here 
            else:
                msg = 'Enter a different letter' 
        else:
            msg = 'Spaces are invalid, please enter a letter'
            #print(msg)

        self.label_output_var.set(msg) # Update user


if __name__ == '__main__':
    # #Run the game 
    game = Hangman()
    game.mainloop()
