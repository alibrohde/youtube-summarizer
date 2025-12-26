# YouTube Transcript Summarizer

A simple Python CLI for extracting YouTube transcripts and generating concise AI summaries.

This tool is designed for fast research, note-taking, and content triage. It pulls YouTube’s native captions when available, summarizes videos into short bullet points, and copies the output directly to your clipboard.

## What this does

- Extracts YouTube’s native transcripts (no scraping, no YouTube API keys)
- Summarizes videos into **exactly 3 concise bullet points**
- Works for a single video or the most recent videos from a channel
- Prints results to the terminal and copies them to the clipboard for easy sharing

## Requirements

- Python 3.10+
- macOS (for clipboard support via `pbcopy`)
- `yt-dlp` installed  
pipx install yt-dlp
- An OpenAI API key set in your environment  
export OPENAI_API_KEY="your_key_here"

## Installation

Clone the repo and install Python dependencies:

pip install -r requirements.txt


## Usage

### Summarize a single YouTube video



python summarize_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID
"


What happens:
- The script fetches the video’s native transcript
- Generates **exactly 3 bullet points**
- Prints the summary
- Copies the summary to your clipboard

### Summarize the most recent videos from a channel



python summarize_channel.py "https://www.youtube.com/@channelname/videos
"


By default, this summarizes the **latest 2 videos**.

You can optionally specify how many videos to summarize:



python summarize_channel.py "https://www.youtube.com/@channelname/videos
" 5


What happens:
- Fetches the most recent videos from the channel
- Pulls title and upload date for each video
- Generates **exactly 3 bullet points per video**
- Prints all summaries
- Copies the combined output to your clipboard

Videos without available transcripts are skipped automatically.

## Repository structure

This repo intentionally contains only a few small, focused scripts:

- `summarize_youtube.py`  
  Summarizes a single YouTube video.  
  Input: video URL  
  Output: 3-bullet summary printed to terminal and copied to clipboard.

- `summarize_channel.py`  
  Summarizes recent videos from a channel.  
  Input: channel `/videos` URL and optional count  
  Output: per-video summaries (title, date, 3 bullets), printed and copied to clipboard.

- `requirements.txt`  
  Python dependencies required to run the scripts.

The scripts are designed to be simple, composable, and easy to extend.

## Notes and limitations

- This tool relies on YouTube’s native captions. If captions are disabled, the video will be skipped.
- Audio transcription fallback is intentionally not included to keep the tool simple.
- Clipboard copying currently supports macOS only.

## License

MIT