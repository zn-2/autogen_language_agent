### AI Thai Language Agent 


The attached Python script autogen_ai_language_assistant.py can be used to answer any queries related to learning or understanding the Thai language, for English speakers. It connects to the gpt-4o LLM model to answer any queries.


To use: 
Simply replace the string "Can you focus on pronounciation?" in:

await Console(agent.run_stream(task="Can you focus on pronounciation?",cancellation_token=CancellationToken()))

and with any question you have and execute the script, and the output will be displayed in the console.

You will need a GITHUB personal access token or similar to connect to the API. If you have a follow up question or want to reply to something the AI agent has said, simply replace the string with your new question, as the AutoGen assistant agent will remember your conversation history. 

