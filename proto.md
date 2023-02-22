
# This file describes all the messages sent between server and client.
The messages are always json objects, and are read from the socket line by line. This works, because if there would be a newline in the data sent, it would be escaped with a "\n".

In Python you can use:
```
sock_file = sock.makefile()
for message in sock_file.readline():
	message_dict = json.loads(message.strip()) #.strip() to remove the newline at the end
	# handle the message
```
to read a socket line by line.

Every message has a field: "msg", that indicates what type a message is. All used message-types are listed below.

## player-list
- to inform the client, about all the players that are currently in the matchmaking lobby.
- always from server to client
- sent to every new client that connects, to every client, when the list of players in the matchmaking lobby changes.
- contains a field "players" with a list of player objects

## set-name
- to inform the server about the name of a client
- always from client to server
- sent when a user presses the button to set its name
- on the server when one such message is received, a new player is added to the list ob players in the matchmaking lobby (and a player-list message is sent to all clients)
- has a field "name", with the name of the player

## match-req
- sent from client to server, when a user selects another player to play a game with.
- sent from server to the client, the client the message came from wants to play a game with.
- has a field "player_id" with the id of the player a match wants to be made.
- when received by a client, a msg and a button should appear for every match-req message. when pressing one, send a match-ack msg to that client, and a match-deny msg to all others.

## match-req-cancel
- sent when clicking on a cancel button, because the other player is not responding
- sent from server to client. just forwarded to the client with id that is in the player_id field
- has a field "player_id"

## match-ack
- sent from client to server, when user selects a player to play with.
- has a field "player_id"

## match-deny
- sent from client to server, when user does not want to play with another player
- has a field "player_id"

## game-start
- sent from server to both clients after a match-ack is received
- fields:
	- boats: object of how many boats of what category. like this: {"1x1": 2, "1x3": 1, "aircraft-carrier": 1}
	- grid-size-x: how wide the grid is
	- grid-size-y: how high the grid is

## game-cancel
- when the other player takes to long to do something (there is a button for canceling a game, when pressed this msg is sent, and client goes back to the lobby)
- puts both players back into the lobby
- sent from client to server and server forwards it to the other client in the game
- when received by a client, gui goes back to the lobby and a msg-popup that the other player canceled the game is displayed

## game-place
- sent from client to server when the user placed all his ships and is presses the button "Done Placing Ships"
- fields:
	- one for every type of ship
	- like this: {"1x1": [[1,2, <rotation>],[3,4, <rotation>]], "1x3": [...]}. rotation is a number from 1 to 4

## game-place-invalid
- sent from server to client, if the placement of ships is not correct
- the client then has to do the placement again

## game-do-hit
- sent from server to client, if it's this client's turn to hit
- sent again, if the hit was a success, with information about the fields around the hit, when do-hits-around is true in the config

## game-hit
- sent from client to server
- fields:
	- x: x-coordinate of the hit
	- y: y-coordinate of the hit

## game-hit-success
- sent from server to either client
- client has to cross out that coordinate
- fields: x, y

## set-score
- sent from server to either client, to update the score
- fields: score




