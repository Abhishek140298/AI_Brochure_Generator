# AI_Brochure_Generator
Creates a short, engaging marketing brochure for prospective customers.
# Project 1: AI Brochure Generator

An AI-powered tool that scrapes a company's website and automatically generates a short, engaging marketing brochure — intelligently deciding which sub-pages (About, Careers, etc.) are worth including, not just the homepage.

## What it does

1. Scrapes a given company URL for its visible text content
2. Extracts all links on the page
3. Uses GPT-4o mini to decide which links are relevant for a brochure (About, Careers, Company, Team) and filters out irrelevant ones (Terms of Service, social media, etc.)
4. Scrapes each relevant sub-page and combines all the content
5. Sends the combined content to GPT-4o mini with a system prompt instructing it to write a brochure in markdown

## Why it's interesting

Most basic AI scripts just take one input and generate one output. This project chains **two separate AI calls** together:
- The first call reasons about *structure* (which links matter) and returns structured JSON output
- The second call performs the actual *generation* task (writing the brochure) using the results of the first

This pattern — using an LLM to make a decision that shapes what happens next in your pipeline — is a building block for the more advanced agentic systems built later in this course.

## Tech stack

- **Python 3**
- **`requests`** — fetches raw HTML from a URL
- **`beautifulsoup4`** — parses HTML into clean, extractable text and links
- **`openai`** — calls GPT-4o mini for both link selection (JSON mode) and brochure generation
- **`python-dotenv`** — loads the API key securely from a `.env` file

## Project structure

```
llm-engineering/
├── scraper.py      # scrape_website() and get_links() functions
├── brochure.py      # link selection + brochure generation logic
├── .env              # holds OPENAI_API_KEY (not committed to git)
└── .gitignore        # excludes .env and venv/ from version control
```

## How to run

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
2. Make sure `.env` contains your API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```
3. Run the brochure generator:
   ```bash
   python3 brochure.py
   ```

By default it generates a brochure for `https://anthropic.com` — change the URL in the `if __name__ == "__main__":` block at the bottom of `brochure.py` to try it on any company website.

## Key concepts learned

- **System vs. user prompts** — shaping model behavior vs. asking the actual question
- **Prompt construction** — combining dynamic scraped data with a fixed instruction
- **Structured (JSON) output** — forcing the model to return machine-readable data with `response_format={"type": "json_object"}`
- **Modular code** — splitting scraping and generation logic across files and importing between them
- **Defensive coding** — using `try/except` so one broken link doesn't crash the whole pipeline
- **Context window management** — trimming scraped text to stay within reasonable token limits

