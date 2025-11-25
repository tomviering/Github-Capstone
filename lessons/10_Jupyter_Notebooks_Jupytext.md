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

Now let's convert our `pipeline.py` file to a Jupyter notebook format. We'll use Jupytext's command-line interface to do this.

**Open a terminal or command prompt** (on Windows, you can use Anaconda Prompt; on Mac/Linux, use Terminal). Make sure your conda environment is activated if you're using one.

Navigate to your repository's `code` folder. Copy and paste the following command into your terminal, replacing `path/to/your/repository` with the actual path to your repository:

```bash
cd path/to/your/repository/code
```

For example, if your repository is on your Desktop, the command might look like:
```bash
cd ~/Desktop/githubdesktop_workshop/code
```

Now, let's convert `pipeline.py` to a notebook format and set up the pairing. **Copy and paste this command into your terminal:**

```bash
jupytext --set-formats ipynb,py:percent pipeline.py
```

This command will:
1. Create a `pipeline.ipynb` file from your `pipeline.py`
2. Update `pipeline.py` to include the percent format markers (`# %%`)
3. Set up the pairing so changes to either file sync to the other

After running this command, if you open `pipeline.py` in a text editor, you should see it now has cell markers like this. Note that your file may look slightly different depending on the modifications you've made in previous lessons (such as docstrings, data shape checks, etc.):

```python
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from preprocessing import preprocess_data

# %% [markdown]
# Machine learning pipeline for predicting football player wages.
# Uses K-Nearest Neighbors regression with standardized features.

# %% [markdown]
# --- 1. Load data and define features and target ---

# %%
df = pd.read_csv('../data/football_wages.csv')

# %%
# Use preprocessing function to separate features and target
X, y = preprocess_data(df)

# %% [markdown]
# --- 2. Train / test split ---

# %%
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# %% [markdown]
# --- 3. Build a simple pipeline: scale -> KNN regressor ---

# %%
knn_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=5))
])

# %% [markdown]
# --- 4. Train ---

# %%
knn_pipeline.fit(X_train, y_train)

# %% [markdown]
# --- 5. Evaluate using MAE ---

# %%
y_pred = knn_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

# %%
print(f"Mean Absolute Error (MAE) on test set: {mae:.4f}")

```

Notice how each section is now separated by `# %%` markers. These markers indicate cell boundaries in the notebook.

## Opening and Editing in VS Code

Now that we have the notebook file, you can open it in VS Code. VS Code has excellent support for Jupyter notebooks through an extension.

1. **Install the Jupyter extension**:
   * Open VS Code
   * Click on the Extensions icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X` on Mac)
   * Search for "Jupyter" in the extensions marketplace
   * Install the "Jupyter" extension by Microsoft
   * You may also want to install the "Python" extension if you haven't already

2. **Open VS Code** and navigate to your repository folder (File → Open Folder, or use the `Open in Visual Studio Code` button in GitHub Desktop).

2. **Navigate to the `code` folder** in VS Code's file explorer (left sidebar) and click on `pipeline.ipynb` to open it.

3. VS Code will automatically recognize it as a Jupyter notebook and display it with notebook features. You should see your code organized into cells, with each cell corresponding to a section marked by `# %%` in the Python file.

4. You can now:
   * **Run cells individually** by clicking the "Run Cell" button above each cell, or use `Shift + Enter`
   * **Add markdown cells** for documentation by clicking the "+ Markdown" button
   * **Add new code cells** by clicking the "+ Code" button
   * **Modify existing cells** by clicking on them and editing directly
   * **See cell outputs** displayed inline below each cell

> **Note**: If VS Code prompts you to select a Python interpreter, make sure to select your conda environment (the one where you installed Jupytext). You can do this by clicking on the Python version in the bottom-right corner of VS Code, or by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and typing "Python: Select Interpreter".


Any changes you make in VS Code will automatically sync to the `pipeline.py` file (and vice versa) because of the pairing we set up.

## Working with the Converted File in Git

Let's see how this looks in GitHub Desktop. Go back to GitHub Desktop and check the `Changes` tab. You should see that `pipeline.py` is listed as a changed file. Notice that `pipeline.ipynb` is not listed - that's because we added it to `.gitignore`, so Git is ignoring it.

Click on `pipeline.py` to see the diff. Notice how readable the changes are! Instead of seeing JSON structure, you can clearly see:
* The `# %%` cell markers that were added
* The actual code content
* Any modifications you might have made

This is exactly what makes Jupytext so useful for version control. The changes are now in a human-readable format.

Let's make a small edit to demonstrate. Open `pipeline.py` in your text editor and change the number of neighbors in the KNN regressor:

```python
# %%
knn_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=10))  # Changed from 5 to 10
])
```

Save the file and go back to GitHub Desktop. You'll see the change clearly displayed in the diff view. The change is easy to read and understand - you can see exactly what line was modified and what the change was.

Now commit this change with an appropriate message, such as "Convert pipeline.py to Jupyter notebook format using Jupytext" or "Add Jupytext cell markers to pipeline.py".