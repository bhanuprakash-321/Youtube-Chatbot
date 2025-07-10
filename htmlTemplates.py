# htmlTemplates.py

css = '''
<style>
/* Global font and layout */
body {
    background-color: #9D8CFF;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #000000;
    margin: 0;
    padding: 0;
}

/* Streamlit app container */
[data-testid="stAppViewContainer"] {
    background-color: #9D8CFF;
    color: #000000;
}

/* Header - transparent */
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #8a7dde;
    color: #ffffff;
}

/* Fix input and label text color */
label, .stTextInput label, .stTextArea label, .stNumberInput label, .stSelectbox label {
    color: #000000 !important;
    font-weight: 600;
    font-size: 16px;
}

/* Title */
h1 {
    color: #000000;
    text-align: center;
    margin-bottom: 2rem;
}

/* Chat container */
.chat-message {
    padding: 1.5rem;
    border-radius: 0.75rem;
    margin-bottom: 1rem;
    display: flex;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.25);
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    transition: all 0.3s ease;
}

/* User message styling */
.chat-message.user {
    background-color: #6A5ACD; /* SlateBlue */
}

/* Bot message styling */
.chat-message.bot {
    background-color: #D5F4FF; /* Light cyan */
}

/* Avatar */
.chat-message .avatar {
    width: 15%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.chat-message .avatar img {
    max-width: 64px;
    max-height: 64px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #00000033;
}

/* Message text */
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #000000;
    font-size: 16px;
    line-height: 1.6;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/cartoon-style-robot-vectorart_78370-4103.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.shutterstock.com/image-vector/young-smiling-man-adam-avatar-600nw-2107967969.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
