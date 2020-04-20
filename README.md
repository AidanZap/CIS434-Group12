## CIS434-Group12
Recreating Snake Game in Python; PythonPythonGame

#### Aidan Z
#### Toral Z
#### Derek W

### To Run
    - Make sure Python is installed, Minimum version 3 recommended
    - From main directory(/CIS434-Group12)
    - pip install pygame
    - pip install shelve       (for highscore)
    - python main.py
    - Enjoy

### V2.0.0 Final Release
#### How to play.

##### Moverment: Arrow keys for player 1 and A,W,S,D for player 2

##### Classic Mode
    - Basic snake game, collect fruits (green cubes) without collding with yourself or the walls
##### 2 Player Race
    - Compete against a friend to see who can collect the most fruit in 60 seconds
    - Careful running into the opponent is an automatic loss and a head on collision is a draw
##### 2 Player Melee
    - No Fruit! Snakes automatically grow every 10 tiles, see who can survive the longest!
    
##### Additional Game Settings
    - Obstacles: spawns grey cubes that if ran into end the game
    - Board Size: change the size of the arena
    - Number of fruit: increase the number of fruit spawned to speed up the game
    - Borders: turn off borders to allow the snake to loop back to the other side of the arena

    
<br/>
### Previous Versions 
<br/>

#### V1.0.0 Base game is working  
    features to work on next:  
    - main menu  
    - difficulties  
    - live score  
    - customization menu in main menu to change colors of things  
    
#### V1.0.1 Added functionality, snake can not turn 180 degrees    
    todo:  
    - add menu() (Aidan, Derek)  
    - Score (toral)  
    
#### V1.0.2 Started framwork for gamestate logic to keep the while loop organized   
      - Discussed the coding goal of keeping the main loop clean, and using a OOP and method based approach  
      
#### V1.0.3 Large Update, Menu was added by Aiden and live score by Toral  
      - After that menu was moved into its own function and the button class was created with hover funtionality 
      - Toral also created a score class  
      - There was some merging errors since Toral and Derek were editing at the same time but they are all resolved  
      - Some refactoring, colors are now at the top, two_player groundwork started, main game objects like font, surface and dimensions are global. buttons list for quick drawing  
      
#### V1.0.4 Persistant data storage setup using python shelve library, used to implement highscore  
      - minor modification to score class to be able to use it for multiple purposes  
      - Delay was causing turning issues so it has been reduced, may get rid of it entirely  
      - Event loop was bypassing the turnback check when multiple arrow keys were pressed and allowing the player to suicide (fixed)  
      
#### V1.0.5   
   ###### features:  
      - dynamic object positioning and drawgrid, game can now be whatever size without damaging functionality, use for user settings  
      - Bottom banner  
      - almost all gameplay related variables are dynamic to allow for user customization  
      
   ###### bug fixes:  
      - hidden column, missing blocks during crossover removed  
      - snake/cube color conflict removed  
      - no up on start fixed  
      - input being ignored because it was put in to fast improved, so snake reaction time improved  
      
   ###### next step:  
      - dynamic variable means a lot more parameters being passed to objects like snake, cube and score so all variables must be
      condensed into one game_var object and passed in one go to improve readability  
      - game mode/ user settings screen(s)  
      
#### V1.0.6  
      - introduction of the game_settings class, used to unify all classes as a place to store global settings and variables for the application  
      - gs is used to reduce the parameter requirement for constructors and methods, and to keep them from being changed everytime there is a new variable  

#### V1.0.7  
      - snakes,snack and obstacles added to gs as lists  
      - new gs lists used to implement two player mode, modifications for user input added to snake.py, may need further improvement  
      todo:  
      - two player mode still needed to be added as an option on menu  
      - snake v snake collisions unhandled
      - score per snake

#### V1.1.0
    - First working settings menu, all buttons change variables
    - Fixed settings menu bugs
    - Updating board and fruit settings apply properly in-game
    
#### V1.1.1
    - Merged 2-player branch, working collisions in 2-player
    - each snake (1 and 2 player) are now their own fields in settings class
    - Individual player scores are tracked as their own fields in score class

#### V1.1.2
    - Working obstacles + borders
    - Introduced some bugs
    
#### V1.1.3
    - Melee mode finished, growth added
    - scr variable moved to gs
    - Endgame screen added, allows for replay, displays score and high score
    - For 2P modes colliding player score set to 0 to show clear winner
    
#### V1.1.4
    -Added timer for race mode
    -some bug fixes    
    
##### Current Bugs:  
      - None

##### progress report notes:  
      - add two player race mode and two player melee mode  
      - get started on final report  
      - obstacle fruits  
      - two player collision handling
      - end screen pop up / hi score implementation
      

      
