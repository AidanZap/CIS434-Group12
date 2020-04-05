## CIS434-Group12
Recreating Snake Game in Python; PyhonPythonGame

#### Aidan Z
#### Toral Z
#### Derek W


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
      -hidden column, missing blocks during crossover removed  
      -snake/cube color conflict removed  
      -no up on start fixed  
      -input being ignored because it was put in to fast improved, so snake reaction time improved  
      
   ###### next step:  
      -dynamic variable means a lot more parameters being passed to objects like snake, cube and score so all variables must be
      condensed into one game_var object and passed in one go to improve readability  
      -game mode/ user settings screen(s)  
      
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

#### v1.1.0
    -First working settings menu, all buttons change variables
    -Fixed settings menu bugs
    -Updating board and fruit settings apply properly in-game

##### Current Bugs:  
      - None  

##### progress report notes:  
      - add two player race mode and two player melee mode  
      - get started on final report  
      - obstacle fruits  
      - two player collision handling
      - end screen pop up / hi score implementation
      
