import requests

def summarize(text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"Summarize the following text:\n\n{text}",
            "stream": False,
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    text = "I built a Python tool to summarize audio transcripts."
    summary = summarize(text)
    print(summary)

