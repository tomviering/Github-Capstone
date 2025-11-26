## Learning Objectives
* Sync local and remote versions of a Git repository
* Make changes to a git repository on GitHub (editing, adding and deleting files)
* Sync local and remote versions of a Git repository
* Access version history of a given file or repository

## Repositories online (remote)

### Pushing Your Changes to Your Remote Repository

In the last lesson we were only recording our changes locally (on your computer), but we may want to have these changes be available remotely (online) as well for our collaborators or as backup. The idea is you keep your local and remote repositories up-to-date with eachother.

At the end of the last lesson, we took the first step to synchronizing your repository locally and remotely by publishing it to GitHub's servers, but any further changes you make locally through GitHub Desktop will remain local and not appear remotely until they are **push**ed to GitHub's servers. Any time you make local changes, you might notice the right-hand tab on the repository bar will say `Push origin`. `Origin` is the default name for your remote repository. Clicking this button will enact a one-way synchronization which will **push** your changes in your repository from your computer to GitHub, and populate the *remote* repository on GitHub's servers in the process.

At the end of the last lesson, we saw our repository on our *Repositories* tab on [GitHub](https://github.com/). If you click on your repository, we can now remotely view our changes on GitHub (if you don't want to navigate there by hand, in GitHub Desktop you can go to `Repository` in the menu bar, then select `View on GitHub` and it will automatically open the repository on GitHub for you: 

<p align="center">
  <img src="../img/2.GHD_githubweb_repo.png" width="800">
</p>

Notice that our short commit descriptions are shown here, and that we can see the different commits that we performed.

On GitHub, you can choose to keep repositories public or make them private; and if they are private, you can choose specific GitHub users with whom you want to share it or collaborate with.

Once your document is online, you can continue to make local changes to your file. But you will have to synchronize your local changes to reflect these changes in the published GitHub repository. Git stores changes both locally (on your computer) and remotely (on GitHub servers), and it is important to keep these changes in sync. 

In GitHub Desktop and standard Git workflows, this is accomplished by regular, intentional rounds of **Pull** and **Push**, which **pulls** in changes from the remote repository, and **push**es any local changes to the remote repository.

## Making Changes Remotely

We now have our work both locally on our computers and online in the GitHub web interface. So far any edits we have made to our files have been directly on the local versions and then we pushed the changes to the online repository. It is also possible to **make a change to your repository on the web interface**. 

To demonstrate how to do this, we will edit one of the files in our **`code`** folder. Inside this folder we have several scripts and we realized that we forgot to give attribution to our functions in the `preprocessing.py` file.

Navigate to the **githubdesktop_workshop** repository online in GitHub.

Go into the `code` directory, and click on the name of the file (`preprocessing.py`) in the title area. This will take you to a new page showing your document.

Click on the 'Edit' option or the pencil icon in the top right-hand corner of the document. You will now be able to edit the file and add some new text. **We are going to make two edits to this file!**

1. We want to add some comments above the `preprocess_data` function. This comment provides the resources from which we obtained and adapted this code. You can **copy the text provided below and paste it into your document**.

```
# Preprocess data function
# adapted from https://scikit-learn.org/stable/modules/preprocessing.html
# and https://pandas.pydata.org/docs/user_guide/basics.html
```

2. Next, we will add a docstring to document the function parameters and return values. The **text you need to add is provided below**.

```
"""
Preprocesses the input dataframe by separating features and target variable.

Args:
    df: Input dataframe containing features and target variable
    
Returns:
    Tuple of (X, y) where X is the feature matrix and y is the target vector
"""
```
<p align="center">
  <img src="../img/2.GHD_edit_utils.png" width="800" align="center">
</p>

Once you have made some changes to your file, **click the green** <kbd><b>Commit changes...</b></kbd> **button** in the upper right hand corner of the screen. You will see the option to commit changes, and two associated text entry boxes. The first box is to give your commit a short description of the changes you made. The second box allows you to provide more detailed text about the commit, which is optional.

**Provide an informative description for your commit and then press "Commit changes"**.

<p align="center">
  <img src="../img/2.GHD_commit_utils.png" width="800" align="center">
</p>

## Deleting files online

One can also add and delete files from the repositiory online. To do this, you will first need to view the file itself (by clicking on the file's name). Once you are viewing your file you will see a trashcan icon at the top right-hand side, located to the right of the edit/pencil icon. 

Let's delete one of the files in our `data` folder. Click on the `very_important_file.csv` file in the `data` folder, then click the `...` button in the top right of the screen and select `Delete file`:

<p align="center">
  <img src="../img/2.GHD_delete_py.png" width="800" align="center">
</p>

You will see the screen change, indicating that `This file was deleted`, but the action won't be complete until you **commit** the change; GitHub will track this change just like any other you might make to your repository. Click the green <kbd><b>Commit changes...</b></kbd> button in the upper right. Just as before, GitHub will ask for a commit description. **Provide a description** (or use the suggested one) **and commit this change**.

<p align="center">
  <img src="../img/2.GHD_commit_delete_py.png" width="800" align="center">
</p>

## Adding files to a repository online

We can also **add files and folders to the repository via the web interface**. There are two ways to do this, by uploading existing files or create new files directly in the interface.

### Uploading files

We'll start with adding files through upload. First, we need to create a `docs` folder. In your **githubdesktop_workshop** repository on GitHub, click the <kbd><b>Add file</b></kbd> button in the upper right, then select **`Create new file`**. In the file path box, type `docs/README.md` (this will create the `docs` folder and a README file in it). Add some text like "Documentation folder" and commit this file to create the folder.

Now navigate to the `docs` folder you just created. On this page you will see all of its contents listed, and in the upper right you will see an <kbd><b>Add File</b></kbd> button. If you click on this, you will see two dropdown options appear: `Create new file` and `Upload files`. **Select `Upload files`**. This will take you to a new page.

<p align="center">
  <img src="../img/2.GHD_upload_files.png" width="800" align="center">
</p>
  
For this example, you can upload any PDF file you have on your computer, or create a simple text file. To add a file to the repo using the web interface, you can do one of two things:

1. Find the file in a File Browser window on your computer and then drag and drop it on to this page.
2. Click on the "choose your files" and find/select the file in the window that pops up. 

Once the file is selected, the Upload will require a Description and subsequent Commit:

<p align="center">
  <img src="../img/2.GHD_upload_files_2.png" width="800" align="center">
</p>

After committing, you will be brought back to the main page of your repository, and you'll see your latest commits. If you navigate to the `docs` folder, you should now see the file you uploaded there.

<p align="center">
  <img src="../img/2.GHD_latest_commits_after_upload.png" width="800" align="center">
</p>

## Syncing remote changes to your local repository via Pull

Let's return to our local machine and apply the changes we made online to our local repo. GitHub Desktop has already noticed that our remote repo has changed, and is now prompting that you can `Pull 2 commits form the origin remote` which is highlighted in a blue box with a <kbd><b>Pull origin</b></kbd> button in blue (you can also see that the repository bar has a `Pull origin` option and tells you when the repo was most recently **fetched**.

> Note: **fetch** and **pull** are similar concepts with some important differences. When a repo is **fetched** from remote, it will note changes to your repo but not merge/commit them to your local directory. When you **pull**, it will note these changes **and** merge/commit them to your local directory.

<p align="center">
  <img src="../img/2.GHD_pull_option.png" width="800" align="center">
</p>

Click on the <kbd><b>Pull origin</b></kbd> button, then navigate to the history tab to **view the commits** you just made via the GitHub website. You can click on individual files to see the changes you made:

<p align="center">
  <img src="../img/2.GHD_view_pulled_commits_2.png" width="700" align="center">
</p>

As before, the changes to any text files are highlighted in <span style="color:green">green</span> and <span style="color:red">red</span>.

* <span style="color:red">Red</span> indicates where things have been removed
* <span style="color:green">Green</span> indicates the addition of text 

Now that we've **pull**ed our changes from GitHub, you'll also be able to see any changes in your File Browser directory for the repository.

> **NOTE**: Two important things to keep in mind when making changes on the web interface:
> * On GitHub file changes are done serially, so commits with modifications to multiple files cannot be done here.
> * All of these changes in the web browser are realtime on the GitHub remote, i.e. the commits take effect immediately without an intermediate **add** or **stage** step.

## Viewing File Histories

One very useful feature of GitHub and GitHub Desktop is the ability to see how a file has changed over time.

We've already seen how you can view changes made to files (highlighted in red and green) in GitHub Desktop in a given commit. It's also possible to view a file's entire history through GitHub.

On the repository page of GitHub, navigate to the file whose history you would like to view. In this case, let's go to `pipeline.py` inside of our `code` directory.

<p align="center">
  <img src="../img/2.GHD_view_file_history_web.png" width="700" align="center">
</p>

You'll notice in the upper right there is a `History` button with a symbol of a clock surrounded by an arrow. You can click this to see all commits which relate to this file:

<p align="center">
  <img src="../img/2.GHD_view_file_history_web_2.png" width="700" align="center">
</p>

You'lll notice that for each commit, there are a series of icons on the right hand side. One looks like a **document with `< >`** and the other is simply **`< >`**. Clicking these icons let you see the version of the file in that commit, or the whole repo as it looked in that commit, respectively. Let's click on the **document with `< >`** icon to see the version of `pipeline.py` from the `Update pipeline.py` commit. Notice that in the upper left, the button that usually says `main` now has an alphanumeric code. This code represents a snapshot of your repo at the time of this commit:

<p align="center">
  <img src="../img/2.GHD_view_file_history_scriptlets.png" width="800" align="center">
</p>

You can also see changes from specific commits leading up to/including the "current" (selected) commit by clicking on the `Blame` button in the upper left. It will also show you the author of the commit (useful if you are collaborating with someone on the project):

<p align="center">
  <img src="../img/2.GHD_blame.png" width="800" align="center">
</p>

> Note: you do not have to be in `History` to view `Blame` for a given file.

And if you'd like to view changes side-by-side, color coded as in GitHub Desktop, click the "Back" button in your web browser to go back to the History and then click on the name of the commit. You'll see the changes between this particular commit and the previous one:

<p align="center">
  <img src="../img/2.GHD_view_file_history_colors.png" width="700" align="center">
</p>


To return to your `main` branch, simply click the name of the repository at the very top of the screen. You'll know you're back in `main` because it will be displayed in the upper left above your folders and files.

***

**Are you done?** Go to the next lesson: [04 Conflicts](https://github.com/tomviering/Github-Capstone/blob/master/lessons/04_Managing_conflicts_GitHub_Desktop.md)
