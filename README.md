# A* Algorithm Visualization

## Introduction

This project is an application that visualizes the A* (A-star) pathfinding algorithm. It allows users to draw a starting point, an ending point, and barriers on the screen to see how the A* algorithm finds the optimal path from the start to the end while avoiding obstacles.

## Features

- **Left-click**:
  - First click: Draw the **starting point**.
  - Second click: Draw the **ending point**.
  - Subsequent clicks: Draw **barriers**.
  
- **Right-click**:
  - Erase any drawn points (starting point, ending point, and barriers).

- **Run Button**:
  - Runs the A* algorithm to find and visualize the shortest path from the start point to the end point.

- **Clear Button**:
  - Clears all points from the screen.

- **Random Button**:
  - Randomly generates barriers on the screen.

- **Keyboard Shortcuts**:
  - **Space**: Runs the A* algorithm.
  - **C**: Clears all points.
  - **R**: Randomly generates barriers.

## How to Download

1. **Clone the project**:
   Open a terminal and run the following command to clone the project to your local machine:
   ```
   git clone https://github.com/GnasAI/AStarAlgorithm.git
2. **Install Pygame**:  If you haven't installed the Pygame library yet, you can install it using pip
   ```   
   pip install pygame
3. **Run the application**: Once Pygame is installed, you can run the program through your preferred Python IDE or via terminal with:
   ```   
   python main.py
## How to Use

1. **Draw Starting and Ending Points**:
   - Left-click anywhere on the screen to set the **starting point**.
   - Left-click again to set the **ending point**.

2. **Draw Barriers**:
   - After placing the start and end points, left-click in different locations to create **barriers** that the A* algorithm will avoid when finding a path.

3. **Erase Points**:
   - Right-click on any point to remove it. You can erase the start point, end point, or barriers by right-clicking on them.

4. **Run the A* Algorithm**:
   - Click the **Run** button or press the **Space** key to run the A* algorithm and visualize the shortest path from the starting point to the ending point, navigating around barriers.

5. **Clear All Points**:
   - Click the **Clear** button or press the **C** key to reset the screen and remove all points (start, end, and barriers).

6. **Generate Random Barriers**:
   - Click the **Random** button or press the **R** key to randomly generate barriers on the screen. This feature helps you quickly create a new setup for testing the A* algorithm.

## System Requirements

- Python 3.x
- Pygame library (install using `pip install pygame`)

## References

This project was developed using guidance from the following resources:

1. [A* Pathfinding Algorithm - YouTube Tutorial by The Coding Train](https://youtu.be/aKYlikFAV4k?si=eol2ASkZBoetJJBH)
2. [A* Algorithm Explained - YouTube by Computerphile](https://youtu.be/EaZxUCWAjb0?si=wr77i5ijkH3bh1rK)
3. [A* Search Algorithm - YouTube by Sebastian Lague](https://youtu.be/jwRT4PCT6RU?si=P6D-5pDJ_7z-MWBx)
4. [A* Pathfinding Visualization - YouTube by Tech With Tim](https://youtu.be/JtiK0DOeI4A?si=7Bn3IsnwOfhNFKKR)

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue to discuss your ideas. Contributions are welcome!




