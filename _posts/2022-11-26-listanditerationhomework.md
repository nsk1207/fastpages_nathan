---
keywords: fastai
description: Try to complete this to show understanding! Copy this into your notebook so you can also take notes as we lecture. Make a copy of this notebook to your own repository to take notes, do the class challenges, and to access the homework.
title: Lists and Iteration Homework
toc: true
permalink: /homework/
nb_path: _notebooks/2022-11-26-listanditerationhomework.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-11-26-listanditerationhomework.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Overview-and-Notes:--3.10---Lists">Overview and Notes:  3.10 - Lists<a class="anchor-link" href="#Overview-and-Notes:--3.10---Lists"> </a></h2><ul>
<li>Make sure you complete the challenge in the challenges section while we present the lesson! </li>
</ul>
<p>Add your <mark>OWN</mark> Notes for 3.10 here:</p>
<p>Notes</p>
<ul>
<li>lists are collections of data<ul>
<li>indexes: most code languages count starting with zero, and this is also the case for list indexes</li>
<li>you can use them to store unlimited amounts of data</li>
</ul>
</li>
<li>loops/functions that locate list data using indexes can perform specific functions on lists </li>
<li>List indexes start with 0 generally</li>
<li>Numbers in list can be used for math</li>
</ul>
<p>Table</p>
<table>
<thead><tr>
<th style="text-align:center">Pseudocode Operation</th>
<th>Python Syntax</th>
<th style="text-align:center">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">aList[i]</td>
<td>aList[i]</td>
<td style="text-align:center"><em>Accesses the element of aList at index i</em></td>
</tr>
<tr>
<td style="text-align:center">x ← aList[i]</td>
<td>x = aList(i)</td>
<td style="text-align:center"><em>Assigns the element of aList at index i <br>to a variable 'x'</em></td>
</tr>
<tr>
<td style="text-align:center">aList[i] ← x</td>
<td>aList(i) = x</td>
<td style="text-align:center"><em>Assigns the value of a variable 'x' to <br>the element of a List at index i</em></td>
</tr>
<tr>
<td style="text-align:center">aList[i] ← aList[j]</td>
<td>aList[i] = aList[j]</td>
<td style="text-align:center"><em>Assigns value of aList[j] to aList[i]</em></td>
</tr>
<tr>
<td style="text-align:center">INSERT(aList, i, value)</td>
<td>aList.insert(i, value)</td>
<td style="text-align:center"><em>value is placed at index i in aList. Any <br>element at an index greater than i will shift<br>one position to the right. </em></td>
</tr>
<tr>
<td style="text-align:center">APPEND(aList, value)</td>
<td>aList.append(value)</td>
<td style="text-align:center"><em>value is added as an element to the end of aList<br>and length of aList is increased by 1</em></td>
</tr>
<tr>
<td style="text-align:center">REMOVE(aList, i)</td>
<td>aList.pop(i)<br>OR<br>aList.remove(value)</td>
<td style="text-align:center"><em>Removes item at index i and any values at <br>indices greater than i shift to the left. <br>Length of aList decreased by 1. </em></td>
</tr>
</tbody>
</table>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Overview-and-Notes:--3.8---Iteration">Overview and Notes:  3.8 - Iteration<a class="anchor-link" href="#Overview-and-Notes:--3.8---Iteration"> </a></h2><p>Add your <mark>OWN</mark> Notes for 3.8 here:</p>
<p>Iteration</p>
<ul>
<li>repetition</li>
<li>copy pasting the same code is complicated and unprofessional<ul>
<li>conditional iteration: you need to tell the machine when to stop </li>
</ul>
</li>
<li>most languages have their own versions of a "for" loop</li>
<li>lists can have multiple items and you may need multiple parenthesis with different variables in the list <ul>
<li>dictionaries are useful here </li>
</ul>
</li>
<li>recursive loops can be created in multiple ways and involve incrementing a varaible until it reaches a certain breaking point </li>
<li>while loops don't require a function that is then called again within the original function until a condition is met</li>
</ul>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">drewpets</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;Drew&quot;</span><span class="p">,</span> <span class="p">({</span><span class="s2">&quot;dogs&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;cats&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;fish&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">}))]</span>
<span class="n">ajpets</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;AJ&quot;</span><span class="p">,</span> <span class="p">{</span><span class="s2">&quot;dogs&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;cats&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;fish&quot;</span><span class="p">:</span> <span class="mi">329</span><span class="p">})]</span>
<span class="n">johnnypets</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;Johnny&quot;</span><span class="p">,</span> <span class="p">{</span><span class="s2">&quot;dogs&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s2">&quot;cats&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;fish&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">})]</span>
<span class="n">allpets</span> <span class="o">=</span> <span class="p">[</span><span class="n">drewpets</span><span class="p">,</span> <span class="n">ajpets</span><span class="p">,</span> <span class="n">johnnypets</span><span class="p">]</span> <span class="c1">#a collection of all pet lists</span>

