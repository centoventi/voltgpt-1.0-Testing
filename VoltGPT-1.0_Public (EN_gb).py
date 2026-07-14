from openai  import openai  
# If you see an error here, please ignore it, it means you do not have OpenAI package installed (pip install openai)

openai.api_key = "Replace with API-Key" # Replace with your own API key
if not openai.api.key: # Failed API-Key check.
    print("Invalid API key.")
    exit(1) # Exits with code 1 (Error) 
if openai.api.key: # Passed API-Key check.
    print("Valid API key detected, proceeding...") # If the API key is valid the script proceeds

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Replace this with whatever you want, must be a valid prompt/question"}]) # Ask whatever you want here, must be valid otherwise the check will return with an error/warning to the terminal                                              

if  not completion.choices: # Does a check to see if the API returned any valid choices
    print("Error: Unexpected error happened - May be because of the API key being invalid or the prompt being invalid.")  # Executes a check and in case of invalid prompt/API key prints the error/warning message onto the terminal 
else: exec(completion.choices[0].message.content) # If passed the check, executes the content of the first choice returned by the API
if not completion.choices[0].message.content:
    print("1: Exit code 1 generated, unexpected error, please check error logs for info.") # If the content of the first choice is empty or invalid the script exits with an error message and generates exit code 1 (error)
    exit(1) # If the content of the first choice is empty, exits with error code 1 (Error)
else: exec(completion.choices.message.content) # If the content of the first choice made is not empty it will be executed by the API. 
print("0: Exit code 0 generated, task executed by python interpreter successfully.") # Prints this message to the terminal if the task was completed successfully. 
exit(0) # Exits with code 0 (Success)