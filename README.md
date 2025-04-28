### AI Thai Language Agent 🛠️



The attached Python script main.py can be used to answer any queries related to learning or understanding the Thai language, for English speakers. It connects to the gpt-4o LLM model to answer any queries.



How to use 🚀🚀🚀


Simply replace the string `"How do I say 'Hello' in Thai?"` in:

`await Console(agent.run_stream(task="How do I say 'Hello' in Thai?",cancellation_token=CancellationToken()))`

with any question you have and execute the script, and the output will be displayed in the console.


You will need a GITHUB personal access token or similar to connect to the API. If you have a follow up question or want to reply to something the AI agent has said, simply replace the string with your new question, as the AutoGen assistant agent will remember your conversation history. Save your personal access token in a separate .env file (e.g. `GITHUB_TOKEN=my_github_token`) 

