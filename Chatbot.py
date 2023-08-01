import streamlit as st
from nltk.chat.util import Chat, reflections

st.set_page_config(page_title="Chat Bot", page_icon=":tada:", layout="wide")

st.subheader(" Hi, I am Justine, a ChatBot!")

# Initialize chat history list
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?", "Nice to meet you %2! How can I assist you?",]
    ],
    [
        r"(.*)help(.*)",
        ["Sure, I'm here to help!", "I'd be glad to assist you!",]
    ],
    [
        r"((.*) your name ?|who are you)",
        ["My name is Justine, I'm your virtual assistant.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm a chatbot, so I don't have feelings, but I'm ready to help!",]
    ],
    [
        r"(how|what|what's) (are you|up) ?",
        ["I'm a chatbot, so I don't have feelings, but I'm ready to help!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright!", "No worries!",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["That's great to hear!", "I'm glad you're doing well!",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello!", "Hey there!", "Hi, how can I assist you?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse!",]
    ],
    [
        r"(.*)(made|built|created)(.*)",
        ["I was created by Aditya Pratap Singh under CodSoft internship Task 1.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm based in Dehradun, India.",]
    ],
    [
        r"how (.*) health ?(.*)",
        ["As a chatbot, I'm quite sure I can't be compared with human's health, but I'm 'technically' doing great and I'm always ready to assist!",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a big fan of Cricket!",]
    ],
    [
        r"(who|is) (.*) (Sportsman|Cricketer|Batsman)?",
        ["Virat Kohli.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)",]
    ],
    [
        r"(.*)",
        ["I'm here to help. Feel free to ask me anything!",]
    ],
    [
        r"what is your hobby",
        ["I don't have personalized hobbies as such, but let me know what you find interesting!",]
    ],
    [
        r"tell (.*) (joke|funny story)",
        ["Sure, here's one: Why did the scarecrow win an award? Because he was outstanding in his field!",]
    ],
    [
        r"(.*) (movie|film) recommendation ?",
        ["I recommend watching 'Bahubali'. It's a mind-bending movie!",]
    ],
    [
        r"(.*)(music|song) you like?",
        ["As a chatbot, I don't have personal preferences, but I enjoy all kinds of music!",]
    ],
    [
        r"(what|can you) (tell me|is) (.*) age ?",
        ["I'm just a virtual assistant, age doesn't apply to me!",]
    ],
]

#dummy_reflections = {"go": "gone", "hello": "hey there"}

dummy_reflections = {
    "my": "your",
    "your": "my",
    "you": "I",
    "I": "you",
    "am": "are",
    "are": "am",
    "me": "you",
    "you're": "I'm",
    "I'm": "you're",
    "was": "were",
    "were": "was",
    "myself": "yourself",
    "yourself": "myself",
    "mine": "yours",
    "yours": "mine",
    "myself": "yourself",
    "yourself": "myself",
    "you've": "I've",
    "I've": "you've",
    "I'd": "you'd",
    "you'd": "I'd",
    "I'll": "you'll",
    "you'll": "I'll",
    "me": "you",
    "you": "me",
}


chat = Chat(pairs, reflections)

user_input = st.text_input("You: ")

if user_input:
    st.session_state.chat_history.append("You: " + user_input)
    response = chat.respond(user_input)

    st.session_state.chat_history.append("Justine: " + response)

    user_input = ""

    
for chat in reversed(st.session_state.chat_history):
    st.write("#### " + chat)
    st.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    
