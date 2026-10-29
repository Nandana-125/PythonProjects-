from langchain_core.messages import HumanMessage

# high level framework that allows us to build AI applications
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)  # complex framework that allows us to build ai agents
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()


@tool  # decorator
def calculator(a: float, b: float) -> str:
    """Useful for  performing basic arithmetic calculation with numbers"""
    print("tool being called")
    return f"The sum of {a} and {b} is {a + b}"


def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    tools = [calculator]

    agent_executor = create_react_agent(model, tools)

    print("Welcome ! I'm your AI assistant. Type 'quit to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()  # removing white space before and after
        if user_input == "quit":
            break
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")  # typing word by word
        print()


if __name__ == "__main__":
    main()
