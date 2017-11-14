# SuperHajusSudoku

##Program description

Program "SuperHajusSudoku" consists of three main modules:

Client- where all the client side of communication is located

Server- where all the server side of communication is located

Common- where all the common part of files are located, for server and client side both


## How to use the program:

### First of all we have to start server side. For that it's needed to open main program file SuperHajusSudoku/server/main.py.

That will open the GUI, where it is needed to specify two parameters:

 1. Port number which is by default 7777
 2. Server host number which is by default 127.0.0.1, as a local ip address
 3. Then have to push the button "Start server"

It will create the Sudoku game server, in where, it is possible to start games


### Secondly must open the client side, as it is multiplayer game, then that point can be done in two variations

If there is only one client, then you must open the game as well:

1. Specify the same port number, as you added for server
2. Insert the same ip address, as server has
3. Then have to fill the blanks
   - (insert new game) where the new game name must be specified
   - (insert the max players number) have to enter the number how many players can play that current game

4. Under Available games should appear: the name of the game
5. In the blank - (insert game id) you have enter the name from list of Available games.

For example:
- create new game: new_sudoku
- max players: 3
- Available games: new_sudoku
- Join a game inserting id: new_sudoku

6.If all the blanks are filled then push {Join game}
7.Finally the sudoku game_field will appear and you can start to play



