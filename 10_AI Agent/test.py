import requests
import json
import os
import time
import sys 

# --- Configuration ---

# This key is intentionally left empty. The environment will securely and 
# automatically inject the necessary API credentials at runtime.
GEMINI_API_KEY = "test_g7XEMeVNPGC0U5pcdXLb0oNh2nxvCyU5lyYRE6Ss"

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent"
MODEL_NAME = "gemini-2.5-flash-preview-05-20"
SYSTEM_PROMPT = (
    "You are a highly inspirational AI quote generator acting as a wise mentor. "
    "Your task is to generate a concise, uplifting, and unique motivational quote "
    "based on the user's request. The quote should be presented clearly without "
    "any extra formatting, surrounding text, or explanation."
)
MAX_RETRIES = 3

# --- Core Functions ---

def generate_quote(topic: str) -> str:
    """
    Generates a motivational quote by making a real-time call to the Gemini API.
    
    This function will ALWAYS attempt the network request.
    """
    
    # Construct the user query
    user_query = f"Generate a powerful motivational quote about: {topic}."

    # Construct the JSON payload for the API
    payload = {
        "contents": [{"parts": [{"text": user_query}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
    }

    headers = {
        'Content-Type': 'application/json',
    }
    
    # The environment will inject the key into the URL here where GEMINI_API_KEY is ""
    full_api_url = f"{API_URL}?key={GEMINI_API_KEY}"

    current_delay = 1 

    for i in range(MAX_RETRIES):
        try:
            print(f"Attempting REAL-TIME quote generation via Gemini API (Attempt {i+1})...")
            
            # Make the API call
            response = requests.post(full_api_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status() 

            # Parse the JSON response
            result = response.json()
            
            # Extract the text from the response structure
            text_part = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text')
            
            if text_part:
                return text_part.strip()
            else:
                return "Error: AI returned a successful response but no quote text was found."

        except requests.exceptions.HTTPError as e:
            # Handle HTTP errors (e.g., key invalid, server error)
            error_message = f"HTTP Error {e.response.status_code}: {e.response.text}"
            print(f"Request failed: {error_message}")
            if i < MAX_RETRIES - 1:
                print(f"Retrying in {current_delay} second(s)...")
                time.sleep(current_delay)
                current_delay *= 2
                continue
            return f"Final Error: Failed to connect to AI after {MAX_RETRIES} attempts. {error_message}"
        
        except requests.exceptions.RequestException as e:
            # Handle network errors (like the NameResolutionError you've been seeing)
            return f"Network Error (DNS/Connection Failure): Could not connect to the API. {e}"

        except Exception as e:
            # Catch all other unexpected errors
            return f"An unexpected error occurred: {e}"

    return "Final Error: All retries failed."


# --- Main Execution Block ---

if __name__ == "__main__":
    try:
        # Filter out arguments that look like internal file paths or system flags.
        internal_path_prefixes = ['/tmp/sandbox_', '--']
        user_args = [
            arg for arg in sys.argv[1:] 
            if not any(arg.startswith(prefix) for prefix in internal_path_prefixes)
        ]
        
        if user_args:
            motivation_topic = " ".join(user_args)
        else:
            motivation_topic = "general motivation"
            
    except ImportError:
        print("A core Python library is missing. Please check your Python environment.")
        exit(1)

    print("-" * 50)
    print("Welcome to the Python Motivational Quote Agent!")
    print(f"Generating a quote automatically on: '{motivation_topic}'")
    print("-" * 50)

    print(f"Searching for wisdom on: '{motivation_topic}'...")
    
    # Generate and print the quote (This is now a forced API call!)
    quote = generate_quote(motivation_topic)

    print("\n" + "=" * 50)
    print("✨ Your Motivational Quote ✨")
    print("=" * 50)
    print(f"\n{quote}\n")
    print("=" * 50)
