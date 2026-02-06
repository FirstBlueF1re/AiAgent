import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.prompts import system_prompt
from functions.call_function import available_functions

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)
if api_key == None:
    raise Exception("the api key is not define or incorrect.")

#Main function for sending prompt to ai
def general_response(user_input, verbose=False):
    #new list of user's prompts
    messages = [types.Content(role="user", parts=[types.Part(text=user_input)])]
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config = types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt)
    )    
    if verbose:
        print(f"User prompt: {user_input}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    #changed response.text --> response.function_calls
    function_calls = response.function_calls
    if function_calls:
        for function_call in function_calls:        
            print(f"Calling function: {function_call.name}{function_call.args}.")
    else:
        print(response.text)

#argument parser
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


#Run code ----------------------------------------------
general_response(args.user_prompt, verbose=args.verbose)
