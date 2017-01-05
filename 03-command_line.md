# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.
 
`cd ../../otherdirectory` navigates up directories to specific folders 	
`mkdir` makes a new directory  
`touch` creates a new empty file with specified name  
`cat file1.txt >> file2.txt` appends standard output of file1 to file2  
`sort file.txt uniq` only gives the unique members sorted  
`grep Word file.txt` prints instances including Word within file, -i option is case insensitive  
`grep –R Word dir/dir` looks recursively for Word anywhere in the directory, -Rl option to only give file names and not instances of Word  
`sed ‘s/word1/word2/g’` file.txt replaces every instance of word1 in every line with word2  
`alias function2="function1"` allows you to type function2 for the function1 command  
`nano file.txt` opens a new text file within nano  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`      displays contents of a directory  
`ls -a`   displays all contents of a directory, including hidden ones  
`ls -l`   displays contents of a directory in long format  
`ls -lh`  displays contents of a directory in long format with file sizes in K/M, etc format  
`ls -lah` displays all contents of a directory in long format with file sizes in K/M, etc format  
`ls -t`   displays contents of a directory sorted by most recently edited  
`ls -Glp` displays contents of a directory in long format with a / at the end of each and color coding for directories and files 

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`-m`	Displays the names as a comma-separated list. (could be useful for lists, dictionaries etc. in Python)  
`-u`	Displays files by the file access time  
`-r`	Displays files in reverse order  
`-g`	Displays the long format listing, but exclude the owner name
`-o`	Displays the long format listing, but excludes group name.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` passes a list of arguments to another command.  
one example of using it is `find . -name '*.txt' | xargs grep 'word1'` which will find all files that contain the string `word1`

 

