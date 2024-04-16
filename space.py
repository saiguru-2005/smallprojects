import tkinter as tk
from tkinter import simpledialog, Text, Button
import requests
from transformers import pipeline
import json

# Initialize the AI model
model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

# Define functions to fetch data from APIs
def get_astronomy_picture():
    try:
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=qdrXhysVHLCU9bDge8v4XkLXtkjWAzOHSxBWjTtt")
        data = response.json()
        with open('apod.json', 'w') as f:
            json.dump(data, f)
        return data['url'], data['explanation']
    except:
        with open('apod.json', 'r') as f:
            data = json.load(f)
        return data['url'], data['explanation']

def get_astronauts_in_space():
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        with open('astronauts.json', 'w') as f:
            json.dump(data, f)
        return data['number'], [person['name'] for person in data['people']]
    except:
        with open('astronauts.json', 'r') as f:
            data = json.load(f)
        return data['number'], [person['name'] for person in data['people']]

# Tkinter UI setup
root = tk.Tk()
root.title("Space Explorer Chatbot")

# Define the function to ask a question
def ask_question():
    print("Ask question function called")  # Debugging statement
    question = simpledialog.askstring("Input", "Ask me anything about space!")
    if question:
        print("Question asked:", question)  # Debugging statement
        response = model(question, max_length=50, num_return_sequences=1)
        response_text = response[0]['generated_text']

        pic_url, pic_explanation = get_astronomy_picture()
        astronauts_num, astronauts = get_astronauts_in_space()
        
        info_text = f"Question: {question}\n\nResponse:\n{response_text}\n\nAstronomy Picture: {pic_explanation}\nAstronauts in Space: {', '.join(astronauts)}"
        
        # Display the information in a Text widget
        text_widget.delete(1.0, tk.END)  # Clear previous content
        text_widget.insert(tk.END, info_text)

# Text widget to display information
text_widget = Text(root, height=20, width=100)
text_widget.pack()

# Button to ask a question
ask_btn = Button(root, text="Ask a Space Question", command=ask_question)
ask_btn.pack()

   
root.mainloop()
