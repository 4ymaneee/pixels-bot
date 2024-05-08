🎮 Pixels Game Automation Bot
Description
This repository contains a Python script for automating actions in the Pixels game. The bot utilizes computer vision techniques for image detection and automation using OpenCV, PyAutoGUI, and threading. It continuously scans the screen for specific images related to collecting and crafting in the game and performs corresponding actions automatically.

Features
Automated Collecting: 🛠️ The bot detects and collects resources in the game.
Crafting Automation: 🏭 It also automates crafting by detecting crafting options and performing necessary actions.
User Interface: 🖥️ Includes a simple GUI built with Tkinter for easy interaction and control.
Prerequisites
Python 3.x
OpenCV (cv2)
NumPy (numpy)
PyAutoGUI (pyautogui)
Tkinter (tkinter)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/aymane67/Pixels-Game-Bot.git
Install dependencies:
Copy code
pip install -r requirements.txt
Usage
Run the bot:
Copy code
python pixels_game_bot.py
Click the "Start" button to begin automation.
To pause automation, click the "Stop" button. Click "Start" again to resume.
Close the application window to exit.
Customization
Images: Replace the image files for collecting and crafting with the relevant images from your game.
Threshold: Adjust the threshold value (0.8 by default) in the code for template matching to improve detection accuracy.
Contribution
Contributions are welcome! Feel free to open issues or pull requests for any improvements or fixes.