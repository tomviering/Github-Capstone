## Learning Objectives

* Describe version control
* Implement version control on text file with Git using the GitHub Desktop interface


## Getting Started with Git using a GUI (Graphical User Interface)

We will use [GitHub Desktop](https://desktop.github.com/) for working with Git. 
Since we are going to be using [GitHub](https://github.com/) along with [GitHub Desktop](https://desktop.github.com/) you will need to register for an account on GitHub if we don’t already have one. 

### Install GitHub Desktop

1.  After you have downloaded and installed GitHub desktop, open the application and click the `Sign in to GitHub.com` button

<p align="center">
    <img src="../img/2.GHD_setup1.png" width="700" align="center">
</p>

2. A browser window will open up prompting you to authorize a GitHub User. Sign in to Github or click `Continue` if you are already signed in. Depending on your browser, you may see a pop-up prompting you to open `Open GitHub Desktop`; if you agree you will see a follow-up message redirecting you back to the GitHub Desktop application

<p align="center">
    <img src="../img/2.GHD_setup2.png" width="700" align="center">
</p>

3. On GitHub Desktop, you will see a `Configure Git` prompt which will allow you to use your GitHub account name and email address or configure manually. You should select `Use my GitHub account name and email address` which should auto-fill your GitHub name/email, and click `Finish`

<p align="center">
    <img src="../img/2.GHD_setup3.png" width="700" align="center">
</p>

4. Then you will be directed to a `Let's get started!` prompt. At this point, you've configured GitHub Desktop and are ready to start working with a *repository*.

<p align="center">
    <img src="../img/2.GHD_setup4.png" width="700" align="center">
</p>

## Version Controlling a directory of files

### Creating a Repository

***So, what is a Git repository?***

A repository means a folder with files that you are sharing via Git. Inside the git repository folder, there is a folder called `.git`. This folder is used by Git to track all changes. If you delete the `.git` folder, you will loose all your history (!). When you create a new repo, Git will make this folder for you. 

Some tips and tricks:
* A repository can have many files and sub-folders (basically, a normal folder).
* Best practice is to have a separate repository for each project.
* Do not create repositories for folders within a repository.
* The changes made within repository folders are being "watched" by Git as mentioned above, but this does not mean the updates are sent directly over the internet. For this, you will need GitHub desktop. 
* You can be control the items that Git is "watching". It is best practice to ignore very large datasets, or temporary files; sharing these via Git is not recommended (large files can make Git very slow). 

Download the folder we have generated for this session [from here](https://github.com/tomviering/Github-Capstone/raw/refs/heads/master/repo_example_files.zip), and unzip it in a location of your choosing. We recommend placing it on your Desktop for the duration of this workshop.

### Creating a Folder/Repository, Starting from your Local Machine

There are a number of different ways to add files/folders for Git/GitHub Desktop to track...

**Method 1: In GitHub Desktop, on the `Let's get started!` screen, click `+ Create a new repository on your Local Drive...`**

**Method 2:** In GitHub Desktop, if you are already past the `Let's get started!` screen, click `Current repository` in the lefthand side of the repository bar, then in the dropdown menu that appears, click `Add` and select `Create New Repository...`

**Method 3:** In GitHub Desktop, click `File` in the Menu Bar, then select `New Repository...`

For this tutorial, we will be using **Method 1**

When you create a new local repository, you will be greeted with this prompt:

<p align="center">
    <img src="../img/2.GHD_create_new_repo.png" width="350" align="center">
</p>

Fill in the fields as appropriate:

1. The `Name` of the repository. Keep this to letters, numbers, and underscores; for this class, let's call it "githubdesktop_workshop".
2. Add a `Description` of what this folder/repository will contain.
3. Choose a `Local Path` where the repository will be stored on your computer. For this workshop, let's place the repo on your Desktop
4. If you want, you can Initialize the repository with a README by clicking the box. For this worskop, we will check this option.
5. If you would like to choose options for `Git Ignore` and `License`, there are options from the dropdown menu. For this workshop, we will select `None` for both.
6. Finally, click the `Create Repository` button.

**Make sure you follow all the steps and instructions listed above!**

>**More on `Git Ignore` and `License` options**
> * Selecting the **`Git Ignore`** option will create a hidden file caled .gitignore. This file allows you to specify if there are files which Git should ignore. For example, you want Git to ignore very large files, because Git can get slow with very large files (for example, a file larger than 10Mb-100Mb). 

Voila! You now have your first Git repo!

Your GitHub Desktop screen should now look like this:

<p align="center">
    <img src="../img/2.GHD_layout.png" width="800" align="center">
</p>

### A quick tour of the GitHub Desktop interface
**The black bar on the upper part of the screen is called the repository bar, which has 3 sections:**

**Current Repository** (left) shows name of the current repository, which is the new repository you just created. If you click here, you'll see a dropdown menu to create and navigate between repositories. 

**Current Branch** (middle) displays the current branch. If you click here, it will let you view and switch to different branches in your repository (these will be visible once you create *pull* requests in your repository) or create a new branch. 

**Publish repository** (right). This option appears because we haven't yet published our repo to the GitHub Server, which we'll do later on in the lesson. This part of the repository bar will change depending on the status of your current branch and repository.

**On the left side of the screen you will also see two tabs:**

**Changes** will show you changes made to files in your current directory that haven't been committed to your local repository. This tab also has "Summary" and "Description" text boxes to describe your changes, and a **Commit to BRANCH** button, which will tell you which branch you are committing to. In this case the BRANCH should be "main", so it should say **Commit to main**.

**History** will show past commits you've made to the current branch of your repository. For now, you'll only see the **Initial commit** from creating the repository. You will also see any changes to files you created during the commit; in our case, we see there is a *README.md* as well as a *.gitattributes* file. Our *.gitignore* and *LICENSE* files would also appear here if we opted to create those during the initial commit. When you click on these files, you can see the *diff* -- only the parts of the file that changed are displayed. For the initial commit, that's all of the file.

> **Note 1:** The folder should also appear on your Desktop! If you can't find your folder, you can click on `Show in Finder` in the "View the files of your repository in Finder" section on the main screen
>
> **Note 2:** files like *.gitattributes* or any files which start with a `.` are hidden files, so they may not be visible in your File explorer or Finder. You may need to update your settings to make them visible. 

### Committing Changes

For this workshop, we will be working with the example repository files. The repository should already contain the `code` and `data` folders with example files. If you're starting from the `repo_example_files` folder, these folders are already in place.

In Finder, your repository should look like this:

<p align="center">
    <img src="../img/2.GHD_folders_in_finder.png" width="800" align="center">
</p>

Now, look in your GitHub Desktop application. You can see that these folders and files actually show up on the left hand panel, ready to be committed to your repository:

<p align="center">
    <img src="../img/2.GHD_folders_in_GHD.png" width="800" align="center">
</p>

You'll notice that GitHub Desktop will actually show you any changes you made to these files on the right hand side of the panel. You can click on each file to review these changes.

>Note: Wait a minute, where is the `reports` folder? Git will ignore folders that are empty. 

>Note: To the right of each file, you'll see a `+` in a box. This indicates that these are newly added files. If you were to delete a file, you would see a `-`, and if you modify an existing file, you'll see a `dot`

These changes have been noted, but this new *version* of the repository is not yet been recorded (saved) by Git. A **commit** tells Git that you made some changes which you want to record. Though a **commit** seems similar to saving a file, there are different aims behind ‘committing’ changes compared to saving changes. **Commits** take a snapshot of the file(s) at that point. You can actually record or commit modifications to multiple files/folders at once. i.e. single commit can have multiple updates.  

Committing changes usually happens in 2 stages:
1. `add` or stage one or many modifications incrementally
2. `commit` them with a special commit message to document the type of updates

GitHub Desktop automatically **adds**, or **stages**, any changes we make to the repository and displays them on the left hand side of the application. You have the option of excluding any of these changes from the **commit** by deselecting the check box to the left of each file.

To **commit** these changes one **must give a summary of the changes** in the `summary` box at the bottom of the left panel, followed by clicking on the <kbd>Commit to <b>main</b></kbd> button. You can also add a longer description, but this is optional.

After the commit, your screen will return to how it looked before, but it will tell you the name and how recently you made your last commit. The changes to your files will no longer be displayed, because they have been committed. You'll have an option to `undo` the commit in the bottom left if you'd like to go back.  Here is how your GitHub Desktop application will look after your first commit (in this case, the summary was `My first commit!`:

<p align="center">
    <img src="../img/2.GHD_first_commit.png" width="800" align="center">
</p>


A useful way to think about commits is as the "history" of your project. Each commit records a development or change made to the documents in your repository; the history of the project can be traced back by looking at all of the commits. You can directly view this `History` by clicking on the `History` tab on the left hand side of the application:

<p align="center">
    <img src="../img/2.GHD_first_commit_history.png" width="800" align="center">
</p>


* We recommend to commit regularly
* Make the commits "atomic", i.e. **commit a few related changes together**; this will help if you have to revert back to a specific version/snapshot. 
* Use meaningful **commit summaries** and **messages**, so that your messages/summaries are independently understandable by your collaborators and your future self.

> **Note about Branches**:
>
> When you commit you will see <code>commit to <b>main</b></code>. This refers to the **main** branch. 
> 
> Within a Git repository it is possible to have multiple ‘branches’. These different branches are essentially different (virtual) places in which to work. Often they are used to test new ideas or work on a particular feature without modifying or "contaminating" the master copy (e.g. current release of software). This feature is very useful when collaborating with others. We will go into this aspect of Version Control later in this workshop.

### Changing File Contents and Committing Changes

We're going to make several sets of changes that reflect the flexibility and capability of a version control system. 

> **Text Editors:**
>
> When creating a plain text document, you will want to use a text editor like VS Code, Sublime Text (Mac) or NotePad++ (Windows) instead of Microscoft Word (!). You will also want to make sure that you save it as plain text. If you don't have time to install these editors now, you can always use TextEdit (Mac) or Notepad (Windows).

Let's open the `README.md` document using our favorite text editor (see note above about text editors) and make this more useful. The information in this document is displayed at the bottom of the main page of your repo when you view it on GitHub (online). The `.md` extension means that this is a text file in ["markdown" format](https://guides.github.com/features/mastering-markdown/), which GitHub automatically renders into readable HTML pages.

> README files are an essential part of any analysis workflow, so that your future self or your collaborators are able to understand what they need to know. 

To open your `README.md` file, you can either click on it directly in File Browser, or you can click the `Open in Visual Studio Code` (or other text editor if that's your preference) button in the `Open the repository in your external editor` box in the middle of your GitHub Desktop when you are on the "Changes" tab. This will open the whole repository within your text editor, and you can select your README file within the editor from the menu on the left.

Open the `README.md` file and add your own name to the list of group members.
Save the changes to your file.

Let's also open the `pipeline.py file` from within the `code` folder. You'll notice we have a working ML pipeline here.
Update the code such that the `age` column is also dropped from the dataframe.

Save this file as well, and go back to GitHub Desktop. You'll see that your README.md and pipeline.py files are in the left-hand panel with the modified indicator to the right of the file: 

<p align="center">
    <img src="../img/2.GHD_modified_files.png" width="800" align="center">
</p>

If you click on these files, you can review the changes you've made. For text-based files, anything highlighted in green is being added to the file, while anything highlighted in red is being removed from the pre-existing file. Anything unchanged will not be highlighted.

As before, this is GitHub Desktop's way of **adding**/**staging** these changes, but they haven't yet been recorded in an official `snapshot` of your repository. To **commit** these changes to your repository and make an official record of them, you'll need to add a summary and click <kbd>Commit to <b>main</b></kbd>, just as we did before.

**Staging** basically means that you are making your changes ready to be committed. You can add several changes in the staging area, and only **commit** when you are ready. 

Since we wish to keep all the different types of changes as separate commits, we will first commit the documentation change to the README file, and then the code change in the python file. 

First, deselect the `pipeline.py` file so only the `README.md` file has a checkbox, and, as we did with our previous initial commit, include a summary message (you'll notice that GitHub Desktop has conveniently suggested `Update README.md` for us), and click on the Commit button:

<p align="center">
    <img src="../img/2.GHD_commit_readme.png" width="800" align="center">
</p>

Again, you'll see this latest commit in the lower left hand corner. Now, select the changed python file and include a meaningful change message (feel free to use the one suggested by GitHub Desktop), and click <kbd>Commit to <b>main</b></kbd>. You'll see the latest commit in the lower left again. 

But what if we want to see our previous commits? We can access all of our previous commits by clicking the `History` tab in the left hand panel:

<p align="center">
<img src="../img/2.GHD_history.png" width="800" align="center">
</p>

There may be times, however, when we wish to ensure that we save a coordinated set of changes. For example, if we want to make coordinated changes to multiple files it makes sense to make the changes and then stage (add) and commit all the updated files all together (**atomic commit**). 

Let's say we want to refactor our code by extracting the data preprocessing logic into a separate module. We'll update the `pipeline.py` file to import a preprocessing function and create a new `preprocessing.py` file to contain that function. 

1. Let's update the part 1 of `pipeline.py` file with the following and save it:

```Py
from preprocessing import preprocess_data

# --- 1. Define features and target ---

df = pd.read_csv('../data/football_wages.csv')

# Drop categorical columns (here: nationality_name) and the target from X
X, y = preprocess_data(df)
```

2. Now, let's create a new file `preprocessing.py` in the code folder. Put the following code in there and save it:

```Py
import pandas as pd
from typing import Tuple

def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    X = df.drop(columns=["log_wages", "nationality_name", "age"])
    y = df["log_wages"]
    return X, y
```

When we return to the GitHub Desktop application, it has noticed the two changes. Since the change in the main code file depends on the presence of this other file, we need to ensure this commit (snapshot) captures these inter-dependent changes. So, let's keep both files selected for staging, give a meaningful commit message reflecting this process, and then commit! 

<p align="center">
    <img src="../img/2.GHD_atomic_commit.png" width="800" align="center">
</p>

### Publishing your local Git repository remotely to github.com

One last thing: It's all well and done to have a git repo on your computer, but to take full advantage of GitHub's tracking and sharing capabilities, we should publish our repository to <a href="https://github.com">GitHub</a>. To do so, simply click the `Publish repository` tab on the right-hand side of the repository bar. A window will pop up which will allow you to make changes to the repository name and description, as well as choose the organization (the default is `None` which will publish the repository to your personal GitHub account). You can also select whether to keep the code private or make it public. Once you've made any changes, click the `Publish Repository` button:

<p align="center">
    <img src="../img/2.GHD_publish_repo.png" width="800" align="center">
</p>

This will only take a moment. And you'll notice that the `Publish repository` tab in the repository bar now says `Fetch origin.` We'll cover the concept of Fetching at a later time.

Go to <a href="https://github.com">GitHub</a> and left-click your profile picture in the top right corner, then select "Your profile". Once you are on your GitHub profile page and click `Repositories` from the bar up top, you'll see your newly published GitHub repository:


<p align="center">
    <img src="../img/2.GHD_githubweb.png" width="800" align="center">
</p>

***

**Exercise #1**

1. Create a repository `capstone_groupX` in GitHub Desktop. Replace `X` with your group number. Make sure to create it both locally and then publish it remotely onto GitHub.
2. Find the folder on your local computer, and make a Readme file. 
3. Go to GitHub Desktop, commit the change with an appropriate message.
4. Switch repos back to the `githubdesktop_workshop` repo.

***

**Are you done?** Go to the next lesson: [03 Syncing](https://github.com/tomviering/Github-Capstone/blob/master/lessons/03_GitHub_Dekstop_remote1.md)
