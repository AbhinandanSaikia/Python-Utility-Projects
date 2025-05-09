import os
import pygame
from tkinter import *
from tkinter import filedialog

# Initialize pygame mixer
pygame.mixer.init()

# Function to load and play a music file
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Create the main application window
root = Tk()
root.title('Music Player')
root.geometry('300x200')

# Create buttons for the player
play_button = Button(root, text="Play Music", command=play_music)
play_button.pack(pady=10)

pause_button = Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=10)

resume_button = Button(root, text="Resume", command=resume_music)
resume_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

# Run the application
root.mainloop()
