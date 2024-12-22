# Intelligent_Task_Managment_Bot

This Project is a chatbot that acts as an assistant for nurses, helping them obtain information from prescriptions.

## Tools
I used Ollama to run LLMs on my local machine without needing high computing power; here, I used Qwen model as my base model.

## Example

#### First we initialize a new conversation by adding a memory feature to the LLM to save the chat history which will be used to keep the conversation live as much as possible.
#### Here I'm saving each question and answer in a CSV file and then I retrieve them again to be added to the memory.

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/init.png)

#### Then we can ask any question for the bot as follows

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/ident.png)

#### Now we can send a prescription to the bot to extract information from it

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/extract.png)

#### Sometimes it fails to get all the information from the first process, so here we asked about specific info and we got the answer as follows

![My Image](https://github.com/muhammadayman97/Intelligent_Task_Managment_Bot/blob/main/images/extract2.png)
