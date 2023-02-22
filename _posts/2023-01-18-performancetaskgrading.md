---
toc: true
title: Collegeboard Grading part 3
layout: base
---

# This week, I need to work on being more thorough and specific with my grading in order to bring up my last week's grad (0.9) to a 1. 

## Submission 1 Overall Idea: 
The overall idea of this program was to create a program simulates a rock-paper-sicsors game .

### Grading:  
<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>0/1</td>
    <td>The video portion did a good job of showing the input, functionality, and output of the program, which prompted the user to pick either rock, scissors, or paper. However, only the purpose was stated in the written portion, and the function of the program was not there and therefore, will not earn the full point.</td>
    <td>Apparently, according to CB, the response included both the purpose/function properly..</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response has a usage of a list, it being (<code>RPS</code>), and the purpose it serves is seving as random set of input for the computer.</td>
    <td>Accorinding to CB, however, it does not show how data in the list is being used in the code. They didn't earn the point for this row.</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>0/1</td>
    <td>Although the response explains why a list is being used, it does not tell us why the usage of the list would serve to reduce complexity in the program. Instead the response only gives a brief overview of what can be used in place of the list, and not how that particular replacement is not as efficient.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written portion indicates a function that takes in an user input and compares it with a computer move thorugh the fucntion <code>rpsGame</code>. This function serves to output different results based on the computer and user inputs.</td>
    <td> CB says that the written response does not serve to explain how the  procedure helped to contribute to the overall functionality of the program, and was unclear in stating how it allowed for the program to execute properly and with smoothly.</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a recursive function call to implement iteration/logical sequencing. In addition the algorithm also uses a if statements to implement selection in the code to determine if the player won against the computer or not.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written part of the program effectively illustrates the process of inputting two different choices, one in which the user selects rock and the computer selects paper, and another where the input is the opposite. The written response clearly explains the outcomes of each scenario and accurately identifies the results of the program.</td>
    <td></td>
  </tr>
</table>

## Submission 2 Overall Idea:
The overall idea of this program was to create a program that challenges the user to a 5-word hangman to help them recognize new words/expand their vocab knowledge

### Grading:  
<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video demonstration effectively illustrates the input process, features, and output of the program, enabling users to participate in the hangman game by choosing a word and inputting guesses to determine if they are correct. The main objective of the program, which is to enhance people's vocabulary and ability to learn new words, is also clearly explained in the accompanying written description.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and its corresponding explanation make use of a list, specifically an array, that holds the individual letters of a word (<code>letOfGuessWord</code>), enabling the program to conduct comparisons. The list is central to the program's functionality, as it enables the execution of the program's purpose as described in the written response.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response successfully states how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store each letter, which would be difficult to implement an iterative method to check for matches. </td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td> The written explanation showcases the usage of the <code>guessWords</code> function, which compares the user's inputted word to the randomly chosen word by the program. This function takes in a string argument that represents the user's guessed letter in the hidden word and checks each index of the word list to find a matching letter. The student also effectively explains the workings of the algorithm.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm employs the use of a for-loop to execute iteration, which allows for checking every letter in the hidden word. The algorithm also uses sequencing and selection, it checks if there is a match between the letter and the word, and whether the number of lives is greater than 0. If the total number of lives reaches 0, the game terminates with a display screen.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written explanation displays the input of two different inputs, one inputting the number "1" which is not present in the test string "hello", and another inputting the letter "h" which is present in "hello". The explanation clearly explains the reasons for each input's results and correctly identifies each outcome of the program. It also specifically references the line numbers within the code to provide a clear reference point for the program's execution.</td>
    <td></td>
  </tr>
</table>

## Submission 3 Overall Idea
The overall idea of this submission was to create a program that takes a state inputed by the user and outputs certain information about that state.

### Grading:  
<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, which had the user input a state and then select different information to display on the screen. The written response also expolained the function/purpose of the program, which was to provide the user with information on a state, with the purpose to help the user learn new information.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>0/1</td>
    <td>The program and response includes the usage of a list, it's name (<code>statelist</code>), and the purpose it serves. However, it does not show how the data is stored within the list. As such, it does not earn the point for this row.
    <td>In addition, the description in the written response for the list was also wrong as the list <code>statelist</code> only represents the name of the states.</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response successfully states how the usage of the list serves to reduce complexity. The student responds that without the list, they would likely have to code each piece of data seperately, resulting in more compelxity as a whole. </td>
    <td>CB says that the written portion doesn't successfully explain how the operation would be more complex in detail. It did not earn the point..</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>0/1</td>
    <td>Although the written reponse displays the function <code>updatescreen</code> in order to assign an index to each state, it does not have any parameters that are passed to it. This does not earn the point for this row..</td>
    <td>In addition to my respoonse, CB also said that the written portion also inaccurately described the main function of the procedure</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>0/1</td>
    <td>The algorithm indicates the proper use several if statements to implement sequencing/selection. However, the program does not indicate the use of any form of a loop or anything similar to show iteration in the program.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response shows the results/scenario of the both proceudres to identify that their program works as expected in accordance with the purpose and function</td>
    <td>The written reponse doesn't properly show different parameters that are put in the procedures. Tt also doesn't describe the result in detail, but  only gives a breif summary of what happens on the screen instead.</td>
  </tr>
</table>

## Submmission 4 Overall Idea:
The overall idea of this submission was to create a program that simulates a fishing game to prevent from being bored. 

### Grading:  
<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response effectively demonstrates the input and output of the program which allows the user to move the boat using specific keyboard keys such as a and d, and then increase a total count of fish when the hook comes into contact with one. The objective and function of the program were also clearly stated, with the objective being to alleviate boredom, and the function being to simulate a fishing game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The written response demonstrates the implementation of a list, referred to as <code>fishtypes</code>, and explains its purpose. The list is in the form of an array and it is used to store the total number of fish caught by the user. The response also shows how the list is used later on to output the total number of fish of different types that were caught by the user.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response effectively explains how the utilization of a list simplifies the program. The student does not specify what the alternative would have been without the use of a list but it's explained that it would have been more complicated and annoying as it would have required the use of individual variables to store each type of fish caught, which would be tedious, especially if more types of fish were added in the future.</td>
    <td>CB says that they actually got it because the student DOES respond that without the list, they would have to resort to individual variables.</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written response effectively explains the use of the <code>clonemovement</code> function, which is used to manage the spawning of the fish, including their location, distance, and movement. This function utilizes five different parameters to determine the range and speed of the fish. The student also highlights how this function contributes to the overall functionality of the program by randomly spawning different fish to change the difficulty of the game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm effectively employs a loop to repeatedly move the cloned fish until it reaches the edge of the screen or is caught by the hook. The logic is executed in a specific order, starting with the creation of a fish clone, followed by the execution of the loop and its subsequent conditions. The use of an if statement allows for the selection of whether or not the cloned fish is touching the edge of the screen.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one where the clone is touching the right edge of the screen, and another one where its not. The response clearly details the results of each procedure.</td>
    <td>CB says that this student did not earn the point for this row because they only tested for the alternate code segments, rather than actual arguments and inputs into the function itself. It did not earn the point.</td>
  </tr>
</table>