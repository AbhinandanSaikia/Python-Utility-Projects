import pyttsx3
import tkinter as tk
from tkinter import ttk

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to speak the text
def speak_text():
    text = text_input.get()
    language = language_var.get()
    rate = rate_var.get()
    
    # Set the voice based on the language selection
    voices = engine.getProperty('voices')
    if language == 'English':
        engine.setProperty('voice', voices[0].id)  # Change index if multiple English voices are installed
    elif language == 'Spanish':
        engine.setProperty('voice', voices[1].id)  # Change index if a Spanish voice is installed
    # Add more language conditions as needed

    # Set the speaking rate
    engine.setProperty('rate', int(rate))

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Create the main application window
app = tk.Tk()
app.title('Multilingual Text-to-Speech')

# Input text
text_label = ttk.Label(app, text="Enter text:")
text_label.pack()
text_input = tk.Entry(app, width=50)
text_input.pack()

# Language selection
language_var = tk.StringVar(value='English')
language_label = ttk.Label(app, text="Select language:")
language_label.pack()
language_combo = ttk.Combobox(app, textvariable=language_var)
language_combo['values'] = ('English', 'Spanish')  # Add more languages if supported
language_combo.pack()

# Speech rate selection
rate_var = tk.IntVar(value=125)
rate_label = ttk.Label(app, text="Set speech rate:")
rate_label.pack()
rate_scale = tk.Scale(app, from_=50, to=300, orient='horizontal', variable=rate_var)
rate_scale.pack()

# Speak button
speak_button = ttk.Button(app, text="Speak", command=speak_text)
speak_button.pack()

# Start the GUI loop
app.mainloop()
