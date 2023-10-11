# Scrape the Web with entities extraction using OpenAI Function

## What is this?

This codebase allows you to scrape any website and extract relevant data points easily using [OpenAI Functions](https://openai.com/blog/function-calling-and-other-api-updates) and [LangChain](https://python.langchain.com/docs/get_started/introduction).
Create a schema in `schemas.py`, pick a url, and use them with `scrape_with_playwright()` in `main.py` to start scraping.

Tip: each website has the bulk of content either in `<p>`, `<span>` or `<h>` tags. For best performance, choose a combination of tags that work for you.

## Setup

### 1. Create a new Python virtual environment

`conda create -p venv python=3.11 -y`

### 2. Install dependencies 

Run `pip install -r requirements.txt`


### 3. Create a new `constants.py` file to store OpenAI's API key

```text
OPENAI_API_KEY=XXXXXX
```

### Run locally

```bash
python main.py
```


