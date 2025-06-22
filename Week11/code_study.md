### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)
https://github.com/sparshg/py-games/blob/95c314eeea7827b64510d8bc2089d0771f0e0b9a/src/RockPaperScissors/game.py
I chose something that I felt would be easier to understand. I simply typed "Python games" into the search bar and looked for games that interested me.

1. What does the program do? What's the general structure of the program? 
This program is a graphical implementation of the classic game Rock, Paper, Scissors using Python and the Pygame library.
The user plays against the computer. The player selects one of the three options by clicking, and the computer randomly picks one as well. The game then displays the winner. The game loops continuously and only stops when you choose to exit.
---

1. Function analysis: pick one function and analyze it in detail:

- What does this function do?
For the function i chose winner(). The winner() function determines the outcome of the Rock-Paper-Scissors game
based on the choices made by the user (P1Choice) and the computer (P2Choice).
It returns a text message that states whether the result is a win, loss, or tie.

- What are the inputs and outputs?
Inputs:
No arguments passed directly into the function
Uses global variables:
P1Choice → Player’s choice (e.g., "rock")
P2Choice → Computer’s choice (e.g., "paper")

Output:
Returns a string, one of:
"Its a tie"
"User wins"
"Computer wins"

- How does it work (step by step)?
def winner():
     result = ""
     resultText = ""
-> Initializes two empty strings to hold the game result.

Step 1:
if P1Choice == P2Choice:
    result = "draw"
-> If both players chose the same item, it's a tie.

Step 2:
if((P1Choice=="rock" and P2Choice =="paper") or (P1Choice =="paper" and P2Choice =="rock")):
    result = "paper"
elif((P1Choice=="rock" and P2Choice=="scissors") or (P1Choice=="scissors" and P2Choice=="rock")):
    result = "rock"
elif((P1Choice=="paper" and P2Choice=="scissors") or (P2Choice=="scissors" and P1Choice=="paper")):
    result = "scissors"
-> These conditions check all win/loss combinations.
The function sets result to the winning item ("rock", "paper", or "scissors"), not directly to a player.

Step 3:
print("P1Choice {} P2Choice {} result {}", P1Choice, P2Choice, result)
-> Prints choices and the result to the console for debugging.
(Note: the formatting is incorrect here, it should use .format() or f-strings.)

Step 4:
if result == "draw":
    resultText = "Its a tie"
if result == P1Choice:
    resultText = "User wins"
elif result == P2Choice:
    resultText = "Computer wins"
else:
    resultText = "Its a tie"
-> Based on the earlier result, this part determines who made the winning choice.
Returns the appropriate result message.

Step 5:
return resultText
-> Outputs a string to display on the screen (e.g., "User wins")


1. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)
I was able to take away, for one, how to structure and organize my own code better, and also to refresh and deepen my understanding of the basics (like if, elif, else).
Additionally, I gained a better understanding of what concepts like event in pygame.event.get() actually mean behind the scenes.

1. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?
At first, I didn’t understand what these numbers meant:
mouserock = 125 + 150 > mousepos[0] > 125 and 225 + 150 > mousepos[1] > 225
mousepaper = 400 + 150 > mousepos[0] > 400 and 225 + 150 > mousepos[1] > 225
mousescissors = 850 > mousepos[0] > 700 and 375 > mousepos[1] > 255
mouseenter = 400 + 180 > mousepos[0] > 400 and 390 + 130 > mousepos[1] > 390
But then I realized that they are checking whether the mouse cursor is inside certain rectangular areas (like buttons), by comparing the mouse position with the coordinates and sizes of those buttons.



