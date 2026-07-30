# IEMT302_04# Second Repo Experiment - Beautiful Soup Web Scraping

## Overview

This project demonstrates how to use Python, Requests and Beautiful Soup to extract information from a website. The program retrieves the latest South African news headlines from the SAnews website and displays them in the terminal.

## What I Learned

During this exercise I learned several important concepts about Git, GitHub and Python development.

### Git and GitHub

- How to create and manage a Git repository.
- How to commit changes and push them to GitHub.
- Why a `.gitignore` file is important for excluding virtual environments and unnecessary files.
- How `requirements.txt` allows others to install the required Python packages quickly.

### Python Virtual Environments

I learned how to create and activate a virtual environment using:

```bash
py -m venv venv
```

and install project dependencies using:

```bash
pip install -r requirements.txt
```

This keeps project dependencies isolated from other Python projects.

### Web Scraping

I learned how to:

- Send HTTP requests using the `requests` library.
- Download the HTML of a webpage.
- Parse HTML using Beautiful Soup.
- Search HTML elements using methods such as `find_all()`.
- Extract text from HTML tags.

### Problem Solving

While completing this project I encountered several issues including:

- Missing Python packages.
- Using the wrong Python interpreter.
- Import errors.
- Incorrect Beautiful Soup imports.
- Incorrect Git repository structure.

Working through these problems improved my understanding of debugging Python applications.

## Requirements

Install the required packages.

```bash
pip install -r requirements.txt
```

## Running the Program

```bash
py scrape.py
```

The program downloads the latest South African news headlines and prints them to the console.

## Technologies Used

- Python
- Requests
- Beautiful Soup 4
- Git
- GitHub
