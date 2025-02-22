# YouTube Video Transcription

A Python-based tool for transcribing YouTube videos and generating summaries using Faster Whisper and Groq LLM.

## Features

- Download audio from YouTube videos
- Transcribe audio using Faster Whisper
- Generate summaries using Groq LLM
- Support for various audio formats
- Clean and efficient processing

## Prerequisites

- Python 3.10 or higher
- GROQ API key

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```
3. Install dependencies:
```bash
pip install -e .
```

## Configuration

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

```python
from app import transcribe_video, summarize_transcript

# Transcribe a video
transcript = transcribe_video("https://www.youtube.com/watch?v=your_video_id")

# Generate summary
summary = summarize_transcript(transcript)
```

## Dependencies

- faster-whisper
- langchain
- langchain-groq
- python-dotenv
- yt-dlp

## License

MIT License