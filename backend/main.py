from graph import run_chat_graph


def main():
    print("Provide the following inputs regarding your car.")
    user_input_text = input("Please enter your car details: ")
    user_input_image = input("Upload the car's image")

    if not user_input_text:
        print("please enter a message")

    print("user wrote: " + user_input_text)

    try:
        response = run_chat_graph(user_input_text,user_input_image)
        print(f"Bot: {response}\n")
    except Exception as e:
        print(f"❌ Error: {e}")

        
if __name__ == "__main__": #ensures that main() only runs when this file is executed as the main script not imported.
    main()