## Inspiration

I love to create and play games. My goal was to use my knowledge about python to create a game, to check the player's awareness about Covid-19 and how to prevent it's spread.

## What it does

A group of sprites, which represent people, are displayed on the screen. Each sprite can be in four different states:
 1. Prepared, with a mask and washed hands.
 2. Relatively unprepared with **no mask** but washed hands.
 3. Relatively unprepared with a mask but **no washed hands**.
 4. Completely unprepared with **no mask and no washed hands**.

The aim of the game is to make each sprite prepared. This can be done by clicking on a sprite and then pressing "w" (for washing hands), or "m", (for putting a mask on) to change its state. 

If you click a sprite, you cannot click another one unless you press escape, w or m.

## How I built it

I used Python for this project, specifically by using Pygame. By using Pygame I could create a UI and render sprites. I  created the sprites by myself using Aseprite, a pixel art tool. The project starts by rendering all of the sprites, randomly choosing their states. The project then waits for the player's click input, and the subsequent keyboard input for the letters. Based on these inputs, the project re-renders the board with the updated sprites.

## Challenges I ran into

I am relatively new to Pygame. Rendering the sprites was pretty challenging at first, but after some research (googling) I was able to figure it out. Finding a way to generate the boards was complex, as well. The hardest part was finding a strategy to detect the state of the sprite clicked and update its state after the click. 

It took some time, so this prototype of the game is not finished completely, but it has enough functionality to be a fun and interactive game.

## Accomplishments that I'm proud of

I'm incredibly proud of everything in this project. I am proud that I could bring it to the state its in, and create an interactive game in Pygame.

## What I learned

I learned effective coding in Pygame, and strategies for using it. I also increased my skill in coding logic by creating this.

## What's next for Stay Safe

 - Stay Safe could be greatly enhanced in the future with a timer for each game, and possibly a point value. 
 - It would be great to add a feature where the game calculates the minimum amount of clicks required to complete the game.
 - When the player finishes the game, the game shows the player clicks and the minimum amount of clicks, so that the player can try to improve their score and match that minimum. 
 - Different, high resolution, detailed sprites could be used for each state. 
 - The window size could also be increased to fit the sprites.