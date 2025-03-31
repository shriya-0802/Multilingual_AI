import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not found in environment variables.")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    # Save the speech in MP3 format
    tts.save("speech.mp3")

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(user_text)
    result = response.text
    return result

# Example usage:
if __name__ == "__main__":
    spoken_text = voice_input()
    if spoken_text:
        response_text = llm_model_object(spoken_text)
        print("Model response:", response_text)
        text_to_speech(response_text)
