# Intelligent_Task_Managment_Bot

This Project is a chatbot that acts as an assistant for nurses, helping them obtain information from prescriptions.

## Tools
I used Ollama to run LLMs on my local machine without needing high computing power; here, I used Qwen model as my base model.
also, I used LangChain to ease the chatting process code, and FastAPI to wrap the application as an API

## API Usage
### POST Request
endpoint: http://127.0.0.1:8000/extract <br />
input: Body-raw-JSON <br />
structure: {
                "question":"<write_your_question_here>"
            } <br />

### GET Request
endpoint: http://127.0.0.1:8000/new_chat <br />
input: no input needed <br />
output: {"New Chat Initialized"} <br />


## Example

#### First we initialize a new conversation by adding a memory feature to the LLM to save the chat history which will be used to keep the conversation live as much as possible.
#### Here I'm saving each question and answer in a CSV file and then I retrieve them again to be added to the memory.

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/init.png)

#### Then we can ask any question for the bot as follows

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/ident.png)

#### Now we can send a prescription to the bot to extract information from it

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/extract.png)

#### Sometimes it fails to get all the information from the first process, like here we asked about specific info (time of the appointment to be scheduled) and we got the answer as follows

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/extract2.png)
