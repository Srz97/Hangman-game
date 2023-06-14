Online Hangman is an enjoyable game against the computer! This is where you'll try to guess a secret word, letter by letter, while the computer tries to do the same and every wrong letter draws the  hangman one step closer to his fate. 
 
 image 
 
 ## Purpose 
 
Entertainment: Hangman is primarily created as a source of fun and entertainment. It can be an engaging game that challenges players' word-guessing abilities and provides a recreational activity for individuals or groups.

Education: Hangman can be used as an educational tool to enhance language skills, particularly vocabulary, spelling, and word recognition. Teachers or language instructors might create Hangman games to make learning more interactive and enjoyable for students.
 
## How To play

* The game begin by greeting the user with a friendly message.
* Before the Game procceds it requests the user for their name.
* You are then provided with two options either to have a look at the rule book or  to start the game.
* You are then provided with two options either to have a look at the rule book or  to start the game.
### When you select to play 
1. You'll see a series of dashes on the screen, representing the letters of the word.
2. Guess one letter at a time by clicking or tapping on the corresponding letter on the on-screen or keyboard.
3. If the guessed letter is in the word,For example, if the word is "apple" and you guess "p," the dashes will update to show "_ _ _ p _".
4. If the guessed letter is not in the word, you'll receive a notification, and one part of the hangman figure will be drawn. Be careful! You have a limited number of incorrect guesses before the hangman figure is completed.
6. Continue guessing letters until you either guess the entire word correctly or the hangman figure is fully drawn.
7. If you guess the word correctly before the hangman figure is completed, you win!
8. If the hangman figure is completed before you guess the word, you lose.
9. After the game ends, you may have the option to play again and try to beat your previous score.



## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
