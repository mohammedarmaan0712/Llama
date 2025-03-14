from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from helper import return_open_mode_for_txt_files

template = """"
Answer the question below:

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation ():
    context = ""
    print ("Welcome to TutorGPT Type exit to quit. What do you wish to learn today?")
    subject = input("You: ")
    print("Great! Let's assess your skill level in ", subject)
    levels =["beginner", "intermediate", "advanced"]
    score = 0
    if not subject == "exit":
        for level in levels:
            question = chain.invoke({"context":context, "question": f"Give a {level} level question for " + subject})
            print ("Bot:", question)
            answer_recieved = input("Your answer: ")
            answer = chain.invoke({"context":context, "question": "Is this the answer: " + answer_recieved + " (Answer y for yes and n for no)"})
            print (answer)

            if answer == 'Y' or answer == 'y':
                score +=1
        print (score)

    print (context)





if __name__ == "__main__":
    handle_conversation()


''''
Vectorize the text

Embed the values extracted in the text file to a database 

retrieve the most relevant detail given an example prompt

generate !!
'''