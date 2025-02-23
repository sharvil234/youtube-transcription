# YouTube Video Transcription

A Python-based tool for transcribing YouTube videos and generating summaries using Faster Whisper and Groq LLM.

## Features

- Download audio from YouTube videos using yt-dlp with IPv4 support
- Local transcription using Faster Whisper when GPU is available
- Cloud transcription using Groq's Whisper service as fallback
- AI-powered summarization using Groq LLM
- Automatic cleanup of temporary files
- Support for various audio formats through FFmpeg

## Prerequisites

- Python 3.10 or higher
- FFmpeg (for audio processing)
- CUDA-compatible GPU (optional, for local transcription)
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd youtube-transcription
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -e .
```
4. Install FFmpeg (Windows):
```bash
scoop install ffmpeg
```

## Configuration

Create a `.env` file in the root directory:
```properties
GROQ_API_KEY=your_api_key_here
```

## Usage

```python
from app import transcribe_video, summarize_transcript

# Transcribe a video
video_url = "https://www.youtube.com/watch?v=your_video_id"
transcript = transcribe_video(video_url)

# Generate summary
summary = summarize_transcript(transcript)
print(summary)
```

## Dependencies

- faster-whisper>=0.10.0
- yt-dlp>=2023.12.30
- langchain>=0.1.0
- langchain-groq>=0.1.0
- python-dotenv>=1.0.0
- torch>=2.2.0
- groq>=0.4.0

## Error Handling

The tool includes robust error handling for:
- YouTube download issues
- Audio processing errors
- Transcription failures
- API communication problems

## License

MIT License - See LICENSE file for details