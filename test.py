import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set properties for the engine
for voice in voices:
    if 'female' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)  # Adjust the speaking rate (default is 200)

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Test the text-to-speech functionality
if __name__ == "__main__":
    speak("Hello, this is a test of the text-to-speech functionality using a female voice.")
