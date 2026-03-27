from dotenv import load_dotenv
import time
import streamlit as st
import pandas as pd
from scraper import get_amazon_data  # Custom function to scrape data from Amazon
from analyzer import analyze_sentiment  # Custom function to analyze sentiment of reviews

load_dotenv()

# Configure the Streamlit page
st.set_page_config(page_title="AI Competitor Monitor", page_icon="📈")
st.title("🚀 Competitor Price & Sentiment Monitor")
st.markdown("Enter an Amazon URL to track pricing and analyze customer satisfaction instantly.")
st.caption("⚡ Demo app — limited to 3 analyses per session with a 30s cooldown to manage API costs.")

# --- Session-based rate limiting ---
COOLDOWN_SECONDS = 30   # seconds between requests
MAX_REQUESTS = 3        # max analyses per session

if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0
if "request_count" not in st.session_state:
    st.session_state.request_count = 0

# Input field for the user to paste the Amazon product URL
target_url = st.text_input("Paste Amazon Product Link Here:")

# This block executes when the user clicks the "Analyze Product" button
if st.button("Analyze Product"):
    if target_url:
        now = time.time()
        time_since_last = now - st.session_state.last_request_time

        # Check session request cap
        if st.session_state.request_count >= MAX_REQUESTS:
            st.error(f"🚫 You've reached the {MAX_REQUESTS}-analysis limit for this session. Open a new tab to continue.")
        # Check cooldown between requests
        elif time_since_last < COOLDOWN_SECONDS:
            remaining = int(COOLDOWN_SECONDS - time_since_last)
            st.warning(f"⏳ Please wait {remaining}s before the next request.")
        else:
            # Update rate limit counters
            st.session_state.last_request_time = now
            st.session_state.request_count += 1

            # Show a loading spinner while the scraping and analysis are in progress
            with st.spinner("Scraping Amazon and calling AI..."):
                # Step 1: Scrape the product data from the provided URL
                data = get_amazon_data(target_url)
                
                # Handle cases where scraping might fail
                if "error" in data:
                    st.error(f"Failed to scrape: {data['error']}")
                else:
                    # Step 2: Display the basic product information
                    col1, col2 = st.columns(2)
                    col1.metric("Product Name", data['title'][:50] + "...")
                    col2.metric("Current Price", data['price'])
                    
                    # Step 3: Analyze the sentiment of the scraped reviews using the AI function
                    sentiment_summary = analyze_sentiment(data['reviews'])
                    
                    # Step 4: Display the AI-generated sentiment analysis
                    st.subheader("🤖 AI Sentiment Analysis")
                    st.info(sentiment_summary)
                    
                    # Step 5: Display the raw reviews in a table for transparency
                    st.subheader("📝 Raw Reviews Scraped")
                    df = pd.DataFrame(data['reviews'], columns=["Review Content"])
                    st.table(df)
    else:
        # Show a warning if the user clicks the button without entering a URL
        st.warning("Please enter a valid URL.")