<span class="k">for</span> <span class="n">person</span> <span class="ow">in</span> <span class="n">allpets</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="nb">dict</span> <span class="ow">in</span> <span class="n">person</span><span class="p">:</span> <span class="c1">#unpacking the name and dictionary</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">name</span> <span class="o">+</span> <span class="s2">&quot;&#39;s pets:&quot;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">pet</span><span class="p">,</span> <span class="n">num</span> <span class="ow">in</span> <span class="nb">dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span> <span class="c1">#use .items() to go through keys and values</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">pet</span><span class="o">.</span><span class="n">capitalize</span><span class="p">()</span> <span class="o">+</span> <span class="s2">&quot;:&quot;</span><span class="p">,</span> <span class="n">num</span><span class="p">)</span> <span class="c1">#capitalizes first letter</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Drew&#39;s pets:
Dogs: 1
Cats: 1
Fish: 0

AJ&#39;s pets:
Dogs: 1
Cats: 0
Fish: 329

Johnny&#39;s pets:
Dogs: 2
Cats: 0
Fish: 0

</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Homework-Assignment">Homework Assignment<a class="anchor-link" href="#Homework-Assignment"> </a></h2><p>Instead of us making a quiz for you to take, we would like YOU to make a quiz about the material we reviewed.</p>
<p>We would like you to <mark>input questions into a list</mark>, and use some sort of iterative system to print the questions, detect an input, and determine if you answered correctly. There should be <em>at least</em> <mark>five questions</mark>, each with <em>at least</em> <mark>three possible answers</mark>.</p>
<p>You may use the template below as a framework for this assignment.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">right</span> <span class="o">=</span> <span class="mi">0</span> 
<span class="n">totalqs</span> <span class="o">=</span> <span class="mi">5</span> 

<span class="n">questions</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">(</span><span class="s2">&quot;What do list indexes generally start with&quot;</span><span class="p">,</span><span class="s2">&quot;A) 0&quot;</span><span class="p">,</span> <span class="s2">&quot;B) 1&quot;</span><span class="p">,</span> <span class="s2">&quot;C) -1&quot;</span><span class="p">,</span> <span class="s2">&quot;A&quot;</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;What is iteration known as?&quot;</span><span class="p">,</span> <span class="s2">&quot;A) Looping&quot;</span><span class="p">,</span> <span class="s2">&quot;B) Repetition&quot;</span><span class="p">,</span> <span class="s2">&quot;C) Stringing&quot;</span><span class="p">,</span> <span class="s2">&quot;B&quot;</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;What does aList[i] do?&quot;</span><span class="p">,</span><span class="s2">&quot;A) Accesses the element of aList at index i&quot;</span><span class="p">,</span> <span class="s2">&quot;B) Assigns the element of aList at index i &lt;br&gt;to a variable &#39;x&#39;&quot;</span><span class="p">,</span> <span class="s2">&quot;C) _Assigns value of aList[j] to aList[i]_&quot;</span><span class="p">,</span> <span class="s2">&quot;A&quot;</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;What can numbers in lists be used for?&quot;</span><span class="p">,</span> <span class="s2">&quot;A) Reading&quot;</span><span class="p">,</span> <span class="s2">&quot;B) Science&quot;</span><span class="p">,</span> <span class="s2">&quot;C) Math&quot;</span><span class="p">,</span> <span class="s2">&quot;C&quot;</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;What are lists?&quot;</span><span class="p">,</span> <span class="s2">&quot;A) A sequence of characters&quot;</span><span class="p">,</span> <span class="s2">&quot;B) Collection of data&quot;</span><span class="p">,</span> <span class="s2">&quot;C) A repetition of code until the desired result is produced&quot;</span><span class="p">,</span> <span class="s2">&quot;B&quot;</span><span class="p">)</span>
<span class="p">]</span>
<span class="c1">#</span>

<span class="c1"># After attempting to try the quiz, it doesn&#39;t seem to work. I think there is something wrong with my integer and position placement, but I don&#39;t understand how to fix it. </span>
<span class="k">def</span> <span class="nf">questionloop</span><span class="p">():</span>
    <span class="n">right</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">questions</span><span class="p">)):</span>
        <span class="n">answer</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;A, B, or C&quot;</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">answer</span> <span class="o">==</span> <span class="n">questions</span><span class="p">[</span><span class="mi">4</span><span class="p">]:</span> <span class="c1"># 4 represents position in lsit</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Correct&quot;</span><span class="p">)</span>
            <span class="n">right</span> <span class="o">=</span> <span class="n">right</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Wrong&quot;</span><span class="p">)</span> 
