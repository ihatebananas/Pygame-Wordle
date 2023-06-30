# Pygame-Wordle
This is Wordle created with Pygame

My first attempt at a game, with the intention of trying to implement Wordle according to the following rules: 

1. The guessed word must be part of the word bank
2. All "perfect matches" -- same letter, same index -- are highlighted.
3. The max amount of highlighted, or colored versions of a given letter never exceeds the number of instances of the letter in the actual word.
   
   For example, if I were to guess "sssss" for the word "essay", assuming the compiler accepts "sssss" (it does not), it would only highlight the two "ss" that match.
   
4. According to #2, all perfect matches, greens, are given priority over imperfect matches, yellows. If there is a case of too many colored letters and it is a clash between yellows, priority is given in a first come first serve basis.

   For example, if I were to guess "sassy" for "essay", the first s would be yellow, and the s at the fourth index would be green. So, the perfect match is highlighted, and among the other two yellows, there is a first come first serve basis

Full disclosure, not every part of this code is unique. In terms of the PyGame functionalities, this was inspired by LeMaster Tech on YouTube (whose code I will link here) 

https://github.com/plemaster01/LeMasterTechYT 

LeMaster Tech's YouTube Channel: https://www.youtube.com/@lemastertech

As for what parts of the code are truly unique:
1. The entire logic. The logic from his tutorial video (https://www.youtube.com/watch?v=L-foz02o3LU&ab_channel=LeMasterTech) is largely flawed, and 99.5% of the effort for this project went into fixing the logic. In the aforementioned rules, the code did not involve points 1,3,4.
2. The methods findMatches and findColored, the biggest part of this project for me.
3. The blinking functionality. I believe there may have been something related to blinking in the project I used as inspiration, but the blinking functionality was a product of different research into documentation.

As for what parts I basically almost copied (but still handwrote and thoroughly read through with the help of the documentation), it had to do with:
1. The fonts, widths, heights, etc. of the drawn shapes and objects.
2. The "routine". The idea of the draw_board() method was not mine to begin with, but part of the "routine" I saw in the video. While the methods are vastly different now because of the completely different logic, I did indeed take the idea of this "routine" from the video.
3. Some of the methods used inside the game loop for recognizing events. While none of the logic inside the game loop was remotely similar, I did take liberty to utilize some of the given code for keystrokes and quitting the game.

As for why I did not uniquely create those, it is simply because I did not think, and still do not think this was the point of the project. The objective was to learn a little bit about how games work for future projects, and to learn and reinforce certain programming skills like recursion in an actual project. The customization of drawing, fonts and general stylistic choices does not really prove useful in that regard.

I have a vague plan of moving this project to a nicer looking product in a different engine, if I were still interested in the future. Perhaps some ingenious 3D version on Unity. 
