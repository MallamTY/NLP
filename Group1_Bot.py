from dataset import kinship_terms
from indigenous_dataset import yoruba


def chatbot(user_input):
    user_input = user_input.lower()
    response = None

    for term, meaning in kinship_terms.items():
        if (user_input.startswith('who is') and term in user_input[7:]) or user_input.startswith('who is a') and term in user_input[9:]:
            response = meaning
            break
        
        elif term in user_input:
            response = meaning
            break

    if response is None:
        response = "I'm sorry, I don't have a meaning for the kinship word you supplied or perhaps you haven't supplied one, please try again !!!"

    return response

def indigenious_chatbot(user_input):
    user_input = user_input.lower()
    response = None

    for term, meaning in yoruba.items():
        if (user_input.startswith('tani') and term in user_input[5:]) or user_input.startswith('tani a n pe ni') and term in user_input[16:]:
            response = meaning
            break
        
        elif term in user_input:
            response = meaning
            break

    if response is None:
        response = "Mabinu, mi o ni idahun si ibeere ti o bi mi yi, tabi o i ti bi mi ni nkankan, gbiyanju ni enkan si !!!"
        
    return response
    

domain = input('\nWhich language will you like to converse with? >>> ')

if domain.lower() == 'english': 

    while True:
        user_input = input('\nUser >>> ')
        if len(user_input) == 0:
            print("\nGroup 1 bot >>> You've asked nothing \n")

        elif user_input.lower() == "exit" or user_input.lower() == "goodbye" or user_input.lower() == "bye" or user_input.lower() == "bye-bye":
            break

        else:
            response = chatbot(user_input)
            print(f"\nGroup 1 Bot >>> {response}")

elif domain.lower() == 'yoruba':
     while True:
        user_input = input('\n Alo Ero >>> ')
        if len(user_input) == 0:
            print("\nEro Egbe Kini >>> o ti bere nkankan \n")

        elif user_input.lower() == "jade" or user_input.lower() == "odigba" or user_input.lower() == "odabo":
            break

        else:
            response = indigenious_chatbot(user_input)
            print(f"\nEro Egbe Kini >>> {response}")
