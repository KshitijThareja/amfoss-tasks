# Terminal Hunt

This was quite engaging I would say. This task made me familiar with almost all the commonly used terminal commands. 
I'd try to mention most of the commands that I used for getting the complete password.

Here's the stepwise order-

1. `git clone https://github.com/gauthamk02/TerminalHunt.git`

    To clone the terminal hunt folder to your pc.

2. 'cd' is used to navigate to a directory.

`cd TerminalHunt`

'mkdir' is used to create a new directory.

`mkdir solution`

3. `cd solution`

'touch' is used to create a new file.

`touch part1.txt`

'echo' is used to insert content into a file.

`echo "107" >> 'part1.txt'`

4. For copying, first navigate to the folder from which you have to copy text with "cd" command. After that use 'cp' command to copy required file to another directory and rename it as shown.

`cp file.txt ~/path..../newfilename.txt`

With this, we can do part-2 and part-3

5. For commiting your work to github, first 'cd' to the directory to be commited. After that-

`git add .` It adds a change in the working directory to the staging area. 

`git status` To see which changes have been staged, which haven't, and which files aren't being tracked by Git.

`git commit -m "initial commit"` To commit your work.

`git push origin main` To push your work to the remote repository.

6. `git branch -a` To see all the local and remote branches of the repository.

`git checkout <branch_name>` To switch to the new branch.

`find . -name <file_name>.txt` To find path of a file in a directory.

7. `git checkout main` 

`git merge <branch_name>`For merging the present branch with another branch.

Go to the folder where the last password text is stored. Then copy it to the solution folder in a file named part4.txt

`cp file.txt ~/path..../part4.txt`

8. `cat part1.txt part2.txt part3.txt part4.txt >> password.txt` To concatenate the contents of multiple files and put it in a single file.

`rm part1.txt part2.txt part3.txt part4.txt` To remove files.

![Secret-scroll](https://user-images.githubusercontent.com/116485536/207087937-657b229f-ac14-4629-8856-508bc0f4fba3.png)