<span class="n">questionloop</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;You got a: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">right</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;/5&quot;</span> <span class="o">+</span> <span class="s2">&quot; or a &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">((</span><span class="n">right</span><span class="o">/</span><span class="n">totalqs</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;%&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Hacks">Hacks<a class="anchor-link" href="#Hacks"> </a></h3><p>Here are some ideas of things you can do to make your program even cooler. Doing these will raise your grade if done correctly.</p>
<ul>
<li>Add more than five questions with more than three answer choices</li>
<li>Randomize the order in which questions/answers are output</li>
<li>At the end, display the user's score and determine whether or not they passed</li>
</ul>
<h2 id="Challenges">Challenges<a class="anchor-link" href="#Challenges"> </a></h2><p><mark>Important!</mark> You don't have to complete these challenges completely perfectly, but you will be marked down if you don't show evidence of at least having tried these challenges in the time we gave during the lesson.</p>
<h3 id="3.10-Challenge">3.10 Challenge<a class="anchor-link" href="#3.10-Challenge"> </a></h3><p>Follow the instructions in the code comments.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">grocery_list</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;apples&#39;</span><span class="p">,</span> <span class="s1">&#39;milk&#39;</span><span class="p">,</span> <span class="s1">&#39;oranges&#39;</span><span class="p">,</span> <span class="s1">&#39;carrots&#39;</span><span class="p">,</span> <span class="s1">&#39;cucumbers&#39;</span><span class="p">]</span>


<span class="c1"># Print the fourth item in the list</span>
<span class="nb">print</span><span class="p">(</span><span class="n">grocery_list</span><span class="p">[</span><span class="mi">3</span><span class="p">])</span>

<span class="c1"># Now, assign the fourth item in the list to a variable, x and then print the variable</span>
<span class="n">x</span> <span class="o">=</span> <span class="n">grocery_list</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>

<span class="c1"># Add these two items at the end of the list : umbrellas and artichokes</span>
<span class="n">grocery_list</span> <span class="o">=</span> <span class="n">grocery_list</span> <span class="o">+</span> <span class="p">[</span><span class="s2">&quot;umbrellas&quot;</span><span class="p">,</span> <span class="s2">&quot;artichokes&quot;</span><span class="p">]</span>

<span class="c1"># Insert the item eggs as the third item of the list </span>
<span class="n">grocery_list</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="s1">&#39;eggs&#39;</span><span class="p">)</span>

<span class="c1"># Remove milk from the list </span>
<span class="n">grocery_list</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s1">&#39;milk&#39;</span><span class="p">)</span>

<span class="c1"># Assign the element at the end of the list to index 2. Print index 2 to check</span>
<span class="n">grocery_list</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="n">grocery_list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">grocery_list</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>

<span class="c1"># Print the entire list, does it match ours ? </span>
<span class="nb">print</span><span class="p">(</span><span class="n">grocery_list</span><span class="p">)</span>

<span class="c1"># Expected output</span>
<span class="c1"># carrots</span>
<span class="c1"># carrots</span>
<span class="c1"># artichokes</span>
<span class="c1"># [&#39;apples&#39;, &#39;eggs&#39;, &#39;artichokes&#39;, &#39;carrots&#39;, &#39;cucumbers&#39;, &#39;umbrellas&#39;, &#39;artichokes&#39;]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>carrots
carrots
artichokes
[&#39;apples&#39;, &#39;eggs&#39;, &#39;artichokes&#39;, &#39;carrots&#39;, &#39;cucumbers&#39;, &#39;umbrellas&#39;, &#39;artichokes&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.8-Challenge">3.8 Challenge<a class="anchor-link" href="#3.8-Challenge"> </a></h3><p>Create a loop that <mark>converts 8-bit binary values</mark> from the provided list into <mark>decimal numbers</mark>. Then, after the value is determined, <mark>remove all the values greater than 100</mark> from the list using a list-related function you've been taught before. <mark>Print the new list</mark> when done.</p>
<p>Once you've done this with one of the types of loops discussed in this lesson, create a function that does the same thing with a <em>different</em> type of loop.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">binarylist</span> <span class="o">=</span> <span class="p">[</span>
    <span class="s2">&quot;01001001&quot;</span><span class="p">,</span> <span class="s2">&quot;10101010&quot;</span><span class="p">,</span> <span class="s2">&quot;10010110&quot;</span><span class="p">,</span> <span class="s2">&quot;00110111&quot;</span><span class="p">,</span> <span class="s2">&quot;11101100&quot;</span><span class="p">,</span> <span class="s2">&quot;11010001&quot;</span><span class="p">,</span> <span class="s2">&quot;10000001&quot;</span>
<span class="p">]</span>

<span class="k">def</span> <span class="nf">binary_convert</span><span class="p">(</span><span class="n">binary</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">binary</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
    <span class="c1">#use this function to convert every binary value in binarylist to decimal</span>
    <span class="c1">#afterward, get rid of the values that are greater than 100 in decimal</span>
<span class="n">binarylist</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">binarylist</span> <span class="k">if</span> <span class="n">binary_convert</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="o">&lt;</span><span class="mi">100</span><span class="p">]</span>
<span class="c1">#when done, print the results</span>
<span class="n">binarylist</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>[&#39;01001001&#39;, &#39;00110111&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 
