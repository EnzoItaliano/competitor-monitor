import os
from openai import OpenAI

# Initialize the OpenAI client using the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(reviews_list):
    """
    Analyzes the sentiment of a list of reviews using OpenAI's GPT-3.5-turbo model.

    Args:
        reviews_list: A list of strings, where each string is a customer review.

    Returns:
        A string summarizing the sentiment of the reviews.
    """
    # Combine all reviews into a single string to send to the AI
    combined_reviews = " ".join(reviews_list)
    
    # Send the combined reviews to the OpenAI API for sentiment analysis
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a market analyst. Summarize the sentiment of these reviews in one word (Positive, Neutral, or Negative) and give a 1-sentence reason."},
            {"role": "user", "content": combined_reviews}
        ]
    )
    # Return the content of the AI's response
    return response.choices[0].message.content