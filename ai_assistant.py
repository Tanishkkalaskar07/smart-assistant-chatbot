import ollama

# List to store conversation history
chat_history = []

print("Type 'exit' to quit the assistant.\n")

while True:
    # Get user input
    user_input = input("You: ").strip()
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Handle empty input
    if not user_input:
        print("Please enter something!")
        continue
    
    # Add user message to history
    chat_history.append({"role": "user", "content": user_input})
    
    # Get response from Ollama
    response = ollama.chat(
        model="llama3",
        messages=chat_history
    )
    
    assistant_message = response["message"]["content"]
    print("Assistant:", assistant_message)
    
    # Add assistant response to history
    chat_history.append({"role": "assistant", "content": assistant_message})
    
    # Optional: save to chat log
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"Assistant: {assistant_message}\n\n")