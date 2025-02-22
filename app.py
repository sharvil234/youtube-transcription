from faster_whisper import WhisperModel
import yt_dlp
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


def video_to_audio(video_url):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": "audio.%(ext)s",
            "quiet": True,
            "source_address": "0.0.0.0",  # Force IPv4
            "force-ipv4": True,  # Force IPv4
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return "audio.mp3"
    except Exception as e:
        print(f"Error downloading video: {str(e)}")


def summarize_transcript(transcript):
    try:
        # Initialize ChatGroq LLM
        llm = ChatGroq(
            api_key=os.environ["GROQ_API_KEY"],
            model_name="llama-3.2-1b-preview",
            temperature=0,
        )

        # Create a prompt template
        prompt_template = """
        Please summarize the following text:
        {text}
        Summary:
        """

        prompt = ChatPromptTemplate.from_template(template=prompt_template)

        # Generate summary
        chain = prompt | llm
        summary = chain.invoke({"text": transcript})
        return summary.content

    except Exception as e:
        print(f"Error summarizing transcript: {str(e)}")


def transcribe_video(video_url):
    try:
        audio_path = video_to_audio(video_url)
        model = WhisperModel("small")
        segments, info = model.transcribe(audio_path)
        transcript = "".join([segment.text for segment in segments])
        print("Transcript: %s" % transcript)

        # Clean up the audio file after transcription
        if os.path.exists(audio_path):
            os.remove(audio_path)
        return transcript

    except Exception as e:
        print(f"Error transcribing video: {str(e)}")

