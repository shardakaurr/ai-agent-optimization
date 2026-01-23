# Manual Baseline Experiment

## Prompt Used
Write a step-by-step user guide for beginners on how to create a GitHub repository and push code from a local computer.

## AI Output
Below is a **beginner-friendly, step-by-step guide** to help you create a GitHub repository and push code from your local computer. I’ll explain everything clearly, assuming **no prior Git/GitHub experience**.

---

## PART 1: Prerequisites (One-time setup)

### 1. Create a GitHub account

1. Go to **github.com**
2. Click **Sign up**
3. Create your account and verify your email

---

### 2. Install Git on your computer

Git is the tool that connects your computer to GitHub.

#### For Windows

1. Go to **git-scm.com**
2. Download Git for Windows
3. Install with default settings
4. Restart your computer if asked

#### For Mac

* Open **Terminal** and type:

```bash
git --version
```

* If Git is not installed, macOS will prompt you to install it.

---

### 3. Check Git installation

Open **Terminal (Mac/Linux)** or **Git Bash (Windows)** and run:

```bash
git --version
```

If you see a version number, Git is installed correctly.

---

## PART 2: Create a Repository on GitHub (Online)

### Step 1: Log in to GitHub

* Go to **github.com**
* Sign in

---

### Step 2: Create a new repository

1. Click the **“+”** icon (top-right)
2. Select **New repository**

---

### Step 3: Fill repository details

* **Repository name:** `my-first-repo` (example)
* **Description:** (optional)
* Choose **Public** (recommended for learning)
* ❌ Do **NOT** check “Initialize with README” (important for beginners)

Click **Create repository**

👉 GitHub will now show instructions. **Keep this page open.**

---

## PART 3: Prepare Your Local Project

### Step 1: Create a project folder

1. Create a folder on your computer
   Example:
   `Desktop → my-first-repo`

2. Add any file inside it:

   * `index.html`
   * `app.py`
   * `main.java`
   * or any code file

---

### Step 2: Open Terminal / Git Bash in the folder

#### Windows

* Right-click inside the folder
* Click **Git Bash Here**

#### Mac/Linux

* Open Terminal
* Navigate to the folder:

```bash
cd Desktop/my-first-repo
```

---

## PART 4: Initialize Git Locally

### Step 1: Initialize Git

```bash
git init
```

This makes your folder a Git repository.

---

### Step 2: Check status

```bash
git status
```

You’ll see your files listed as **untracked**.

---

### Step 3: Add files to Git

Add all files:

```bash
git add .
```

---

### Step 4: Commit your changes

```bash
git commit -m "Initial commit"
```

This saves a snapshot of your code.

---

## PART 5: Connect Local Repo to GitHub

### Step 1: Copy GitHub repository URL

From GitHub repo page:

* Click **Code**
* Copy the **HTTPS URL**
  Example:

```
https://github.com/username/my-first-repo.git
```

---

### Step 2: Add remote origin

In Terminal / Git Bash:

```bash
git remote add origin https://github.com/username/my-first-repo.git
```

Check connection:

```bash
git remote -v
```

---

## PART 6: Push Code to GitHub

### Step 1: Push for the first time

```bash
git branch -M main
git push -u origin main
```

---

### Step 2: Login to GitHub

* Enter your **GitHub username**
* Enter **GitHub Personal Access Token** (not password)

> ⚠️ GitHub no longer allows passwords. You must create a **Personal Access Token**.

---

## PART 7: Create GitHub Token (If Asked)

### Steps:

1. GitHub → **Settings**
2. **Developer settings**
3. **Personal access tokens**
4. **Generate new token**
5. Select:

   * ✅ repo
6. Generate and copy token

📌 Use this token as **password** when pushing code.

---

## PART 8: Verify on GitHub

1. Refresh your GitHub repository page
2. 🎉 Your files are now visible online!

---

## PART 9: Future Updates (Daily Use)

Whenever you change code:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

---

## Common Beginner Mistakes (Avoid These)

❌ Forgetting `git add .`
❌ Repo name mismatch
❌ Using GitHub password instead of token
❌ Not committing before pushing

---

## Quick Command Summary

```bash
git init
git add .
git commit -m "message"
git remote add origin <repo-url>
git push -u origin main
```

---

If you want, I can also:

* Explain **Git vs GitHub** simply
* Create a **one-page cheat sheet**
* Show **GitHub Desktop (no terminal) method**
* Help you push **Python / Java / Web project**

Just tell me 👍


## Observations
- Clarity: The guide is very clear, well structured, and beginner friendly. Each part is separated logically and easy to follow.
- Missing steps: Git configuration steps such as setting username and email are missing. Verification after push could also be explained more clearly.
- Incorrect information: The instructions are mostly correct, but the explanation about authentication could vary depending on system setup.
- Formatting issues: The document is long and could be slightly simplified or summarized for faster reading. Some sections may be repetitive for beginners.
- Any hallucinations: No obvious hallucinations or fake commands were observed.
- Overall quality rating (1–5): 4



