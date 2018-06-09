# ARCRobot - Autonomous and Remote Control Robot
---
ARCRobot is a robot platform written in Python 3. ARCRobot is built for 
dual-motored robots controlled via Raspberry Pi. ARCR started as a passion 
project with little experience in programming. After hitting a wall, I took time 
off of ARCR to focus on the Python language. In coming back to this project I 
feel much more confident in my ability to write and understand Python.

## Getting Started
---
### Dependencies
---
On a fresh install of Raspbian Lite you will need to ensure you have the 
following installed to use with Python 3:

- git
- RPi.GPIO

Optional:

- curses (Remote control)
- subprocess (Activating RPi Camera)
- RPi Camera Web Interface (Remote viewing)

### Usage
---
After ensuring all sensors and motors are connected correctly, you can start 
autonomous mode my running
`python3 go_auto.py`
Your robot should then travel along, avoiding objects and staying out of trouble.

To take back control of your robot you can run
`python3 manual_control.py`
This will begin a loop that responds to key presses to move your robot where you 
please.

## Contributions
---
All contributions are welcome to my project. My email is open to any comments 
and questions as well.
