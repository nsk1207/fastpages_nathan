---
toc: true
title: Collegeboard Grading part 3
layout: default
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
    <td>Apparently, the response was had enough to include both the purpose/function.</td>
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
    <td>The algorithm indicates the proper use of a recursive function call to implement iteration/logical sequencing. Moreover, the algorithm also uses a if statements to implement selection in the code to determine if the player won against the computer or not.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written portion clearly shows the inputting of two different "guesses", one comparing the user's guess of rock with the computer's guess of paper, and another one that was the opposite of the previous inputs. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program.</td>
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
    <td>The video response does a good job of showing the input, functionality, and output of the program, allowing the user to play hangman by selecting a word and taking in user inputs to judge whether or not a correct guess was found. The overall purpose/function of the program was also clearly stated in the written portion, aiming to improve people's ability to recognize new words and expand their vocab.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response includes the usage of a list, it's name, and the purpose it serves. The list is in the form of an array that stores the individual letters of a word (<code>letOfGuessWord</code>), which allows for the program to perform comparisons in the future. In addition, the written response also shows the list being used in the program to fullfil it's purpose in the execution of the program</td>
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
    <td>The written reponse demonstrates usage of the function <code>guessWords</code> in order to compare the inputted word by the user against the randomly selected word by the program . This function also consists of a string argument to represent the user's letter guess at the hidden word, and checks each index of the word list to find a match for the letter. The students also a does a good job to describe how the algorithm works.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a for-loop to implement iteration, in order to properly check over each letter in the hidden word. Sequencing is also present, and selection is also implemented to check if there was a match in the letter and the word, and if the total number of lives is > than 0. If the total number of lives was found to be equal to 0, the game ends with a display screen.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response  shows the inputting of two different inputs, one containing the number "1" that is not in the test string "hello", and another containing the letter "h" that is found in "hello". The response clearly shows why each response gave their resutls and also properly identified each respective result of the program. They also explicitly cited the line numbers within the code to give a reference point of of the execution of the program.</td>
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
    <td>The video response succesfully shows the input and output of the program, which was to use certain keyboard keys such as a and d to move the boat, and eventually add to a total count of fish if the hook comes into contact with one. THe function / purpose were also explicit, with the purpose being to reduce boredom, and the function being to simulate a fishing game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response includes the use of a list ( (<code>fishtypes</code>) ), and the purpose it serves. The list is in the form of an array that stores the total amount of fish caught by the user. Later, the list is also shown to be used to output the total number of fish of the different types that were caught by the user.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response succesfully writes how a list serves to reduce complexity. The student doesn't say what would happen without the usage of a list. They don't say how they would likely have to resort to the use of individual variables to store each fish and the number of that fish caught, which would be complicated and annoying, especially if they wanted to add more types of fish in the future.</td>
    <td>CB says that they actually got it because the student DOES respond that without the list, they would have to resort to individual variables.</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates usage of a function <code>clonemovement</code> in order to determine the spawning of the fishes including their location, distance, and displacement. This function consists of 5 arguments serving to define the range/speed of the fish. The student also explains how this specific helps the functionality of the program, as it serves to randomly spawn differnt fished in order to change difficulty in the game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a loop to implement iteration to move the fish clone until it either reaches the screen's edge, or is touched by the hook. Sequencing could also be observed in the function as it creates a clone of a fish first before executing the loop and it's following logic. The algorithm also uses an if statement to implement selection in the code to determine whether of not if the clone is touching the screen edges.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one where the clone is touching the right edge of the screen, and another one where its not. The response clearly details the results of each procedure.</td>
    <td>CB says that this student did not earn the point for this row because they only tested for the alternate code segments, rather than actual arguments and inputs into the function itself. It did not earn the point.</td>
  </tr>
</table>