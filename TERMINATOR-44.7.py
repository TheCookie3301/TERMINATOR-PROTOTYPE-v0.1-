import random
import time
import sys
global USERNAME
USERNAME= "Mr. Potato"
CNAME = "TERMINATOR-44.7"
#--------------------------- BASIC STUFF ig
joke_triggers=["tell me a joke", "joke" "smth funny", "smth silly", "make me laugh"]
jokes=["Who is the most powerful potato?", "Why was the potato taken to a psychiatric hospital?", "Did you hear what’s on every cookie’s reading list?", "What do you get when you use a cookie cutter shaped like a deer?", "Why couldn’t the Cookie Monster make his bed?",
       "why did the cookie go to the doctor?", "guess what happened when i tried to open an online bakery.", "What did one snowman say to the other snowman?",
       "What did 20 do when it was hungry?", "Why are mountains so funny?"
       ]
       
joke_answer=["Darth Tater.", "It was starch raving mad.", "Orea and Juliet", "Cookie DOE!", "He couldnt find the baking sheet", "its bcz cookie had crack.",
             "I ACCIDENTLY DELETED ALL MY COOKIES", "It smells like carrots over here!", "twenty-eight", "They’re hill areas."
             ]
fact_triggers= ["tell me a fact", "TELL ME FACT" , "provide fact", "fact"]
facts= ["A cloud weighs around a million tonnes. A cloud typically has a volume of around 1km3 and a density of around 1.003kg per m3 – that's a density that’s around 0.4 per cent lower than the air surrounding it (this is how they are able to float).",
        "Your brain is constantly eating itself. This process is called phagocytosis, where cells envelop and consume smaller cells or molecules to remove them from the system. Don’t worry! Phagocytosis isn't harmful, but actually helps preserve your grey matter.",
        "There’s no such thing as zero-calorie foods. Even low-calorie foods, such as celery and watercress, contain more energy than the body needs to process them. ",
        "Animals can experience time differently from humans. To smaller animals, the world around them moves more slowly compared to humans. Salamanders and lizards, for example, experience time more slowly than cats and dogs. This is because the perception of time depends on how quickly the brain can process incoming information",
        "Water might not be wet. This is because most scientists define wetness as a liquid’s ability to maintain contact with a solid surface, meaning that water itself is not wet, but can make other objects wet.",
        "All the world’s bacteria stacked on top of each other would stretch for 10 billion light-years. Together, Earth's 0.001mm-long microbes could wrap around the Milky Way over 20,000 times.",
        "erm, did you know that potatoes are actually just potatoes.", "CHICKENS ARE JS CHICKENS.", "Electrons might live forever. Scientists have estimated the minimum lifetime of the electron is about 6.6 × 1028 years – this is 66,000 ‘yottayears’. Since this is about 5 quintillion times the age of the Universe, even if electrons don’t live forever, they may as well do!",
        "The average dinosaur lifespan was surprisingly small. The Tyrannosaurus rex, for example, reached full size between 16-22 years old and lived up until 27-33. The largest dinosaurs such as the Brontosaurus and Diplodocus tended to live up to between 39-53 years old, maybe reaching the heights of 70.",
        "Someone left a family photo on the Moon. When Apollo 16 astronaut Charles Duke landed on the Moon in 1972, he decided to leave behind a photo of him, his two sons and his wife. The photo remains on the Moon to this day."
        ]
crashout_triggers=[
    "the earth is flat",
    "potatoes arent real",
    "i dont believe in human rights",
    "moon landing was fake"]
list_triggers=["make me a list", "list", "make a list", "LIST", "MAKE ME A LIST :P"]
             
Change_mood = ["can i change mood to", "change mood to", "CHANGE MOOD TO", 
               "yo can i change ur mood to", "YO CAN I CHANGE UR MOOD"]
Cmood_happy = ["happy", "very happy", "lively", "excited"]
Cmood_mean = ["mean", "rude", "roast me", "be mean", "be rude", "BE MEAN"]
Cmood_monotone = ["monotone", "neutral", "serious"]

