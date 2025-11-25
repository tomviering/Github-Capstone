## Learning objectives
In this lesson you will:

* Learn what Jupytext is and why it's useful for version control
* Install and configure Jupytext
* Convert Python scripts to Jupyter notebooks using Jupytext
* Work with Jupyter notebooks in Git/GitHub Desktop

## The Problem with Jupyter Notebooks in Git

Jupyter notebooks are excellent for interactive data analysis and exploration. However, when it comes to version control with Git, they present a significant challenge. Jupyter notebook files (`.ipynb`) are stored as JSON files, which makes them difficult to work with in Git:

* **Hard to read diffs**: When you view changes in Git, you see JSON structure rather than the actual code changes
* **Merge conflicts**: JSON format makes resolving conflicts between different versions very difficult
* **Large diffs**: Even small changes can result in large diffs because the entire notebook structure is stored in JSON

This makes collaboration on notebooks challenging and makes it hard to review changes in pull requests.

## What is Jupytext?

**Jupytext** is a tool that solves this problem by allowing Jupyter notebooks to be represented as plain text files. Instead of storing notebooks as JSON, Jupytext can convert them to Python scripts (or other formats) that use special markers to indicate cell boundaries. This means:

* **Readable diffs**: Changes show up as normal code changes, making it easy to see what was modified
* **Easy collaboration**: Multiple people can work on notebooks without complex merge conflicts
* **Version control friendly**: Git can properly track and diff the changes

Jupytext supports several formats, but we'll focus on the **percent format**, which uses `# %%` markers to separate cells. This format is widely supported and easy to read.

## Installing Jupytext

