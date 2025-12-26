import random

def random_quote_generator():
    print("----- RANDOM QUOTE GENERATOR -----\n")

    quotes = [
        "Believe in yourself and all that you are.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don’t watch the clock; do what it does. Keep going.",
        "Dream big and dare to fail.",
        "Hard work beats talent when talent doesn’t work hard.",
        "Your limitation—it’s only your imagination.",
        "Push yourself, because no one else is going to do it for you."
    ]

    while True:
        print("\n✨ Quote of the Moment:")
        print(f"\"{random.choice(quotes)}\"")

        choice = input("\nWant another quote? (yes/no): ").lower()
        if choice != "yes":
            print("Stay motivated! 💪 Goodbye!")
            break

random_quote_generator()
