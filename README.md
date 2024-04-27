# PythonBasics Project

![learning python](Python-logo-notext.svg.png)

This project is about learning basics of Python. We will cover following topics in this project:

- Hello World file
- Variables: basic data types(integer, string, float, boolean)
- Data structures
  - List
  - Dictionary

## Markdown Language

### title text
#### title text
##### title text

This is the **bold text** use double asterisks

In markdown we can format links, [click here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to know more about it.

Markdown is really cool for formatting the coding

Showing sample python code:

```python
print("hello world!")
a=10
b=20
c=a+b
```

Shell scripting sample code:

```shell
cd ~
pwd
ls -l
tail -f /var/log/applogfile.log|grep johnd22
```


### One time git actions in the project:
-When you join the team and you need to start working with existing project you to clone (download) the project to your local PC. Go to the right folder and copy the HTTPS link of the existing github repository:
shell
cd /c/dev/temp
git clone https://github.com/rreilly283/PythonBasics2.git

-Initializing the git repository if you are starting brand new project:
(open the project > Eanble VCS)
by default it creates repository

Mostly used commands:
### Daily used commands/git features
Commit:
<on the project folder> git init(open the project > Enable VCS)
by default git creates  'master' branch

git and filepath
git commit -m 'your Commit message'
git status (pycharm Commit window shows)
git log (pycharm git > log window shows this)

### Daily used commands/git features
- Commit(Pycharm Commit window):
git and filepath
- git commit -m 'your Commit message'

-Setting your user profile:
Pycharm propmpted to set the username details:
username, email
git config -- global user.name "John Doe"
git config -- global user.email "john@leveleupacademy.tech"

-Logs(pycharm git > Log window shows this)
git log

-Pushing the changes and all commits to the Server (github - cloud) to shae with everyone
PyCharm > Git > Git Push
Manage remote: set origin:main
Origin: https://github.com/rreilly283/PythonBasics2.git
connection: master -> origin: main
```git 
git push
```

- Project will have some changes from other collaborators/qa engineers so you need to get the updates from gitHub. This change particularly needs to be pulled first even though you have commits on your local repository.

- Branching: creating the local or remote brances to work on your own draft/copy/task. You will name your branch and branch will be created base on current branch, then new branch and current branch becomes independent copies of the project. Usually when new branch is created git will automatically swith to new branch (checkou to new branch)
- Switching to existing branch is called Checkout. YOu can easily switch between branches in Pycharm
