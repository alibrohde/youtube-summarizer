import sys
import subprocess
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

if len(sys.argv) < 2:
    print("Usage: python summarize_channel.py <channel_url> [N]")
    sys.exit(1)

channel_url = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 2

print(f"Fetching last {N} videos from channel...")

# Get video IDs (most recent first)
result = subprocess.run(
    [
        "yt-dlp",
        "--flat-playlist",
        "--print",
        "id",
        channel_url
    ],
    capture_output=True,
    text=True
)

video_ids = result.stdout.strip().splitlines()[:N]

client = OpenAI()
all_output = []

for video_id in video_ids:
    print(f"\nProcessing video {video_id}")

    # Fetch title and upload date
    meta = subprocess.run(
        [
            "yt-dlp",
            "--print",
            "%(title)s\n%(upload_date)s",
            f"https://www.youtube.com/watch?v={video_id}"
        ],
        capture_output=True,
        text=True
    ).stdout.strip().splitlines()

    title = meta[0]
    raw_date = meta[1] if len(meta) > 1 else ""
    formatted_date = (
        f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
        if raw_date else "Unknown date"
    )

    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
    except Exception:
        print(f"Skipping {video_id}: no transcript available")
        continue

    text = " ".join(segment.text for segment in transcript)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Summarize the transcript into exactly 3 bullet points. "
                    "Each bullet should capture a core idea. "
                    "Do not produce more or fewer than 3 bullets."
                )
            },
            {
                "role": "user",
                "content": text
            },
        ],
    )

    summary = response.choices[0].message.content.strip()

    block = (
        f"{title}\n"
        f"{formatted_date}\n\n"
        f"{summary}\n\n"
    )

    print(block)
    all_output.append(block)

final_text = "".join(all_output)

# Copy full output to clipboard (macOS)
subprocess.run(
    ["pbcopy"],
    input=final_text,
    text=True
)

print("All summaries copied to clipboard.")
