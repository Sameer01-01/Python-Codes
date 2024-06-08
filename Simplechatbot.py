def chatbot_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you": "I'm good, thank you!",
        "bye": "Goodbye!"
    }

    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def chatbot():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chatbot()
