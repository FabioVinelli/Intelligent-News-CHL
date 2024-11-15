from google.cloud import texttospeech
import os

class TTSAgent:
    """
    Agent for text-to-speech conversion.
    """

    def __init__(self):
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError("Please set the GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        self.client = texttospeech.TextToSpeechClient()

    def text_to_speech(self, text: str, output_filename: str):
        """
        Convert text to speech and save as an audio file.

        Args:
            text (str): The text to convert.
            output_filename (str): The filename for the output audio file.
        """
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Wavenet-D")
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = self.client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        with open(output_filename, "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to "{output_filename}"')

# Example Usage
if __name__ == "__main__":
    tts = TTSAgent()
    tts.text_to_speech("This is a test summary.", "summary.mp3")
