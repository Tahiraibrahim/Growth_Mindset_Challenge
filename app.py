import streamlit as st
import random

# Page configuration with custom theme
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS for styling (added full-page background color)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #E8F6F3, #D1F2EB) !important;
        padding: 20px;
    }
    body {
        background: linear-gradient(135deg, #E8F6F3, #D1F2EB) !important;
    }
    .mega-title {
        color: #1A5276;
        text-align: center;
        font-size: 56px !important;
        font-weight: bold;
        padding: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .header-text {
        color: #2E86C1;
        font-size: 32px;
        padding: 20px 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .quote-box {
        background-color: #D4E6F1;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .quotes-section {
        background-color: #E8F8F5;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
    }
    .success-box {
        background-color: #D5F5E3;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .motivation-button {
        background-color: #3498DB;
        color: white;
        padding: 15px 30px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-size: 18px;
        margin: 20px 0;
        transition: all 0.3s;
    }
    .motivation-button:hover {
        background-color: #2874A6;
    }
    .footer-text {
        text-align: center;
        color: #566573;
        padding: 30px;
    }
    </style>
    <div class="main">
    """, unsafe_allow_html=True)

# Title Section with enhanced styling
st.markdown('<p class="mega-title">🌱 Growth Mindset Challenge</p>', unsafe_allow_html=True)

# Inspirational Introduction
st.markdown("""
    <div style="text-align: center; padding: 25px; background-color: #E8F8F5; border-radius: 15px; margin: 20px 0;">
    Embark on a transformative journey of personal growth and development.
    Let's unlock your potential and embrace the power of a growth mindset! 🚀
    </div>
    """, unsafe_allow_html=True)

# Quotes Collection
inspirational_quotes = [
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Everything you've ever wanted is sitting on the other side of fear. - George Addair",
    "The mind is everything. What you think you become. - Buddha",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "Nothing is impossible. The word itself says 'I'm possible!' - Audrey Hepburn"
]

# Quote Section with styled box and random quote
st.markdown('<h2 class="header-text">✨ Today\'s Wisdom</h2>', unsafe_allow_html=True)
st.markdown(f"""
    <div class="quote-box">
    {random.choice(inspirational_quotes)}
    </div>
    """, unsafe_allow_html=True)

# Challenge Section
st.markdown('<h2 class="header-text">🎯 Your Current Challenge</h2>', unsafe_allow_html=True)
user_input = st.text_input("What obstacle are you ready to overcome today?")

if user_input:
    st.markdown(f"""
        <div class="success-box">
        🌟 You're facing: {user_input}<br>
        Remember: Every challenge is an opportunity for growth. You've got this! 💪
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Share your challenge - it's the first step towards overcoming it! 🌱")

# Reflection Section
st.markdown('<h2 class="header-text">🤔 Mindful Reflection</h2>', unsafe_allow_html=True)
reflection = st.text_area("What have you learned from your recent experiences?")

if reflection:
    st.markdown(f"""
        <div class="success-box">
        💭 Powerful reflection! Your thoughts: {reflection}<br>
        Keep this growth mindset - it's your superpower! ✨
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("📝 Take a moment to reflect - it's where deep learning happens!")

# Achievement Section
st.markdown('<h2 class="header-text">🏆 Victory Corner</h2>', unsafe_allow_html=True)
achievements = st.text_input("What victory would you like to celebrate today?")

if achievements:
    st.markdown(f"""
        <div class="success-box">
        🎉 Wonderful Achievement: {achievements}<br>
        Let this success fuel your journey forward! 🌟
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("🌟 Every step forward counts - share your win, no matter how small!")

# Additional Quotes Section
st.markdown('<h2 class="header-text">📚 More Inspirational Quotes</h2>', unsafe_allow_html=True)
st.markdown('<div class="quotes-section">', unsafe_allow_html=True)
for quote in inspirational_quotes[:5]:  # Display first 5 quotes
    st.markdown(f"• {quote}")
st.markdown('</div>', unsafe_allow_html=True)

# Need Motivation Button
if st.button("🔥 Need Motivation?", key="motivation_button"):
    motivational_messages = [
        "You are stronger than you think! Keep pushing forward! 💪",
        "Every expert was once a beginner. Your journey matters! 🌟",
        "Small progress is still progress. Be proud of how far you've come! 🎯",
        "Your potential is unlimited. Believe in yourself! ✨",
        "Today's efforts are tomorrow's successes! Keep going! 🚀"
    ]
    st.markdown(f"""
        <div class="success-box">
        {random.choice(motivational_messages)}
        </div>
        """, unsafe_allow_html=True)

# Footer with styling
st.markdown("""
    <div class="footer-text">
    <hr>
    🌱 Your potential is limitless. Keep growing, keep glowing! 🌟<br>
    Created with ❤️ by Tahira Ibrahim
    </div>
    </div>
    """, unsafe_allow_html=True)
