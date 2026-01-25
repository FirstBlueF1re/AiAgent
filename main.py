import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)
if api_key == None:
    raise Exception("the api key is not define or incorrect.")

#Main function for sending prompt to ai
def general_response(user_input, verbose=False):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages
    )
    
    if verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)

#argument parser
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

#new list of user's prompts
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

#Run code ----------------------------------------------
general_response(messages, verbose=args.verbose)
