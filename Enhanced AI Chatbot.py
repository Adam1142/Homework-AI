import colorama 
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

conversation_history = []

print("Hello! I am AI Bot. What's your name : ")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent" #Fallback if user doesn't provide a name
print(f"Nice to meet you, {user_name}!")

print("How are you feeling today? (good/bad) : ")
mood = input().lower()

if not mood:
    print(f"{Fore.RED}Please enter some text ot a valid command.{Style.RESET_ALL}")

if mood == "good":
    print(f"{Fore.GREEN}I'm glad to hear that!")
elif mood == "bad":
    print(f"{Fore.RED}I'm sorry to hear that. Hope things get better soon.")
else:
    print(f"{Fore.YELLOW}I see. Sometimes it's hard to put felings into words.")

if mood.lower() == "exit":
    print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent")
    print(f"It was nice chatting with you {user_name}. Goodbye!")
    quit()

if not mood:
    print(f"{Fore.RED}Please enter some text ot a valid command.{Style.RESET_ALL}")

if mood.lower() == "exit":
    print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent")

print(conversation_history)