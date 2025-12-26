import sys
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

if len(sys.argv) != 2:
    print("Usage: python summarize_youtube.py <youtube_url>")
    sys.exit(1)

url = sys.argv[1]

parsed = urlparse(url)
video_id = parse_qs(parsed.query).get("v", [None])[0]

if not video_id:
    print("Could not extract video ID")
    sys.exit(1)

print(f"Fetching transcript for {video_id}...")

transcript = YouTubeTranscriptApi().fetch(video_id)
text = " ".join(segment.text for segment in transcript)

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "Produce exactly 5 concise bullet points that capture the core ideas of the transcript."
        },
        {
            "role": "user",
            "content": text
        },
    ],
)

summary = response.choices[0].message.content.strip()

print("\nSummary:\n")
print(summary)

with open(f"{video_id}.summary.txt", "w") as f:
    f.write(summary)

print(f"\nSaved summary to {video_id}.summary.txt")
