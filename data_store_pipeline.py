import os
from openai import OpenAI
from langchain_openai import ChatOpenAI

# Set up your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model='gpt-4o',temperature=0.1)
client = OpenAI()

class VideoTranscriber:
    def Trasnsriber(self,file_path):
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        return transcription
        

