 Hangman is an enjoyable game against the computer! This is where you'll try to guess a secret word, letter by letter, while the computer tries to do the same be cautious Every wrong letter draws the  hangman one step closer to his fate. 
 
 image 
 
 ## purpose 
 
Entertainment: Hangman is primarily created as a source of fun and entertainment. It can be an engaging game that challenges players' word-guessing abilities and provides a recreational activity for individuals or groups.

Education: Hangman can be used as an educational tool to enhance language skills, particularly vocabulary, spelling, and word recognition. Teachers or language instructors might create Hangman games to make learning more interactive and enjoyable for students.
 
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

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
