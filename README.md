# CIS434-Group12
Recreating Snake Game in Python; PyhonPythonGame

####Aidan Z
####Toral Z
####Derek W


V1.0.0 Base game is working
  features to work on next:
    -main menu
    -difficulties
    -live score
    -customization menu in main menu to change colors of things
    
V1.0.1 Added functionality, snake can not turn 180 degrees
  todo:
    -add menu() (Aidan, Derek)
    -Score (toral)
    
V1.0.2 Started framwork for gamestate logic to keep the while loop organized
      -Discussed the coding goal of keeping the main loop clean, and using a OOP and method based approach
      
V1.0.3 Large Update, Menu was added by Aiden and live score by Toral
      -After that menu was moved into its own function and the button class was created with hover funtionality
      -Toral also created a score class
      -There was some merging errors since Toral and Derek were editing at the same time but they are all resolved
      -Some refactoring, colors are now at the top, two_player groundwork started, main game objects like font, surface and dimensions are global. buttons list for quick drawing
      
V1.0.4 Persistant data storage setup using python shelve library, used to implement highscore
      - minor modification to score class to be able to use it for multiple purposes
      - Delay was causing turning issues so it has been reduced, may get rid of it entirely
      - Event loop was bypassing the turnback check when multiple arrow keys were pressed and allowing the player to suicide (fixed)
      
      
Current Bugs:
      -There appears to be a hidden column that the snake can turn into at index x = -1 despite there being 20/20 columns on screen


progress report:
      - add two player race mode and two player melee mode
      - get started on final report
      - obstacle fruits
