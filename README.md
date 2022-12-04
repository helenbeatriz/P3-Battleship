<h1 align="center"> Battleships Game </h1>

[View the live project here](https://battleshipprojct3.herokuapp.com/)

<h2> How to Play </h2>
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
I was planning to display on the board each one of the user guesses which I did.

Initially, I wanted to create a interactive game with other user scores, names but due to the lack of time it became out of my scope. 
   

## Features

   ### Existing/current Features
      
-   __Welcome Screen__

    - A  ASCII art images of a shit is displayed for the user 
    - Then user can see the rules section display and have access to the board of the game

      ![Navbar]()

-   __Rules__

    - The rules of the game are display and provided step by step for the user to know how it needs to be played. 

      ![Navbar](/media/rules.png)
      
-   __What To Expect From The Game__

    - Once user starts the game, a board is displayed.
    - The board displayed only contains '|' that sinalize the spaces that the user did not insert to play. 
    - User is required to select a row number (1-8) and a column (A-H). 
    - If user inserts an invalid command, an error message will be displayed.
    - If successful, a green 'X' and a message 'Hit' will be displayed. 
    - If unsuccessful, the user will see that message 'MISS!' and a '-' displayed. 

      ![Navbar]()
      
## Flow Chart
 The flow of the game was structured to work in responsiveness to user input using features such as if-elif-else statements, while loops and for loops. This also enable the user input validation checks to be visually clear before the code was written.
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
   - Mozilla FIrefox - Version 99.0.1 (64-bit)
   - Safari - Version 13.1.3 (15609.4.1)

- Everything was working accordingly.    

### User Testing

- User was able to play the game and the game is responsive based on the user inputs. 
### Resolved Bugs

- I coudnt get my game working because my Gitpod wasnt updated so replying on stack and used git commands and resolved the bug.
- I was getting an Error and not able to open the game because of variables that were not being called. 
## Deployment

This game was deployed through Heroku. The live link is [here](https://battleshipprojct3.herokuapp.com/)

- Fork/clone this repository
- Create a new app on Heroku
- Ensure that the buildpacks are set to 'Python' and 'NodeJS' (the Code Institute template provides code for the terminal to display the game)
- Link the app on Heroku to the repository
- Click on the 'Deploy' button.