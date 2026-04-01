import random

responses = [
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

def magic_8_ball():
    name = input("Enter your name: ").strip()
    question = input("Ask your question: ").strip()

    if not question:
        print("Please ask your query.")
        return

    answer = random.choice(responses)

    if name:
        print(f"{name} asks: {question}")
    else:
        print(f"Question: {question}")

    print(f"Magic 8-Ball's answer: {answer}")

if __name__ == "__main__":
    while True:
        magic_8_ball()
        again = input("\nDo you want to ask another question? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the Magic 8-Ball!")
            break
