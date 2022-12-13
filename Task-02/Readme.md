# Terminal Hunt

This was quite engaging I would say. This task made me familiar with almost all the commonly used terminal commands. 
I'd try to mention most of the commands that I used for getting the complete password.

Here's the stepwise order-

1. git clone https://github.com/gauthamk02/TerminalHunt.git 

2. cd TerminalHunt
mkdir solution

3. cd solution
touch part1.txt
echo "107" >> 'part1.txt'

4. For copying, first navigate to the folder from which you have to copy text with "cd" command. After that-
cp file.txt ~/path..../newfilename.txt
With this, we can do part-2 and part-3

5. For commiting your work to github, first cd to the directory to be commited. After that-
git int -b main
git add .
git commit -m "initial commit"
git remote add origin <REMOTE_URL>
git remote -v
git push origin main

6. git branch -a
git checkout <branch_name>
find . -name <file_name>.txt`

7. git checkout main
git merge <branch_name>
Go to the folder where the last password text is stored. Then copy it to the solution folder in a file named part4.txt
cp file.txt ~/path..../part4.txt

8. cat part1.txt part2.txt part3.txt part4.txt >> password.txt
rm part1.txt part2.txt part3.txt part4.txt

![Secret-scroll](https://user-images.githubusercontent.com/116485536/207087937-657b229f-ac14-4629-8856-508bc0f4fba3.png)
