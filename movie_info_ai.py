import streamlit as st
import sys
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# Initialize the chat model
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Define the system message to set the context for the AI
template = "You are an assistant that helps users find information about movies."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# Define the human message template to get information about a specific movie
human_template = "Find information about the movie {movie_title}."
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Combine the system and human message templates to create the chat prompt
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

def get_movie_info(movie_title):
    # Format the chat prompt with the user's movie title and convert it to messages
    response = chat(chat_prompt.format_prompt(movie_title=movie_title).to_messages())
    return response.content

def run_streamlit_app():
    st.title("Movie Info AI")
    st.write("Powered by OpenAI's `gpt-3.5-turbo` model, our Movie Info AI provides insights into movies, including plot summaries and cast details. Dive into cinematic archives with just a movie title and experience the capabilities of advanced language models firsthand!")
    
    # Using markdown for italic text
    st.markdown("*Disclaimer: Movie information is limited up to September 2021.*")
    
    # Using the label parameter for the input box
    movie_title = st.text_input(label="Movie Title", value="", label_visibility="hidden")
    
    if st.button("Find"):
        with st.spinner('Finding movie information...'):
            result = get_movie_info(movie_title)
        st.write(result)

def run_terminal_app():
    movie_title = input("Enter the title of the movie you want information about: ")
    result = get_movie_info(movie_title)
    print(result)

if __name__ == "__main__":
    # Check if the script is being run through Streamlit or not
    if 'streamlit' in sys.modules:
        run_streamlit_app()
    else:
        run_terminal_app()
