import re, random
from colorama import Fore, init

#Initialize colorama (autoreset ensures each print resets after use)
init(autoreset = True)

#Destination & joke data
destinations = {
    "beasches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountain", "Himolayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why dont programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!,",
    "Why do travellers always feel warm? Because of all their hot spots!"
]

#Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"s+", " ", text.strip().lower())

#Provide travel recomendations (recursive if user rejects suggestion)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    prefrence = input(Fore.YELLOW + "You: ")
    prefrence = normalize_input(prefrence)

    if prefrence in destinations:
        suggestion = random.choice(destinations[prefrence])
        print(Fore.GREEN + f"TravelBot: How About {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
            recommend()
        
        show_help()

# Offer packing tips based on user's destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(input(Fore.YELLOW + "You: ")))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Where to?")
    print(Fore.GREEN + "- pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forcast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN +"- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or bye' to end.\n")
    
# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()