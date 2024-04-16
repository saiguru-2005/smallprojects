import streamlit as st
import requests

# Function to get space facts
def get_space_facts():
    response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
    data = response.json()
    return data['bodies']

# Function to get astronomy picture of the day
def get_astronomy_picture():
    api_key = "DEMO_KEY"  # Replace with your NASA API key
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
    data = response.json()
    return data['url'], data['title']

# Function to get current astronauts in space
def get_astronauts():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    return data['people']

# Streamlit UI
def main():
    st.title("Space Chatbot")

    st.sidebar.title("Features")
    option = st.sidebar.selectbox("Choose a feature", 
                                  ("Space Facts", "Astronomy Picture", "Astronauts in Space"))

    if option == "Space Facts":
        facts = get_space_facts()
        st.subheader("Space Facts")
        for fact in facts:
            st.text(f"{fact['name']}: {fact['gravity']} m/s²")

    elif option == "Astronomy Picture":
        url, title = get_astronomy_picture()
        st.subheader("Astronomy Picture of the Day")
        st.image(url, caption=title)

    elif option == "Astronauts in Space":
        astronauts = get_astronauts()
        st.subheader("Astronauts currently in space")
        for person in astronauts:
            st.text(person['name'])

if __name__ == "__main__":
    main()