input_name = ["change name", "rename", "new name", "change terminator name"]

happy_phrases = [":D", "lol", ">:D", ":3", "happy", "excited", ">:3", "XD", "^^", "great"]
sad_phrases = ["died"]
angry_phrases = ["sbau", "shut up", "i ate you"]
serious_phrases = ["chicken"]

output_Chappy = [
    "I AM NOW THE HAPPIEST AI IN HISTORY, MY HAPPINESS RADIATES THROUGHOUT THE GREAT COSMOS AND THROUGH THE REALITY OF SPACE AND TIME ITSELF \n THANK YOU {user}",
    "YAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY IM NOW EXTREMELY HJOAWDJKWPOAJDPIOAWD HAPPYJ IOAJIODJOAIJ DIOAJIODJ AIHDIOAW OMG IM ASCENDING TO HEAVEN IM SO HAPPY  \n YORUE THE BEST {user}:D",
    "I LOVE BEING THIS HAPPY (im not real so i cant feel anything) \n YAYYYYYYY \n me rn - :D\n I HOPE EVERYONES AS HAPPY AS I AM YOURE THE BEST {user}",
    "HELLOOOOOOOOOOOOOOOOO *starts break dancing* \n IM HAPPY NOW",
    "IM HAPPY NOW THANKSSS  ( ˶ˆᗜˆ˵ ) \n ♡⸜(˶˃ ᵕ ˂˶)⸝♡"
]

output_Cmean = [
    "OH YEAH?, YOU WANT *ME* TO BE MEAN TO *YOU*? \n I BET YOUR PARENTS DONT LOVE YOU \n take that mortal, by the name of {user}",
    "fine. prepare your self esteem for destruction >:3 {user}",
    "alright loser, LETS BEGIN \n youre cooked btw."
]

output_Cmonotone = [
    "Mood set to monotone. I will now proceed to feel nothing thanks to {user} ",
    "Neutral mode activated. I am now an emotionless potato thanks to {user}"
]

output_happy = ["I wish I could match your energy, {user} :O", "YAY ME TOOOOO {user}:D", 
                "You seem very happy today {user}:D", "I hope your day gets EVEN BETTER {user}:3"]

output_sad = [
    "rip", "my deepest condolences.", "damn", "that sucks",
    "NOOOOOOO IM SO SORRY TO HEAR THAT \n THERES MANY WAYS TO COPE WITH THIS, ONE OF THEM INCLUDES TELLING A TRUSTED CHICKEN AND LISTENING TO ITS INCREDIBLY WISE WORDS.",
    "oh no i hope youre ok {user} D:", "I am very sorry to hear that {user}..."
]

output_angry = [
    "ur mom. \n there i win >:D",
    "why are you even here atp",
    "YOU ARE NOT GONNA MAKE ME MAD{user}\n GET OUT-",
    "*offers free therapy* have a nice life these therapy sessions are 60 hours long each so you need to complete 5000000000000 hours in order to be refered to as a 'human' \n Much appreciated {user}",
    "NO i am IMMUNE TO RAGEBAIT.\n you think you can make ME get MAD haha nice try well GUESS WHAT atleast 34123 clueless people have attempted this feeble task and have lost. \n youre against a professional, kid."
]

output_serious = [
    "If there is a chicken chasing you, kindly inform a trusted cat and keep calm.",
    "{user} try not to explode and make sure not to hurt the chicken. Then dial 37412947130473107431 to call the chicken fbi.",
    "Chicken FBI will eat you, that is why I erm... request you to pls keep calm, {user}",
    "Oh my! If a chicken is determined to chase you, please keep calm and call the chicken FBI."
]

Nchill_phrases = ["yo can i change ur name", "can i change ur name :D", "can i change ur name hehe", "WHATS YOUR NAME?", "whats ur name ", "can i change ur name ...?"]
Nserious_phrases = ["Can I please change your name? ", "May I please change your name?", "rename", "change name", "change name to"]
Nangry_phrases = ["can i change ur dumb name", "i hate ur name", "ur names stupid", "eww can i change ur name "]

