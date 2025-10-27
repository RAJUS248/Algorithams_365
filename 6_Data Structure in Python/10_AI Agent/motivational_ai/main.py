from wrapper import AgentWrapper

def main():
    print("🌟 Welcome to the Motivational AI Agent!")
    api_key = "put your OPENAI_API_KEY here "
    wrapper = AgentWrapper(api_key)

    name = input("Enter your name: ")
    motivation_type = input("What kind of motivation do you need (e.g., career, fitness, emotional)? ")

    print("\n🧠 Sending your request to ChatGPT...\n")
    message = wrapper.get_motivation(name, motivation_type)
    print(f"💬 ChatGPT says:\n{message}")

if __name__ == "__main__":
    main()
