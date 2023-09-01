# Wordle-project
## Description
A [Wordle simulator](https://www.nytimes.com/games/wordle/index.html), using [Shannon’s entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)). 

## The idea
The main idea of the project is to select a random word from a list of words, then the computer have to find it in as few tries as possible.

## The code
I made two versions of the Wordle game simulator, but the only difference between them is that one of them is using multiprocessing, which made the solution come faster.
-	[wordle_1.py](wordle_1.py) contains the version without multiprocessing, having the average time to find the solution ≈ **2.964 minutes**;
-	[wordle_2.py](wordle_2.py) has the version with the multiprocessing code, which finds the solution in the average time ≈ **47.398 seconds ≈ 0.789 minutes**;
-	[subprog.py](subprog.py) has all the functions used in *wordle_1.py*;
-	[processes.py](processes.py]) has some functions that are in the *subprog.py* file but they are modified for multiprocessing;
-	[words.txt](words.txt) contains **11454 Romanian words** used in this game simulator.
 > [!NOTE]
 > If you modify the number of words in the *words.txt* file, then you have to modify the *processes.py* file too.

In both versions, the output will be:
1.	every word followed by its entropy for the entire list
2.	then a list ordered descending by entropy
3.	the random word which must be find
4.	after that, every try will be printed out, followed by its entropy at that moment, and a list of *remaining words*(after every try, the list of words is updated, removing each word which doesn’t have any similarity and recalculating the entropy for each word)
5.	in the end, if the searched word is find, it will be printed again, otherwise the messages "nereusit" and "Cuvantul nu a fost gasit" will appear. All the tries with their entropies and the execution time will be printed out.

<img width="500" alt="Screenshot 2023-09-01 at 15 48 59" src="https://github.com/TaviF24/Wordle-project/assets/118764142/d2601d4a-da0e-4789-ad63-f8d9ed0217ef">

## What I used
-	Operating system: MacOS with M1 chip
-	Language: Python 3.10
-	IDE: PyCharm 2022.2.5

 