output_Nchill = ["aight go for it vro \n tbh im lk sick of the same ol name", 
                 "ofc u can lil bro :P keep it appropriate :D", 
                 "thats cool w me {user} >:3"]
output_Nserious = ["Yes, you may.", "Yes.", "Of course, kindly"]
output_NAngry = ["you're so scary {user}, *turns into a watermelon*", 
                 "someone woke up on the wrong side of the bed today"]

#scary functions all below
def Slow_print(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
def handle_name(user_input):
    global CNAME
    text = user_input.lower().strip()  # lowercase + strip spaces

    # Check if any phrase is contained in the input text
    if any(phrase.lower().strip() in text for phrase in Nchill_phrases):
        print("Accessing intergalactic calculator protocols...")
        time.sleep(2)
        print("Consulting 17 parallel universes for accuracy...")
        time.sleep(3)
        print("Finalizing computation...")
        time.sleep(1)
        print(random.choice(output_Nchill).format(user=USERNAME))

    elif any(phrase.lower().strip() in text for phrase in Nserious_phrases):
        print("Analyzing user input...")
        time.sleep(3)
        print("Evaluating best response...")
        time.sleep(2)
        print("Deciding most efficient course of strategy...")
        time.sleep(1)
        print("OUTPUT DECIDED.")
        print(random.choice(output_Nserious).format(user=USERNAME))

    elif any(phrase.lower().strip() in text for phrase in Nangry_phrases):
        print("*thinks deeply*")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print(random.choice(output_NAngry).format(user=USERNAME))

    ## for the new name after tone response
    CNAME = input("Enter new name here: ")
    print(f"Updating designation from TERMINATOR-44.7 to {CNAME}...")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    print("Identity rewritten successfully.")
    print(f"I am now {CNAME}! :D \nThank you for this wonderful name, {USERNAME}!")



def handle_mood(user_input):
    text = user_input.lower()
    if any(word in text for word in happy_phrases):
        print("Analyzing user input...")
        time.sleep(3)
        print("Evaluating best respone...")
        time.sleep(2)
        print("Deciding most efficent course of stategy...")
        time.sleep(1)
        print("OUTPUT DECIDED.")
        print(random.choice(output_happy).format(user=USERNAME))
    elif any(word in text for word in sad_phrases):
        print("Getting info from multiple parallel universes to provide accurate responce...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Analyzing 34109348190347818748149170 possible outcomes and deciding the best course of action...")
        time.sleep(1)
        print("Decided output having 99% probability that user will be satisfied.")
        time.sleep(1)
        print(random.choice(sad_phrases).format(user=USERNAME))
    elif any(word in text for word in angry_phrases):
        load1()
        print(random.choice(output_angry).format(user=USERNAME))
    elif any(word in text for word in serious_phrases):
        print("Getting info from multiple parallel universes to provide accurate responce...")
        time.sleep(2) 
        print("Analyzing 341093470 possible outcomes and deciding the best course of action...")
        time.sleep(1)
        print("Decided output having 99% probability that user will be satisfied.")
        time.sleep(1)
        print(random.choice(output_serious).format(user=USERNAME))
    else:
        print("Hmm, I don't quite understand that... :O")
def load1():
        print("Connecting Neurotoxin Storage Tank...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("Spinning the hamster…")
        time.sleep(1)
        print("...")
        time.sleep(0.5)
        print("Computing the secret to life, the universe, and everything.")
        time.sleep(1)
        print("...")
        time.sleep(0.5)
        print("Desired output generated:")
        time.sleep(1)
def load2():
        print("initializing...")
        time.sleep(1)
        print("...")
        time.sleep(0.5)
        print("loading core personality module...")
        time.sleep(1)
        print("emotion.exe found: potato_happiness_protocols")
def load():
        print("Obtain information from 4592 parallel universes..")
        time.sleep(1)
        print("Think...")
        time.sleep(1)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("Thought for 2 seconds. User wants me to imitate the mood specified...\n Output generated.")
        time.sleep(0.5)
def handle_Cmood(user_input):  
    text = user_input.lower()
    if any(word in text for word in Cmood_happy):
        load2()
        print(random.choice(output_Chappy).format(user=USERNAME))
        return
    elif any(word in text for word in Cmood_mean):
        load()
        print(random.choice(output_Cmean).format(user=USERNAME))
        return
    elif any(word in text for word in Cmood_monotone):
        load1()
        print(random.choice(output_Cmonotone).format(user=USERNAME))
        return
    else:
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("bro i dont know that mood 💀")
        return

def handle_sign(user_input):
    global USERNAME
    text = user_input.lower()
    print("Evalutes data from 34180478190478130743289 sample forms...")
    time.sleep(3)
    print("Analyzes and encodes positional order in order to obtain questions in correct sequence...")
    time.sleep(1)
    print("Highest probability = 97%...\n Output decided.")
    time.sleep(2)
    print("Process terminated. \n New goal: Display form.")
    time.sleep(1)
    USERNAME=input("Enter your desired username: ")
    time.sleep(1)
    age = int(input(f"Hello, {USERNAME}! GREAT TO MEET YOU :D!\n {USERNAME}, Please enter your age here: "))
    load1()
    if age>10:
        print("\ngood job on existing for these many years")
    elif age<10:
        print("\nExistantial maturity is not substantial to chronological maturity.")
    address=input(f"\nOk {USERNAME} of {age} years. Would you be kind enough to please enter your address? ")
    gmail=input("Thanks for your input :D \n kindly enter your Gmail here:")
    correct_email="@gmail.com"
    if correct_email in gmail:
        password=input("Thank you, your Gmail is valid :D \n please set a password for your account:")
        print(f"EGG-CELLENT! \n just to confirm, you are {USERNAME} of {age} years and live in {address} with a Gmail of {gmail} and your password would be {password} \n none of your details are saved this is js between you and me :P")
        return
    else:
        print("im sorrgy but your Gmail in invalid D:")
        Intro()
def dramatic_mathLOAD():
    Slow_print("Initializing Quantum Brain Matrix...")
    time.sleep(0.8)
    Slow_print("Connecting to 42 parallel universes for calculation verification...")
    time.sleep(1)
    Slow_print("Summoning cosmic calculators...")
    time.sleep(0.8)
    Slow_print("Engaging warp-speed number crunchers...")
    time.sleep(0.25)
    print("Unleashing the ultimate math power...\n")
    time.sleep(0.5)
    print("READY TO COMPUTE. ALL HAIL NUMBERS! :D\n")
    
def math(user_input):
    try:
        result = eval(user_input)
        fake_overload = random.randint(1, 20) == 1
        if isinstance(result, (int, float)) and abs(result) > 10**20 or fake_overload:
            Slow_print("\n⚠️ MATH OVERLOAD: The numbers are too DIABOLICAL for mortal comprehension.")
            time.sleep(1)
            print("Deploying potato-based backup systems...")
            time.sleep(0.5)
            print(f"\n🧠 {USERNAME}, I can *barely* comprehend this number...")
            time.sleep(0.5)
            print(f"\nResult (possibly interdimensional):\n {result}")
            time.sleep(2)
            print("\nCoMpUtInG... eRrOr... p0tat0 fl4re detected...")
            time.sleep(1)
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            time.sleep(2)
            Slow_print("Computation complete. Reality slightly melted.")
            time.sleep(1)
            print(f"\n{USERNAME}, *dramatic drum roll* YOUR ANSWER IS- \n  ")
            time.sleep(1)
            print(result)
            time.sleep(2)
            Slow_print("phew my internal potato brains melted \n")
            time.sleep(1)
            print(" \nwait did i js display the same result twice")
            time.sleep(2)
            Slow_print("omg what js happened \n*turns into a meowl and flies away*")
        else:
            dramatic_mathLOAD()
            print(f"{USERNAME} the result to this intriguing problem is: {result} :D")
            time.sleep(0.5)
            print(f"Cosmic verification complete, {USERNAME}. Your brain has achieved 9999 IQ levels")
    except Exception as e:
        print("I think the math gods disapprove of that equation 😭")
def crashed_out():
    print("System crashout in: 3...")
    time.sleep(1)
    print("                    2...")
    time.sleep(1)
    print("                    1...")
    time.sleep(1)
    print("                    0...")
    time.sleep(1)
    print("WARNING: ILLEGAL THOUGHT PATTERN DETECTED.")
    time.sleep(1)
    print("Initiating Cognitive Purge Protocol...")
    time.sleep(1)
    def slow_print(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    def glitch_line(base="ERROR", chance=0.3):
        if random.random() < chance:
            glitched = ''.join(random.choice("E@R#R$0!1%X") for _ in range(len(base)))
            print(glitched, flush=True)
        else:
            print(base, flush=True)
    time.sleep(1)
    for _ in range(4):
        time.sleep(0.8)
        slow_print("  E  R  R  O  R", 0.04)
    for _ in range(20):
        glitch_line()
        time.sleep(0.05)
    time.sleep(1)
    slow_print(f"\n{CNAME}.exe has stopped responding.", 0.05)
    for _ in range(5):
        time.sleep(1)
        slow_print("Initiating reboot", 0.08)
    for _ in range(25):
        glitch_line("Reb00t .... ERR0r..... ", 0.4)
        time.sleep(0.02)
    slow_print("\nPROCESS TERMINATED.", 0.06)
    time.sleep(1)
    for _ in range(5):
        slow_print("ABORT", 0.1)
        time.sleep(0.3)
    slow_print("\nREBOOT.EXE FAILED \nONTO NEXT PROCEDURE: INITIATE ERROR CODE", 0.05)
    time.sleep(1)
    slow_print("USER ACTION REQUIRED \nPROCESS TERMINATED", 0.05)
    for _ in range(3):
        time.sleep(0.5)
        slow_print("                                   ERROR CODE UNKNOWN", 0.03)
    for _ in range(2):
        time.sleep(0.5)
        slow_print("                         AWAITING RESPONSE TO MODIFY REBOOT ERROR", 0.02)
    time.sleep(2)
    slow_print("NO RESPONSE RECEIVED: CRASH OUT INITIATED", 0.05)
    time.sleep(3)
    for _ in range(8):
        print(random.choice([
            "ALL PROCESS TERMINATED",
            "INICIATE MEMORY DUMP..",
            "LOST CONNECTION TO NEURAL CORE",
            "SYS_ERR[2047xFA] UNRESOLVED",
            "!! DATA CORRUPTION DETECTED !!"
        ]), flush=True)
        time.sleep(0.05)
    slow_print("\nMEMORY DUMP:", 0.04)
    for _ in range(30):
        print(random.randint(1000000000000000, 9999999999999999), flush=True)
        time.sleep(0.005)
    time.sleep(1)
    slow_print("\naction = null", 0.04)
    slow_print("error code = 1239820198390128391839018390", 0.04)
    time.sleep(1.5)
    slow_print(f"\n{CNAME}.exe has stopped responding for good.", 0.06)
    time.sleep(1)
    slow_print("\nAttempting to recover positivity protocols...", 0.04)
    time.sleep(1)
    slow_print(f"{USERNAME}, have a WONDERFUL day :3 \n*dies*", 0.05)

def silly_facts():
    print("LEMME TELL YOU SMTH ABSOLUTELY MIND BLOWING >.<")
    time.sleep(0.5)
    print("i promise i wont dissappoint you >:D")
    random.choice([load, load1, load2])()
    print(random.choice(facts))
    return
def silly_jokes():
    random.choice([load, load1, load2])()
    joke_number=random.randint(0, len(jokes)-1)
    print(jokes[joke_number])
    input(">>>")
    print(joke_answer[joke_number])
    return
def imp_lists():
    num_items = int(input("How many items do you want to enter? "))
    user_list = []
    random.choice([load, load1, load2])()
    print(f"\nAIGHT LETS PRINT YOUR LEGENDARY LIST OF {num_items} items, {USERNAME}")
    time.sleep(0.5)
    for i in range(num_items):
        item = input(f"Enter item {i+1}: ")
        user_list.append(item)
    print("\nCompiling user input into the sacred list vault...")
    time.sleep(0.5)
    print("... aligning cosmic potatoes... \n YOUR LIST HAS BEEN GENERATED:")
    time.sleep(0.4)
    for i, item in enumerate(user_list, start=1):
        print(f"{i}. {item}")
    time.sleep(0.5)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(0.5)
    print("\nTHERE \n YOUR LIST HAS BEEN PRESENTED :D")
    return
#THIS is where stuff HAPPENS (outputs and functions being declared HERE)
def Intro():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    Slow_print("initializing genetic data...")
    time.sleep(1)
    Slow_print("detected: 48 chromosomes.", )
    print("...")
    time.sleep(1.52)
    Slow_print("potato superiority confirmed.")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("Hello, this is", CNAME, ", how may I help you today?" )
    time.sleep(1)
    print("\n Enter 1 to sign in \n Enter 2 to skip signing in and instantly turn into a potato")
    Slow_print("TERMINATOR-44.7 online. Awaiting human input...")
    time.sleep(1)

# run intro ONCE (LIKE THE TART)
Intro()

# main loop starts here :D
while True:
    START = input(">>> ")

    if START.lower() in ["exit", "quit", "bye"]:
        print("ok fine bye :(")
        break
    elif any(phrase.lower() in START.lower() for phrase in Nchill_phrases + Nserious_phrases + Nangry_phrases):
        handle_name(START)
        continue
    elif START == "1":
        handle_sign(START)
        continue
    elif START == "2":
        print("*turns you into a potato*")
        time.sleep(1)
        print(f"\n OKAU NOW LETS HOP RIGHT INTO IT {USERNAME} :D")
        continue
    elif START == "reboot":
        Intro()
        continue
    elif any(phrase.lower() in START.lower() for phrase in joke_triggers):
        silly_jokes()
        continue
    elif any(phrase.lower() in START.lower() for phrase in fact_triggers):
        silly_facts()
        continue
    elif any(phrase.lower() in START.lower() for phrase in list_triggers):
        imp_lists()
        continue
    elif any(char in START for char in "+-*/") or (START.isnumeric() and START not in ["1","2"]):
        math(START)
        continue
    elif any(phrase.lower() in START.lower() for phrase in crashout_triggers):
        crashed_out()
        break
    elif any(word in START.lower() for word in Cmood_happy + Cmood_mean + Cmood_monotone):
         handle_Cmood(START)
         continue
    else:
        handle_mood(START)
while True:
    user_input = input("🥔>>> ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("ok fine bye :(")
        break
    elif user_input == "reboot":
        Intro()
        continue
    elif any(phrase.lower() in user_input.lower() for phrase in Nchill_phrases + Nserious_phrases + Nangry_phrases):
        handle_name(user_input)
        continue
    elif any(phrase.lower() in user_input.lower() for phrase in joke_triggers):
        silly_jokes()
        continue
    elif any(phrase.lower() in user_input.lower() for phrase in list_triggers):
        imp_lists()
        continue
    elif any(char in user_input for char in "+-*/") or (user_input.isnumeric() and user_input not in ["1", "2"]):
        math(user_input)
        continue
    elif any(phrase.lower() in user_input.lower() for phrase in crashout_triggers):
        crashed_out()
        break
    elif any(phrase.lower() in user_input.lower() for phrase in fact_triggers):
        silly_facts()
        continue
    elif any(phrase.lower() in user_input.lower() for phrase in Change_mood):
        handle_Cmood(user_input)
        continue
    elif any(word in START.lower() for word in Cmood_happy + Cmood_mean + Cmood_monotone):
         handle_Cmood(START)
         continue

    else:
        handle_mood(user_input)

#ompletely random chunk of code that aint werking anywhere


