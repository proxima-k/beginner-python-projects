# https://github.com/jorgegonzalez/beginner-projects#mad-libs-story-maker
# FINISHED ON 24.MAR.20
import re, time, os

class Madlibs:

    # STARTING THE PROGRAM
    def __init__(self,story):
        self.story = story # Stores a list
        self.name_LIST = []
        self.main_event()

    # MAIN EVENT
    def main_event(self):
        print("|-----------[ Welcome to Mad Libs! ]-----------|\nYou know the rules. If you don't, google it o.<")
        print("Alright. Let's begin!")
        new_story = []
        for sentence in self.story:
            new_story.append(self.fill_in(sentence))
        self.review(new_story)

    # REPLACING THE REQUIRED WORDS WITH THE INPUT OF THE USER
    def fill_in(self,sentence):
        # MATCHING THE WORDS
        sentenceLIST = sentence.split()
        pattern = r"\([A-Z]+\)"  # (B)
        pattern_name = r"\(Name([0-9])+\)"
        pattern_digit = r"\d+"

        newsentence = []
        for word in sentenceLIST:
            match = re.search(pattern, word)
            namematch = re.search(pattern_name,word)
            # (XXX)
            if match:
                bracket_index = (word.index("(") + 1, word.index(")"))
                requestWORD = input(f"I need a(n) {word[bracket_index[0]:bracket_index[1]]}\n>>> ")
                if re.search(r"\(NAME\)",word):
                    requestWORD = requestWORD.title()
                    self.name_LIST.append(requestWORD)

                word = re.sub(pattern,requestWORD,word)
            # (Name1......)
            if namematch:
                digit = re.findall(pattern_digit,word)
                digit = int(digit[0])
                word = re.sub(pattern_name,self.name_LIST[digit-1],word)

            newsentence.append(word)
        # JOINING THE LIST INTO A A STRING
        s = " "
        newsentence =  s.join(newsentence)
        return newsentence

    # PRINTING OUT THE SENTENCE
    def review(self,story):
        print("\nYou used some great words.")
        print("Joining the words you've put....")
        time.sleep(2)
        print("Here's the story you made\n-----------------------------")
        for line in story:
            print(f"{line}")


story = ["The (ADJECTIVE) (NAME) tried to (VERB) a (NOUN), (NUMBER) times. However, he was (VERB) by it instead. Later, a wild (NAME) appeared out of no where. Just to kill (Name1). Without noticing, (Name2) got (VERB) by (Name1) and died as well. THE END"]
# story = ["(NAME) (Name1) (NAME) (Name2) (Name1) (Name2)"]
# print(os.getcwd())
# with open("shortstory.txt", "r") as rf:
#     story = rf.readlines()


program = Madlibs(story)