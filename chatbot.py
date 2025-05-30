def get_bot_response(user_input):
    text = user_input.lower().strip()

    if any(greeting in text for greeting in ['hello', 'hi', 'hey']):
        return "Hello! How can I help you today?"
    elif 'your name' in text:
        return "I'm a simple chatbot created with Python."
    elif 'how are you' in text:
        return "I'm just code, but I'm doing well! Thanks for asking."
    elif 'time' in text or 'what time' in text or 'current time' in text:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif 'current thank' in text:
        return "You're welcome! I'm here to help."
    elif any(bye in text for bye in ['bye', 'goodbye', 'exit', 'quit']):
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"

def chat():
    print("Simple Python Chatbot (type 'exit' or 'quit' to end)")
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)
        if response.lower().startswith('goodbye'):
            break

if __name__ == "__main__":
    chat()
