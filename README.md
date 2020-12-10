# Problems - Hangman Loops

This is my take on the Hangman game.
This should run on any CLI **with Python3 installed**, but I have only tested it on the linux terminal (Arch Linux, Debian, and distros based on the two aforementioned).

Here are a few things to note:
* The work submitted herein is mine, with the exception of the unittests, which were provided by the institution.
* The fact that there were already unittests to conform to, means I had to limit the scope of my project (in terms of ideas and preferences) in order to pass the mandatory testing.
* The Hangman game in itself is actually not as interesting as GTA V... So don't expect too much.
* I appreciate that you are reading this. I am only writing this "documentation" because... ummh, yeah, my procrastination methods are weird.

### To Run

* ```python3 hangman.py```
    Follow the input prompts to play the game

### To Test

* ```python3 -m unittest tests/test_main.py```
    Runs all the unittests

* ```python3 -m unittest tests.test_main.MyTestCase.test_step1```
    Runs a specific step's unittest, e.g step *1*
