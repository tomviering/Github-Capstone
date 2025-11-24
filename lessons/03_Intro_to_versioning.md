---
layout: default
title: "Introduction to Versioning"
author: "Daniel van Strien, Radhika Khetani, Bob Freeman, Meeta Mistry, Kathleen Keating, Amir Karger"
---

#  Versioning your Data and Scripts

## Learning Objectives

* Explain the need for version control

## What is Version Control?

Version control can be used to keep track of versions of a piece of work that either a single person is working on, or a shared document. It is designed to avoid a situation like the one noted below.

```
mydocument.txt
mydocument_v2.txt
mydocument_v3_rev-BHP.txt
mydocument_v8_Final?.txt
```

Some tools let us deal with this a bit better without creating a brand new file for every "save". For example, using Microsoft Word's "Track Changes" allows us to highlight the changes that are being made within the document. This can be helpful for when collaborating on a document so other people can see the changes being made. Alternatively, DropBox and Google Docs have a built-in "version history" feature which keeps older versions of documents (up to a certain point in time) so that you can revert back to if need be.

**Version control systems** on the other hand start with a base version of the document and then **save only the changes you made at each step** of the way by taking a so-called "snapshot". A snapshot records information about when a file was saved, and all the differences between the current document and the previous version. The user (you) decides when these snapshots are collected, and this allows one to ‘rewind’ your file to an older version. 

<img src="../img/play-changes.png" width="600" align="center">

Version control is also very useful when collaborating. For example, two users can make independent sets of changes based on the same document and each have separate snapshots documenting their changes.

<img src="../img/versions.png" width="400" align="center">

If there aren't any conflicts (i.e updates to the same line), the two sets of changes can be "merged" back into the same base document.

<img src="../img/merged_example.png" width="400" align="center">

### Version Control Systems and Hosts

In this class we will be focusing on [Git](https://git-scm.com/). Git is usually used for version control on a local computer and you do not need internet access to use it - so you can also work offline. Only when you want to share your updates on your project (or receive them), you will need to be online. 

GitHub is currently the most popular host of open source projects and is often used in AI and machine learning. This is why we will use GitHub. 

## Why use Version Control?

The two main reasons to use version control are to:

* Manage text/data/code effectively 
* Collaborate efficiently

It was originally developed for working on code together. However, it also works well when working on text documents (such as `.txt`,`.md` or `.tex` files). It is not recommended to use Git in combination with Microsoft Word or Powerpoint. 

**Why Not use Dropbox or Google Drive?**

Dropbox, Google Drive and other services offer some form of version control in their systems. Benefits of collaborating with Version Control include:

* Supports both text and programming languages
* Allows comments on every modification
* Allows you and others to navigate the history easily
* Robust conflict resolution (working on the same file does not lead to loss of data)

***

**Are you done?** Go to the next lesson: [04 GitHub Desktop](https://github.com/tomviering/Github-Capstone/blob/master/lessons/04_GitHub_desktop.md)

* Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). These materials are also licensed under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
