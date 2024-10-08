from langchain.chains import SimpleChain
from langchain.prompts import PromptTemplate

# Utility function to generate itinerary using LangChain
def create_itinerary_chain(user_profile):
    # Define the prompt template
    template = """
    Based on the following user profile, generate a personalized travel itinerary:
    User profile: {user_profile}
    """
    
    prompt = PromptTemplate(input_variables=["user_profile"], template=template)
    
    # Create a simple chain to handle the prompt and itinerary generation
    chain = SimpleChain(
        prompt=prompt,
    )

    # Run the chain to generate the itinerary
    itinerary = chain.run({"user_profile": user_profile})
    
    return itinerary
