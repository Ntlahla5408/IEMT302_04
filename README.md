# South African News Headline Scraper

A small Python web-scraping exercise that retrieves news headlines from the SAnews website and displays them in the terminal.

## Overview

This project demonstrates how to use Python, Requests and Beautiful Soup to retrieve and parse webpage content. It was completed as a learning exercise covering web scraping, Python environments, dependency management and Git/GitHub workflows.

## What I Learned

### Git and GitHub

- Creating and managing a Git repository.
- Committing changes and pushing them to GitHub.
- Using a `.gitignore` file to exclude virtual environments and unnecessary files.
- Using `requirements.txt` to document project dependencies.

### Python Virtual Environments

Create and activate a virtual environment:

```bash
py -m venv venv
```

Install the required packages:

```bash
pip install -r requirements.txt
```

A virtual environment keeps this project's dependencies separate from other Python projects.

### Web Scraping

The exercise covers how to:

- Send HTTP requests with the `requests` library.
- Retrieve a webpage's HTML.
- Parse HTML with Beautiful Soup.
- Find HTML elements and extract their text.

### Problem Solving

During the exercise, I worked through issues involving missing packages, Python interpreter selection, import errors and repository structure. Resolving these issues strengthened my debugging and troubleshooting skills.

## Requirements

- Python
- Requests
- Beautiful Soup 4

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Script

```bash
py scrape.py
```

The script retrieves South African news headlines from SAnews and prints them in the terminal.

## Technologies Used

- Python
- Requests
- Beautiful Soup 4
- Git and GitHub

---

*Academic learning exercise.*
