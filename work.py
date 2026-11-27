PS C:\Python> git init
Reinitialized existing Git repository in C:/Python/.git/
PS C:\Python> git status
On branch Python-Practice
Your branch is up to date with 'origin/Python-Practice'.

Changes to be committed:

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
        modified:   sample1.py
Untracked files:
        work.py

PS C:\Python> git add .
PS C:\Python> git commit -m "work.py"             
[Python-Practice ce41163] work.py
 2 files changed, 30 insertions(+), 1 deletion(-)
 create mode 100644 work.py
PS C:\Python> git branch -M Python-Practice
PS C:\Python> git remote add origin https://github.com/manivannan066/Python-Practice.git
error: remote origin already exists.
PS C:\Python> git push -u origin Python-Practice
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Writing objects: 100% (3/3), 278 bytes | 139.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/manivannan066/Python-Practice.git
   3c7904a..ce41163  Python-Practice -> Python-Practice
branch 'Python-Practice' set up to track 'origin/Python-Practice'.
PS C:\Python> git add .
PS C:\Python> git commit -m "work.py"            
On branch Python-Practice
Your branch is up to date with 'origin/Python-Practice'.

nothing to commit, working tree clean
PS C:\Python> git push origin Python-Practice
Everything up-to-date
PS C:\Python> 