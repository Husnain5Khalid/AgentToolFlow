from app.agent.agent import Agent

def main():
    agent = Agent()
    query = input("You: ")

    response = agent.run(query)

    print(response)


if __name__ == "__main__":
    main()

    