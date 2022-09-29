---
toc: true
layout: post
title: City Generator
categories: [week5,markdown]
comments: true
---
<button type="button" class="btn btn-light" onclick="randomNumber()">Click to Generate Random Number</button>
  <br>
  <h3 id="Number Generator" href="#">Here is your number!</h3>
  <script>
    const numberList = [ 
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20"
  ];
    function randomNumber() { 
    var index=Math.floor(Math.random() *numberList.length) 
    document.getElementById("Number Generator").innerHTML = numberList
    [index]
  }
  </script>