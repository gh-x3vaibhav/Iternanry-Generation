import sys
import json
from langchain_utils import create_itinerary_chain
from openai_config import setup_openai

# Initialize LangChain
setup_openai()

# Read user data from stdin (provided by Node.js)
user_data = sys.stdin.read()
user_profile = json.loads(user_data)

# Generate personalized itinerary using LangChain
itinerary = create_itinerary_chain(user_profile)

# Output itinerary
print(itinerary)
