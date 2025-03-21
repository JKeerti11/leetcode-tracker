import streamlit as st
import pandas as pd
import datetime
from leetcode_api import fetch_leetcode_stats
from debug_code import debug_code

st.title("🔥 LeetCode Performance Tracker with Debugger")

# Input: LeetCode Username
username = st.text_input("Enter your LeetCode username:")

if username:
    data = fetch_leetcode_stats(username)

    if data:
        st.subheader("📊 Your LeetCode Stats:")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Easy", data['easySolved'])
        col2.metric("Medium", data['mediumSolved'])
        col3.metric("Hard", data['hardSolved'])

        # Visualizing progress
        stats = {
            "Difficulty": ["Easy", "Medium", "Hard"],
            "Solved": [data['easySolved'], data['mediumSolved'], data['hardSolved']]
        }

        df = pd.DataFrame(stats)
        st.bar_chart(df.set_index("Difficulty"))

        # Store timestamp for progress
        progress = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "easy": data['easySolved'],
            "medium": data['mediumSolved'],
            "hard": data['hardSolved']
        }

        # Store in MongoDB
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017/")
        db = client["leetcode_tracker"]
        collection = db["progress"]
        collection.insert_one(progress)
        
        st.success("✅ Progress Saved!")
    else:
        st.error("❌ Invalid username or API issue")
st.subheader("🛠️ Code Debugger")

code = st.text_area("Paste your LeetCode code for debugging:")

if st.button("Debug Code"):
    if code:
        result = debug_code(code)
        st.subheader("Debugging Result:")
        st.write(result)
    else:
        st.error("❌ Please enter some code to debug.")