Before we can use Jupytext, we need to install it. First, make sure you have your conda environment activated (if you're using conda). If you haven't set up your Python environment yet, please follow the instructions in [How to use Python on your own laptop](https://brightspace.tudelft.nl/d2l/le/content/775697/viewContent/4424059/View) to set up Anaconda and create a conda environment.

Once your conda environment is activated, install Jupytext using conda:

```bash
conda install -c conda-forge jupytext
```



To verify that Jupytext is installed correctly, you can check the version:

```bash
jupytext --version
```

You should see the version number displayed. If you get an error, make sure Jupytext is installed in the same Python environment that you're using, and that your conda environment is activated.

## Configuring Jupytext

Jupytext can be configured to automatically pair notebooks with text files. For this lesson, we'll configure it to use the percent format by default. 

Create a configuration file called `.jupytext.toml` in the root of your repository (the same folder where your `README.md` is located). Add the following content:

```toml
default_jupytext_formats = "ipynb,py:percent"
```

This configuration tells Jupytext to:
* Keep the original `.ipynb` file
* Create a paired `.py` file in percent format
* Automatically sync changes between the two files

## Ignoring .ipynb Files in Git

Before we convert our Python file to a notebook, let's set up Git to ignore `.ipynb` files. This way, the `.ipynb` files will stay on your local machine for you to work with, but won't be tracked by Git. This ensures that only the readable `.py` files (with `# %%` markers) are committed to version control.

1. **Check if you already have a `.gitignore` file** in the root of your repository (the same folder where your `README.md` is located). If you don't have one, create it. If you already have a `.gitignore` file (which you might have created in earlier lessons), open it for editing.

2. **Add the following line** to the `.gitignore` file:

```
*.ipynb
```

This tells Git to ignore all `.ipynb` files in your repository.

3. **Save the `.gitignore` file**.

Now, when we create notebook files, they will automatically be ignored by Git, and only the `.py` files will be tracked. This gives you the best of both worlds: you can work with notebooks locally, and Git will only track the readable `.py` files.

## Converting pipeline.py to a Notebook

Now let's convert our `pipeline.py` file to a Jupyter notebook format and set up automatic pairing.

1. **Open VS Code** and navigate to your repository folder (File → Open Folder, or use the `Open in Visual Studio Code` button in GitHub Desktop).

2. **Install the required extensions**:
   * Click on the Extensions icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X` on Mac)
   * Search for and install:
     - **"Jupyter"** extension by Microsoft
     - **"Jupytext Sync"** extension 
   * You may also want to install the "Python" extension if you haven't already

3. **Navigate to the `code` folder** in VS Code's file explorer (left sidebar).

4. **Create a new Jupyter notebook**: 
   * Right-click in the `code` folder in the file explorer
   * Select "New File"
   * Name it `pipeline.ipynb` (make sure it has the `.ipynb` extension and the same base name as `pipeline.py`)

5. **Open both files**: Open both `pipeline.py` and `pipeline.ipynb` in VS Code (you can have them in separate tabs).

6. **Copy the code from `pipeline.py` to the notebook**:
   * In `pipeline.py`, select all the code (`Ctrl+A` / `Cmd+A`) and copy it (`Ctrl+C` / `Cmd+C`)
   * In `pipeline.ipynb`, paste the code into the first cell

7. **Save the notebook** (`Ctrl+S` / `Cmd+S`).

8. **The Jupytext Sync extension will automatically pair them**: Because you have the `.jupytext.toml` configuration file in your repository root with `default_jupytext_formats = "ipynb,py:percent"`, the Jupytext Sync extension will automatically detect that these files should be paired. 

   When you save either file, changes will automatically sync to the other! The extension reads your `.jupytext.toml` configuration, so it knows how to pair the files.

9. **Verify the pairing**: After saving, the `pipeline.py` file should automatically be updated with `# %%` cell markers. You can check this by looking at `pipeline.py` - it should now have cell markers separating the code sections.


After the pairing is set up and you've saved the notebook, if you open `pipeline.py` in a text editor, you should see it now has cell markers like this. Note that your file may look slightly different depending on the modifications you've made in previous lessons and how you split up the code into cells:

```python
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %% vscode={"languageId": "plaintext"}
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# %% vscode={"languageId": "plaintext"}
# 1. Load data + define features and target
df = pd.read_csv('../data/football_wages.csv')

# Drop categorical column and target
X = df.drop(columns=["log_wages", "nationality_name"])
y = df["log_wages"]

# %% vscode={"languageId": "plaintext"}
# 2. Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# %% vscode={"languageId": "plaintext"}
# 3. Build KNN pipeline
knn_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=5))
])

# %% vscode={"languageId": "plaintext"}
# 4. Train the model
knn_pipeline.fit(X_train, y_train)

# %% vscode={"languageId": "plaintext"}
# 5. Evaluate using MAE
y_pred = knn_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error (MAE) on test set: {mae:.4f}")

# %%

```

Notice how each section is now separated by `# %%` markers. These markers indicate cell boundaries in the notebook.

## Working with the Paired Notebook in VS Code

Now that the pairing is set up, you can work with the notebook just like any other Jupyter notebook. VS Code will automatically recognize it and display it with notebook features. You should see your code organized into cells, with each cell corresponding to a section marked by `# %%` in the Python file.

You can now:
* **Run cells individually** by clicking the "Run Cell" button above each cell, or use `Shift + Enter`
* **Add markdown cells** for documentation by clicking the "+ Markdown" button
* **Add new code cells** by clicking the "+ Code" button
* **Modify existing cells** by clicking on them and editing directly
* **See cell outputs** displayed inline below each cell

> **Note**: If VS Code prompts you to select a Python interpreter, make sure to select your conda environment (the one where you installed Jupytext). You can do this by clicking on the Python version in the bottom-right corner of VS Code, or by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and typing "Python: Select Interpreter".

## Working with the Converted File in Git

Let's see how this looks in GitHub Desktop. Go back to GitHub Desktop and check the `Changes` tab. You should see that `pipeline.py` is listed as a changed file. Notice that `pipeline.ipynb` is not listed - that's because we added it to `.gitignore`, so Git is ignoring it.

Click on `pipeline.py` to see the diff. Notice how readable the changes are! Instead of seeing JSON structure, you can clearly see:
* The `# %%` cell markers that were added
* The actual code content
* Any modifications you might have made

This is exactly what makes Jupytext so useful for version control. The changes are now in a human-readable format.

Let's make a small edit to demonstrate. In the `pipeline.ipynb` notebook, find the cell that contains the pipeline definition and change the number of neighbors in the KNN regressor from 5 to 10:

```python
knn_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=10))  # Changed from 5 to 10
])
```

Save the notebook. The Jupytext Sync extension will automatically sync this change to the `pipeline.py` file. Now go back to GitHub Desktop and check the `Changes` tab. You'll see the change clearly displayed in the diff view for `pipeline.py`. The change is easy to read and understand - you can see exactly what line was modified and what the change was.

Now commit this change with an appropriate message, such as "Convert pipeline.py to Jupyter notebook format using Jupytext" or "Add Jupytext cell markers to pipeline.py".