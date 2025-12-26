# YouTube Transcript Summarizer

A simple Python CLI to extract YouTube transcripts and generate concise AI summaries.

This tool:
- Pulls YouTube’s native captions (no scraping, no API keys)
- Summarizes videos into clear bullet points using an LLM
- Works for single videos or recent uploads from a channel
- Copies output directly to your clipboard for easy sharing

## Requirements

- Python 3.10+
- macOS (for clipboard support via `pbcopy`)
- `yt-dlp` installed (`pipx install yt-dlp`)
- An OpenAI API key set in your environment

## Installation

Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
