# Python-Class-test
This project is an an experiment with python classes in order to get a better understanding of them and when you should and shouldn't use them.

Note: I did not comment my code when I created this. In the future I may update the repo and add commented code

# Insperation
I got the idea of make a text base RGP like "game" (not really a game) from this [reddit post](https://www.reddit.com/r/learnpython/comments/15uxgf/for_the_life_of_me_i_dont_understand_classes/c7q1si1/) I think this project turned out farily well and it tought me a lot about what the point of classes are in python and when and how to use them. I still have a lot of learning to do when it comes to classes but I say this was a good first step that turned out pretty nicely. I highly suggest reading the reddit post as it was very insightful as well as watching the [MIT OpenCourseWare video](https://www.youtube.com/watch?v=FlGjISF3l78&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA&index=33) on classes as it goes into more detail about classes and how to make them.

# Results
When I was creating this project my idea was to continue my learning in using functions and classes imported from other python files so I wanted to keep the main.py file relativly clean when so I opted to use the localcommand.py (called Standardcommands.py in this project) file developed by LocalsGithub to clear the terminal and rename the window. I also opted to put the classes in their other python file called charerterinfo.py (I just now noticed I spelt character wrong in the file name) as to save space in the main.py file.

In this project there are 2 classes one called Character which is used as the base building block whenever making a character whether it be the main character or the Ogre you fight. There is also a child class of Character called Hero which is used when making the main character which adds a new variable and function.

## The Character class
This class is the building block of all characters in the program and assigns the following variables to all Characters
- name
- hp
- maxhp
- attack
- defense

The Character class also houses the basic combat mechanic in the form of the following functions
- attackother
- add_defend
- remove_defend
- magic
- heal

The Character class is not the best and could be made better but for what its suppose to do it does it well.

## The Hero class
The Hero class is far simpler then the Character class since all it does is inherit the variables from the Character class and then add an XP variable and a function to give the Hero XP. The XP machanic is not used at all and was purly there so I could make an excuse to make a subclass. The frame basic framework is there if someone wants to incorperate a leveling system that increases the heros base stats but I didnt do that.

## The main file
Its a mess and by far not the cleanest code I have ever made but it gets the job done and thats all I care about. The main part of this file is the fightloop since it calls all the functions in the Character class so that proper combat can be had. It is a farily stright forward file but can get a bit confusing if you dont look the files in the core folder. There is another function called cool_print that exists purly to make the intro text look cool.


# What I would change but wont
So this section is just things I would want to improve upon or change but wont since this is only a learning excersise. In the future I might do other learning excersises and actually implament these changes but who knows.

So lets start with the part I hate the most and thats the defending action. Its purpose is to double the defense of a character for 1 turn and it does its job but it does it poorly. The current system in place checks removes the defense buff of the hero after the ogres turn and the ogres buff after the heros turn. If I was to change the system I would try and combine the buff system into a single function and try to remove the if statement that check for the buff, but the current system works no matter how you look at it and thats all I care about.

Lets move on to the text system. Idealy I would like to make the cool_print function the default way of printing text and I know I could have just used that function instead of print, but I honestly want to just make that function take over the print function. Yes its a stupid thing to change becuase the implimentatin of it is easy, but let me be extra ok.

The battle menu is something I would love to change and I honestly might revist this project in the future just so I can learn how to implament the idea. You see the current battle system displays the menu and then you type a number then it says what happens and then has the orge do what he does and then loops until the battle is over. I hate it, its boring, and its easy for someone to mess up. My ideal battle menu would be a pokemon like system where the menu is at the bottom of the screen and you can navigate it with arrow keys or type what you want to do then keep the menu there and have ascii art of the ogre and hero and it would be all cool and fancy, but I dont even know how to keep something static in a terminal window as it is so im just not going to deal with that now.

# The conclusion
This project was a great introduction for me into the world of python classes and I feel like i have a much greater understanding of how they work in python and other languages. In a way you could say its just a dictionary on crack. A good way to put it is that all dictionaries can be turned into a class BUT ideally you dont shouldnt do that. The use case of being able to create the framework and structure of a dictionary and then make multiple dictionaries from that framework makes it worthwhile to learn about classes. I hope that this project can help someone else learn about python classes as much as it helped me learn about them.
