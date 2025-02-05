# 🎮 Treasure Hunt Adventure Game 🎮

This project recreates a simple adventure game where the player must move across a grid to find a hidden treasure. The player can move in four directions (up, down, left, right), dig to find the treasure, and receive information about the game status at each step.

## 🚀 Main Features

### 🗺️ Movement and Exploration
- **Movement**: The player can move across the grid using the keys `W`, `A`, `S`, `D` to move up, down, left, or right, respectively.
- **Environment Exploration**: The game displays the current position of the player on the grid, along with the coordinates. Each movement is visually reflected on the board.
- **Game Cycle**: The player can keep moving and searching for the treasure until they find it or decide to exit.

### 🏆 Finding the Treasure
- **Digging**: The player can dig at their current location by pressing the `E` key to check if they have found the treasure.
- **Objective**: The player wins the game by finding the treasure, which is hidden at a random coordinate on the grid.

### 🔄 Interface and Logic
- **Real-Time Update**: The grid and the player's position are updated every time the player performs an action.
- **Console Cleaning**: The console is simulated to clear, improving the game's visual representation by printing blank lines.

## 🧩 Additional Features
- **Treasure Coordinates**: The treasure is located at a random coordinate on the grid, and the player needs to find it before they decide to quit.
- **Secret Interaction**: By pressing the `M` key, the player can view the coordinates of the treasure, useful for debugging or development purposes.
- **Game End**: The game ends when the player finds the treasure or chooses to quit.

## 🌐 How to Play
Run the code and follow the instructions in the console to move and explore. Good luck on your treasure hunt!
