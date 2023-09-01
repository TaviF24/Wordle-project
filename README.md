# Wordle-project
## Description
A [Wordle simulator](https://www.nytimes.com/games/wordle/index.html), using [Shannon’s entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)). 

## The idea
The main idea of the project is to select a random word from a list of words, then the computer have to find it in as few tries as possible.

## The code
I made two versions of the Wordle game simulator, but the only difference between them is that one of them is using multiprocessing, which made the solution come faster.
-	[wordle_1.py](wordle_1.py) contains the version without multiprocessing, having the average time to find the solution: **2.964 minutes**;
-	[wordle_2.py](wordle_2.py) has the version with the multiprocessing code, which finds the solution in the average time: **47.398 seconds = 0.789 minutes**;
-	[subprog.py](subprog.py) has all the functions used in wordle_1.py;
-	[processes.py](processes.py]) has some functions that are in the subprog.py file but they are modified for multiprocessing;
-	[words.txt](words.txt) contains **11454 Romanian words** used in this game simulator.

## What I used
-	Operating system: MacOS with M1 chip
-	Language: Python 3.10
-	IDE: PyCharm 2022.2.5

 
