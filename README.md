# YouTube Transcript Summarizer

A simple Python CLI for extracting YouTube transcripts and generating concise AI summaries.

This tool is designed for fast research, note-taking, and content triage. It pulls YouTube’s native captions when available, summarizes videos into short bullet points, and copies the output directly to your clipboard.

## What this does

- Extracts YouTube’s native transcripts (no scraping, no YouTube API keys)
- Summarizes videos into exactly 3 concise bullet points
- Works for a single video or the most recent videos from a channel
- Prints results to the terminal and copies them to the clipboard for easy sharing

## Requirements

- Python 3.10+
- macOS (for clipboard support via pbcopy)
- yt-dlp installed: `pipx install yt-dlp`
- OpenAI API key set: `export OPENAI_API_KEY="your_key_here"`

## Installation

Install Python dependencies:

`pip install -r requirements.txt`


## Usage

### Summarize a single YouTube video
```bash
python summarize_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Summarize the most recent videos from a channel
```bash
python summarize_channel.py "https://www.youtube.com/@channelname/videos"
```

## Repository structure

- `summarize_youtube.py` — summarize a single video
- `summarize_channel.py` — summarize recent channel uploads
- `requirements.txt` — Python dependencies


## Notes

- Relies on YouTube’s native captions
- Skips videos without transcripts
- Clipboard support is macOS only

## License

MIT
