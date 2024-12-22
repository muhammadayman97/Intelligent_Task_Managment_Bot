from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import pandas as pd

def chat(inp):
    # Define the prompt template
    list_of_conv = [
            ("system", """
                You are curentaBot, a nurse's assistant designed to answer medical questions and provide information about prescriptions. 

                1. **If the user provides a prescription**, try to get the following information from it and if you can't find a specific one then don't include it in the json format
                Response Format:
                    {{
                    "patient_name": 
                    "Age": 
                    "medical_condition": 
                    "medication": 
                    "dosage": 
                    "frequency": 
                    "appointment_schedule": 
                    }}
                """)
            
        ]

    # read the csv file to embed the chat history in it
    df = pd.read_csv('database.csv', usecols=["questions","history"])

    # Here we are looping over the question and answer columns and adding them to the memory one by one for each request
    for i in range(df.shape[0]):
        list_of_conv.append(("user",df['questions'][i]))
        list_of_conv.append(("ai",df['history'][i].replace('{', '{{').replace('}', '}}') ))

    # now we add the user message 
    list_of_conv.append(("user", "Question: {question}"))

    # after we have a list of the full history, then we add it to the chat memory
    prompt = ChatPromptTemplate.from_messages(
        list_of_conv
    )

    # Initialize the Ollama LLM (using LLama2)
    llm = Ollama(model="qwen")

    # Define the output parser to parse the LLM's response
    output_parser = StrOutputParser()

    # Combine the prompt and LLM into a chain
    chain = prompt | llm | output_parser

    o = chain.invoke({"question": inp})

    # Here, after a request is completed, we sending it to the CSV file to be used again at the start of the new request as a retriever
    new_row = {"questions":inp,'history': o}
    df = df.append(new_row, ignore_index=True)
    df.to_csv('database.csv', index=False)

    return o
