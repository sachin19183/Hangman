# This is a hangman project. User shall be presented with blanks represnting a random word
# User needs to guess each alphabet within a stipulated no. of turns to win the game.
import random
import hangman_art as ha
import hangman_words as hw

# Create a list of random numbers
#word_list= ['flabbergasted',"pneumonia","chrysanthemum","xylophone","ambidextrous","rhythm","eccentric","epiphany","kaleidoscope","dystopia","gazebo","quinoa","zucchini","ostacize","synchronize","haaphazard","juxtaposition","pyrotechnics","chameleon"]
#tough_word_list= ["Antidisestablishmentarianism","Hieroglyphics","Sphygmomanometer","Pterodactyl","Onomatopoeia","Zephyr","Ecclesiastical"]
print(ha.logo)
chosen_word =random.choice(hw.word_list)
#chosen_word = "yoyoyoyo"
display_word=['-']*len(chosen_word)
no_chances=6
print(chosen_word)
print(display_word)
while no_chances > 0:
    user_input= input("Guess a letter: ").lower()
    found= False
    for i, ch in enumerate(chosen_word):
        if user_input== ch:
            display_word[i]=ch
            found = True
    print(display_word)
    if found == False:
        no_chances-=1
    #print(no_chances)
    print(ha.stages[no_chances])
    if '-' not in display_word:
        print("You win")
        break
if '-' in display_word:
    print("You Loose")