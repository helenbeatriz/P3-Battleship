<h1 align="center"> Battleships Game </h1>

[View the live project here](https://battleshipprojct3.herokuapp.com/)

<h2> How to Play </h2>

![Game](/media/gif.gif)

    Our board consists of 8 rows and 8 columns.
    The user goal is to find where the ships are.
    After every input you type a row and a column letter into the game, then user has to press enter to continue.
    Whenever the user gets it right an 'X' will be displayed.
    Whenever the user get it wrong an '-' will be displayed.


## Index - Table of Contents
*  [Scope](#scope)
*  [Features](#features)
*  [Design](#design)
*  [Technologies and Support](#technologies-and-support)
*  [Testing](#testing)
*  [Deployment](#deployment)

## Scope

I wanted to create a functional, simple battleships game, which is fully responsive and interactive. 
I was planning to display each user guess on the board which I did.
Initially, I wanted to create an interactive game with other user's scores and names but due to the lack of time it was removed from scope. 
   

## Features

   ### Existing/current Features
      
-   __Welcome Screen__

    - An ASCII art image of a ship is displayed for the user.
    - Then, the user can see the rules section display and have access to the board of the game.

-   __Rules__

    - The rules of the game are displayed and provided step by step for the user to know how the game is played. 

      ![Navbar](/media/rules.png)
      
-   __What To Expect From The Game__

    - Once user starts the game, a board is displayed.
    - The board display only contains '|' which identifies the spaces that the user did not insert to play. 
    - User is required to select a row number (1-8) and a column (A-H). 
    - If user inserts an invalid command, an error message will be displayed.
    - If successful, a green 'X' and a message 'Hit' will be displayed. 

      ![Hit](/media/hit.png)

    - If unsuccessful, the user will see the message 'MISS!' and a '-' displayed. 

      ![Miss](/media/miss.png)
      
## Flow Chart
 The flow of the game was structured to work in responsiveness to user input using features such as if-elif-else statements, while loops and for loops. This also enables the user input validation checks to be visually clear before the code was written.
      ![Navbar](/media/diagram.png)

   ### Potential Future Features
   
- User name input
- APIs
- A leaderboard
- Using Google Cloud APIs, I could store the user's name into a database.
- A 'play again' button
- With additional time, I would have done way more. 

## Technologies and Support

### Languages Used

-   [Python](https://en.wikipedia.org/wiki/python)

### Programs

-   [ASCII Art Library](https://pypi.org/project/art/)
      - Website Helped me with 'Battleships' image/art for the welcome text.

-   [Coloured text in Python(stackabuse)](https://stackabuse.com/how-to-print-colored-text-in-python/)
      - Applying colors to my project. 

-   [Unexpected unident error(stack overflow)](https://stackoverflow.com/questions/10239668/indentationerror-unexpected-unindent-why)
      - Referenced this post to help me work through a challenging bug regarding some of my indentation which was breaking the entirity of my code.

-   [Try except statement(Python Basics)](https://pythonbasics.org/try-except/)
      - Helped me realise that I had forgotten to close off my try statements with the except function.

-   [Battleship function ideas](https://codereview.stackexchange.com/questions/tagged/battleship)
      - Referenced posts within the stack overflow community to help me build it.

-   [Youtube Tutorial](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=1200s)
      - Used as a reference to build the logic of the game. 

-   [Am I Responsive](https://ui.dev/amiresponsive)
      - Used to check if my game was responsive in different mobiles.


## Testing
    
### Browser Compatibility

- Testing was sucessful using those browsers:
   
   - Google Chrome - Version 100.0.4896.60 (Official Build) (64-bit)
   - Microsoft Edge - Version 100.0.1185.50 (Official build) (64-bit)
   - Mozilla Firefox - Version 99.0.1 (64-bit)
   - Safari - Version 13.1.3 (15609.4.1)

### CI Python Linter

I checked the app using Python validator provided by Code Institute. 
A warning ocurred due to the Ship ASCII art images but apart from that it passes the code verification. 
![Navbar](/media/codeinstitutepythonlinter.png)


### User Testing

- User was able to play the game and the game is responsive based on the user inputs. 
- Users was able to see the correct markers for 'hits' and 'misses', and was able to read visual prompts that were shown '-' and 'X'. 
- When the max amount of hits was reached, users experienced the 'end message' either congratulating or commiserating. 

### Resolved Bugs

- I coudnt get my game working because my Gitpod wasnt updated so replying on stack and used git commands and resolved the bug.
- I was getting an Error and not able to open the game because of variables that were not being called. 
- I had few errors related to data that was not being inserted properly and generating an error. 
- When user was inserting an empty command like just "enter" an error was being shown so I added ' or row in "" ' to the code to fix that.
## Deployment

This game was deployed through Heroku. The live link is [here](https://battleshipprojct3.herokuapp.com/)

## This is how you can deploy this project:

- Fork/clone this repository
- Create a new app on Heroku
- Ensure that the buildpacks are set to 'Python' and 'NodeJS' (the Code Institute template provides code for the terminal to display the game)
- Link the app on Heroku to the repository
- Go to Application Management.
- Generating and Downloading SSH Keys.
- Upload the SSH Public Key to Your Git Repository.
For Github.
- Copy the Repository SSH Address.
- Deploy Code from Your Repository.

### Credits and Acknowledgements

- Credit to various inspiration from code found in various posts on Code Institute groups on slack.
- Thanks to Daisy my mentor. 
- I would like to thank Harry Dhillon that is not my mentor but has always been there helping and supporting me whenever I needed. 
 