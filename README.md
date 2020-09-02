# CS3001_Break-TimeFun_AU19B1005
This repository is about the game "Break - Time Fun".

## Overview

This game is all about having fun in break – time. Of course you can play this without break also… Enjoy!

## Description

This game is basically a card (tile) based game. It has 3 categories overall to play. They are MATH, RIDDLE and G.K.
So, each of these categories consist of a set of questions. After selecting Play Game option, the player needs to select the category to play. After the selection the player gets the related set of questions one by one on a card. He needs to click the card and then the question is revealed. After the question is revealed automatically a text box appears below the card, so, the user can feed the answer there. You are provided with 3 lives in the game. After feeding the answer, it is evaluated, whether it is correct or wrong - it gets displayed on the screen. If you attempt a wrong answer, your one life gets reduced, i.e. it becomes red. Accordingly scores are added in the game for correct answers + 5 and for wrong answers -4. There are 13 questions, initially this number is fixed randomly. The difficulty of questions increases after each question. So, if a player scores around 50 (i.e. equal to 50 or more than 50), then when all the attempts have been used at the end this appears on the screen “Hey.. Congratulations! Your knowledge is strong. Keep it up!”. And if the player scores less than 50 towards the end, then this appears on the screen “Hey.. You need to push your brain a little more. Keep up the pace!”. So, it’s all about your existing knowledge and brain efforts in any of the 3 sections.

## Rulebook

* You have 3 lives!
* You can only answer once per question.
* There are 2 SKIP options available. 
* Once you have disclosed a tile it cannot be closed again.
* Each wrong answer results to -1 life.
* Fourth wrong attempt leads to game over.
* If you give a correct answer, only then next tile appears on your screen.
* Each correct answer leads to +5 score and each wrong answer leads to -4 score. 
* When you Click on TRY ME tile, the question will appear on that and automatically an answer textbox will appear there.
* You cannot go to the next question until you solve the current question. So, to reach the next question you can either use skip option (only for twice) or if you input wrong answer, then your life would be reduced and you can proceed further.
* As you solve the questions and clear the levels, no. of questions get increase at each level and with increasing questions, time limit comes in existence. After clearing initial 4 questions the above statement comes in action.

## Game Interface - Proposed:

![Image](https://github.com/MuskanJain13/CS3001_Break-TimeFun_AU19B1005/blob/readme-edits/page_1.png)
![Image](https://github.com/MuskanJain13/CS3001_Break-TimeFun_AU19B1005/blob/readme-edits/page_2.png)
![Image](https://github.com/MuskanJain13/CS3001_Break-TimeFun_AU19B1005/blob/readme-edits/page_3.png)
![Image](https://github.com/MuskanJain13/CS3001_Break-TimeFun_AU19B1005/blob/readme-edits/page_4.png)
![Image](https://github.com/MuskanJain13/CS3001_Break-TimeFun_AU19B1005/blob/readme-edits/page_5.png)
![Image](https://github.com/MuskanJain13/CS3001_Break-TimeFun_AU19B1005/blob/readme-edits/page_6.png)

## Gathering technical requirements

*	Identification of Problem
*	Gathering technical requirements
*	Spyder (Python (3.7)
*	Module for GUI - PySimpleGUI or Tkinter: Window, Keys, Labels, Text and user inputs, Buttons (Elements or Widgets)
*	Conditional statements – if else
*	Counter variables – SKIP, LIFE, SCORE
*	Sequences

## Steps to proceed

1.  Create a basic window.
2.  Display text and buttons on window - Play Game! and Game Info.
3.  Game Info - Display text and Play Game! button.
4.  Play Game! - Display text and 3 buttons: MATH, RIDDLE, G.K.
5.  RIDDLE - Display a card TRY ME (button)
    After clicking card, question and text box should appear.
    Display 3 lives on the page.
6.  Validate the answer
    After the answer is feeded and enter is pressed, answer should be evaluated as wrong or correct.
    Display correct or wrong answer!
7.  Correct answer - NEXT button should appear.
8.  Wrong answer - 1 life becomes red.
9.  Display SKIP button - can be used only 2 times.
10. Score - Display score on the game page.
    Correct answer - (+5)
    Wrong answer - (-4)

