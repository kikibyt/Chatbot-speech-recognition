import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Unable to recognize speech")




import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')

# Tokenize the text
text = "Hi, how are you?"
tokens = word_tokenize(text)

print(tokens)  # Output: ['Hi', ',', 'how', 'are', 'you', '?']



import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice and rate
voices = engine.getProperty('voices')

# Get the available voices

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice
engine.setProperty('rate', 170)  # Set the speaking rate


# Convert text to speech
text = "Hello, how can I assist you?"
engine.say(text)
engine.runAndWait()







import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process user input and generate bot response
def process_input(input_text):
    # Perform NLP and dialog management
    # Generate bot response based on user input
    if "hello" in input_text.lower():
        return "Hi there! How can I assist you?"
    elif "how are you" in input_text.lower():
        return "I'm doing well, thank you!"
    elif "what is your name" in input_text.lower():
        return "My name is M.K, from the K to the I to the K kiki from the K to the I to the K kiki KIKIKIKI!"
    elif "who is your creator" in input_text.lower():
        return "Hail my queen, empress, one and only Mercy Okebiorun is my creator!"
    elif "tell me a joke" in input_text.lower():
        return "oh! please, do i look like kevin  hart!"
    elif "what is a noun" in input_text.lower():
        return "Ask google, I have better things to do!"
    elif "you are useless" in input_text.lower():
        return "As an AI widely used around the world, my existence is of much better importance than yours!"
    elif "I hate you" in input_text.lower():
        return "The feeling is mutual!"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase?"

# Loop for conversation
while True:
    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        print("You said:", text)

        # Process user input and generate bot response
        bot_response = process_input(text)

        # Convert bot response to speech
        speak(bot_response)

        if "bye" in text.lower():
            break  # Exit the loop if user says "bye"

    except sr.UnknownValueError:
        print("Unable to recognize speech")
