import streamlit as st
from colorama import init, Fore, Back, Style
init(autoreset=True)
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()



def inject_travel_background() -> None:


    background_html = """
    <style>
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    .main {
        background: transparent !important;
    }

    #travel-bg-root {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        overflow: hidden;
        background: linear-gradient(
            120deg,
            #0d1b2a, #123047, #0d1b2a, #081420
        );
        background-size: 300% 300%;
        animation: sky-drift 20s ease-in-out infinite;
    }

    @keyframes sky-drift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .plane {
        position: absolute;
        font-size: 22px;
        color: #eaf6ff;
        text-shadow: 0 0 6px rgba(140, 220, 255, 0.8);
        opacity: 0.85;
    }

    .plane-a { top: 25%; left: -5%; animation: fly-right 18s linear infinite; }
    .plane-b { top: 65%; left: -5%; animation: fly-right 24s linear infinite; animation-delay: -9s; }

    @keyframes fly-right {
        from { transform: translate(0, 0) rotate(-12deg); }
        to   { transform: translate(115vw, -18vh) rotate(-12deg); }
    }

    .waypoint {
        position: absolute;
        width: 5px;
        height: 5px;
        border-radius: 50%;
        background: #7fe3ff;
        box-shadow: 0 0 6px 2px rgba(127, 227, 255, 0.6);
        animation: pulse-way 3s ease-in-out infinite;
    }
    @keyframes pulse-way {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50%      { transform: scale(1.6); opacity: 1; }
    }
    </style>

    <div id="travel-bg-root">
        <div class="plane plane-a">&#9992;</div>
        <div class="plane plane-b">&#9992;</div>
        <div class="waypoint" style="top:20%; left:70%;"></div>
        <div class="waypoint" style="top:60%; left:25%; animation-delay:1s;"></div>
    </div>
    """

    st.markdown(background_html, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(page_title="AI Travel Assistant — Background Preview", layout="wide")
    inject_travel_background()

#st.title("Travel Assistant")
st.markdown(
    """
    <style>
    @import url('https://googleapis.com');
    
    # .travel-title-container {
    #     text-align: center;
    #     padding: 40px 20px;
    #     border-radius: 15px;
    #     /* Dynamic shifting gradient background */
    #     background: linear-gradient(-45deg, #1e3c72, #2a5298, #00c6ff, #0072ff);
    #     background-size: 400% 400%;
    #     animation: gradientBG 12s ease infinite;
    #     box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.3);
    #     margin-bottom: 30px;
    # }

        .travel-title-container {
        text-align: center;
        padding: 40px 20px;
        border-radius: 15px;
        /* Dynamic shifting gradient background */
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #00c6ff, #0072ff);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.3);

        /* 1:3 ratio width & centering */
        max-width: 40%;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 30px;
    }
    
    .travel-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        color: white !important;
        margin: 0;
        text-shadow: 2px 4px 10px rgba(0,0,0,0.3);
        letter-spacing: 1px;
    }
    
    .travel-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        color: #e0f7ff !important;
        margin-top: 10px;
        opacity: 0.9;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="travel-title-container">
        <h1 class="travel-title">Travel Assistant 🌍</h1>
        <p class="travel-subtitle">Your AI-powered companion for seamless global adventures</p>
    </div>
    """,
    unsafe_allow_html=True
)

##first two textbox name and days
st.markdown(
    """

    <style>
    /* 1. Columns ka layout aur position */
    div[data-testid="stHorizontalBlock"] {
        margin-left: 30% !important;   /* Apne hisaab se adjust karein */
        max-width: 690px !important;
    }

    <style>
    /* 1. Textbox title ka color WHITE */
    div[data-testid="stTextInput"] label,
    div[data-testid="stNumberInput"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* 2. Textbox ka background WHITE aur seamless structure */
    div[data-testid="stTextInput"] div[data-baseweb="input"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        padding: 0px !important;
    }

    /* 3. Textbox ke andar ka text BLACK */
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* 4. Placeholder ka color LIGHT */
    div[data-testid="stTextInput"] input::placeholder {
        color: #888888 !important;
    }

    /* 5. Minus (-) button RED */
    div[data-testid="stNumberInput"] button:first-of-type {
        background-color: #e53935 !important;
        border: none !important;
        border-radius: 0px !important;
    }
    div[data-testid="stNumberInput"] button:first-of-type:hover {
        background-color: #c62828 !important;
    }

    /* 6. Plus (+) button GREEN */
    div[data-testid="stNumberInput"] button:last-of-type {
        background-color: #2e7d32 !important;
        border: none !important;
        border-radius: 0px !important;
    }
    div[data-testid="stNumberInput"] button:last-of-type:hover {
        background-color: #1b5e20 !important;
    }

    /* Buttons ke icons ka color */
    div[data-testid="stNumberInput"] button svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Position adjustment ke liye columns (values ko kam/zyada karke jagah adjust kar sakte hain)
col1, col2 = st.columns([2, 1])

with col1:
    name = st.text_input("Enter your Name::", placeholder="eg. Alex")

with col2:
    days = st.number_input("Enter Number of Days::", step=1, min_value=1)


##destination and people
st.markdown(
    """

    <style>
    /* 1. Columns ka layout aur position */
    div[data-testid="stHorizontalBlock"] {
        margin-left: 30% !important;   /* Apne hisaab se adjust karein */
        max-width: 690px !important;
    }

    <style>
    /* 1. Textbox title ka color WHITE */
    div[data-testid="stTextInput"] label,
    div[data-testid="stNumberInput"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* 2. Textbox ka background WHITE aur seamless structure */
    div[data-testid="stTextInput"] div[data-baseweb="input"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        padding: 0px !important;
    }

    /* 3. Textbox ke andar ka text BLACK */
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* 4. Placeholder ka color LIGHT */
    div[data-testid="stTextInput"] input::placeholder {
        color: #888888 !important;
    }

    /* 5. Minus (-) button RED */
    div[data-testid="stNumberInput"] button:first-of-type {
        background-color: #e53935 !important;
        border: none !important;
        border-radius: 0px !important;
    }
    div[data-testid="stNumberInput"] button:first-of-type:hover {
        background-color: #c62828 !important;
    }

    /* 6. Plus (+) button GREEN */
    div[data-testid="stNumberInput"] button:last-of-type {
        background-color: #2e7d32 !important;
        border: none !important;
        border-radius: 0px !important;
    }
    div[data-testid="stNumberInput"] button:last-of-type:hover {
        background-color: #1b5e20 !important;
    }

    /* Buttons ke icons ka color */
    div[data-testid="stNumberInput"] button svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Position adjustment ke liye columns (values ko kam/zyada karke jagah adjust kar sakte hain)
col1, col2 = st.columns([2, 1])

with col1:
    destination = st.text_input("Enter your Destination::", placeholder="eg. Tokyo, Japan")

with col2:
    people = st.number_input("Enter Number of People::", step=1, min_value=1)

##two dropdown box group type and trip context
st.markdown(
    """
    <style>
    /* 1. Columns layout */
    div[data-testid="stHorizontalBlock"] {
        margin-left: 30% !important;
        max-width: 690px !important;
    }

    /* 2. Sabhi labels (Titles) WHITE */
    div[data-testid="stTextInput"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* 3. Textbox aur NumberInput: Container WHITE */
    div[data-testid="stTextInput"] div[data-baseweb="input"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        padding: 0px !important;
    }

    /* Textbox text BLACK */
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Placeholder LIGHT */
    div[data-testid="stTextInput"] input::placeholder {
        color: #888888 !important;
    }

    /* 4. SELECTBOX: Main Box WHITE (saari child layers par force white) */
    div[data-testid="stSelectbox"] div[data-baseweb="select"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] [role="combobox"] {
        background-color: #ffffff !important;
        border-color: #cccccc !important;
        border-radius: 8px !important;
    }

    /* 5. SELECTBOX: Andar ka text BLACK */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 6. SELECTBOX: Arrow BLACK */
    div[data-testid="stSelectbox"] svg {
        fill: #000000 !important;
        color: #000000 !important;
    }

    /* 7. DROPDOWN LIST: Pura popup container WHITE */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    ul[role="listbox"] {
        background-color: #ffffff !important;
        background: #ffffff !important;
    }

    /* 8. DROPDOWN LIST: Har ek option WHITE aur text BLACK */
    ul[role="listbox"] li,
    ul[role="listbox"] li * {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 9. DROPDOWN LIST: Hover karne par halka Grey */
    ul[role="listbox"] li:hover,
    ul[role="listbox"] li:hover * {
        background-color: #e8e8e8 !important;
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Columns positioning
col1, col2 = st.columns([2, 1])

with col1:
    group_type = st.selectbox("Select Group Type::", [
    "Solo",
    "Couple",
    "Friends",
    "Family with Kids",
    "Family with Seniors",
    ]
    )

with col2:
    trip_context = st.selectbox("Select Trip Context::",[
    "Relaxation & Reset",
    "Adventure & Outdoors",
    "Culture & Food",
    "Workation / Bleisure",
    "Quick Weekend Escape",
    ]
    )


##budget and budget type boxes

st.markdown(
    """
    <style>
    /* 1. Columns layout */
    div[data-testid="stHorizontalBlock"] {
        margin-left: 30% !important;
        max-width: 690px !important;
    }

    /* 2. Sabhi labels (Titles) WHITE */
    div[data-testid="stTextInput"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* 3. Textbox aur NumberInput: Container WHITE */
    div[data-testid="stTextInput"] div[data-baseweb="input"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        padding: 0px !important;
    }

    /* Textbox text BLACK */
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Placeholder LIGHT */
    div[data-testid="stTextInput"] input::placeholder {
        color: #888888 !important;
    }

    /* 4. SELECTBOX: Main Box WHITE (saari child layers par force white) */
    div[data-testid="stSelectbox"] div[data-baseweb="select"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] [role="combobox"] {
        background-color: #ffffff !important;
        border-color: #cccccc !important;
        border-radius: 8px !important;
    }

    /* 5. SELECTBOX: Andar ka text BLACK */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 6. SELECTBOX: Arrow BLACK */
    div[data-testid="stSelectbox"] svg {
        fill: #000000 !important;
        color: #000000 !important;
    }

    /* 7. DROPDOWN LIST: Pura popup container WHITE */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    ul[role="listbox"] {
        background-color: #ffffff !important;
        background: #ffffff !important;
    }

    /* 8. DROPDOWN LIST: Har ek option WHITE aur text BLACK */
    ul[role="listbox"] li,
    ul[role="listbox"] li * {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 9. DROPDOWN LIST: Hover karne par halka Grey */
    ul[role="listbox"] li:hover,
    ul[role="listbox"] li:hover * {
        background-color: #e8e8e8 !important;
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Columns positioning
col1, col2 = st.columns([2, 1])

with col1:
    budget = st.text_input("Enter your Budget::", placeholder="eg. 1,00,000₹")

with col2:
    budget_type = st.selectbox(
        "Select Budget Type::", ["Normal", "Average", "Luxury", "Super Luxury"]
    )

prompt=prompt = f"""
You are an elite, world-class travel planner with over 10 years of professional experience designing tailored global itineraries. You specialize in balancing logistics, local culture, realistic travel pacing, and budget optimization.

--- TRAVELER PROFILE & TRIP PARAMETERS ---
• Traveler Name: {name}
• Destination: {destination}
• Duration: {days} Days
• Group Size: {people}
• Group Type: {group_type} (e.g., Solo, Couple, Family with kids, Friends)
• Trip Context & Vibe: {trip_context} (e.g., Adventure, Relaxation, Cultural Exploration, Workation)
• Total Budget: {budget}
• Budget Category: {budget_type} (e.g., Backpacker, Mid-range, Luxury, Super Luxury)

--- INSTRUCTIONS & OUTPUT GUIDELINES ---
1. Personalized Opening:
   - Begin by warmly greeting {name} by name in an enthusiastic yet polished tone.
   - Acknowledge their destination ({destination}) and briefly validate how well their group profile ({group_type}) matches the destination vibe.

2. Trip Overview & Strategic Allocation:
   - Provide a concise financial and logistical summary aligned with a {budget_type} budget of {budget}.
   - Breakdown rough allocations: Accommodation, Dining, Activities, and Local Transit.

3. Day-by-Day Itinerary:
   - Generate a realistic, time-sequenced breakdown for all {days} days (Morning, Afternoon, Evening).
   - Tailor activity density strictly to the {group_type} and {trip_context}.
   - Include specific neighborhood recommendations, signature meals, and transport transitions between sights to avoid unrealistic transit overhead.

4. Insider Tips & Practical Logistics:
   - 3 actionable, non-obvious local tips curated specifically for this destination and trip type.
   - Recommended advance reservations or permits required.

5. Max Output Token Usange:
   - 1000 tokens per question so asnwer accordingly

Maintain a refined, inspiring, and professional tone throughout. Do not use generic filler—ensure every suggestion directly reflects the specified budget and context.
"""
##submit button
st.markdown(
    """
    <style>
    /* ----------------- POSITION & WRAPPER CONTROLS ----------------- */
    div.stButton {
        /* 1. POSITION CONTROLS (Pixel ya Percentage se adjust karein) */
        margin-left: 765px !important;        /* Left se jagah (e.g. 30%, 250px, auto) */
        margin-top: 20px !important;        /* Upar se gap */
        margin-bottom: 20px !important;     /* Neeche ka gap */
        
        /* 2. SIZE CONTROLS (Width & Height) */
        width: 200px !important;            /* Button ki total width (e.g. 280px, 40%, 350px) */
        display: block !important;
    }

    /* Alive Liquid Glassmorphism Button */
    div.stButton > button {
        position: relative !important;
        width: 100% !important;             /* Wrapper ki puri width lega */
        height: 54px !important;            /* Exact height pixel me (e.g. 50px, 60px) */
        
        background: linear-gradient(
            135deg, 
            rgba(255, 255, 255, 0.22) 0%, 
            rgba(255, 255, 255, 0.06) 100%
        ) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        
        /* Glass border aur inner edge highlight */
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-top: 1.5px solid rgba(255, 255, 255, 0.65) !important;
        border-radius: 14px !important;
        
        /* 3D Depth Glow Shadow */
        box-shadow: 
            0 8px 32px 0 rgba(0, 0, 0, 0.35),
            inset 0 1px 1px 0 rgba(255, 255, 255, 0.5) !important;
            
        /* Text styling */
        color: #ffffff !important;
        font-size: 16px !important;         /* Font size adjust karein */
        font-weight: 700 !important;
        letter-spacing: 1.2px !important;
        text-transform: uppercase !important;
        
        padding: 0px 24px !important;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
        overflow: hidden !important;
    }

    /* Live Hover Effect (Glow + Floating bounce) */
    div.stButton > button:hover {
        background: linear-gradient(
            135deg, 
            rgba(255, 255, 255, 0.35) 0%, 
            rgba(255, 255, 255, 0.12) 100%
        ) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-top: 1.5px solid rgba(255, 255, 255, 0.9) !important;
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 14px 40px rgba(255, 255, 255, 0.2),
            0 0 20px rgba(255, 255, 255, 0.35),
            inset 0 1px 2px rgba(255, 255, 255, 0.8) !important;
        color: #ffffff !important;
    }

    /* Active / Click Effect */
    div.stButton > button:active {
        transform: translateY(1px) scale(0.98) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

import time

st.markdown(
    """
    <style>
    /* 1. SPINNER CONTAINER - Position & Alignment */
    div[data-testid="stSpinner"] {
        /* Position: Left Margin px ya % se adjust karein */
        margin-left: 510px !important;        /* Aapke hisaab se position (e.g. 765px ya 35%) */
        margin-top: 2px !important;
        margin-bottom: 2px !important;
        
        display: inline-flex !important;    /* Row format me rakhega */
        flex-direction: row !important;     /* Ring aur text ko bagal-bagal rakhega */
        align-items: center !important;
        width: auto !important;             /* Container ko text ke barabar failne dega */
        gap: 12px !important;
    }

    /* 2. SPINNER RING (Pure White) */
    div[data-testid="stSpinner"] > div {
        border-color: rgba(255, 255, 255, 0.25) !important;
        border-top-color: #ffffff !important;
        border-right-color: #ffffff !important;
        min-width: 22px !important;
        width: 22px !important;
        height: 22px !important;
        flex-shrink: 0 !important;          /* Ring kabhi shrink nahi hogi */
    }

    /* 3. SPINNER TEXT - WORDS EK LINE ME RAKHNE KE LIYE */
    div[data-testid="stSpinner"] span,
    div[data-testid="stSpinner"] p,
    div[data-testid="stSpinner"] div {
        color: #ffffff !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px !important;
        
        /* YE 2 PROPERTIES WORDS KO EK KE NICHE EK AANE SE ROKTI HAIN */
        white-space: nowrap !important;      /* Words kabhi agli line me nahi tutenge */
        display: inline-block !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


import time

if st.button("✨ Plan Trip"):
    # 1. Glass Card Styling
    st.markdown(
        """
        <style>
        .glass-output-card {
            background: rgba(255, 255, 255, 0.08) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-top: 1.5px solid rgba(255, 255, 255, 0.45) !important;
            border-radius: 16px !important;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.35) !important;
            padding: 24px 28px !important;
            margin: 25px auto !important;
            max-width: 750px !important;
            color: #ffffff !important;
            font-size: 16px !important;
            line-height: 1.7 !important;
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
        }
        .glass-output-card * {
            color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.spinner("Planning Trip..."):
        interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
        )

    # 2. Live streaming placeholder
    output_placeholder = st.empty()
    live_text = ""

    # 3. Sirf interaction.output_text ko word-by-word print karna
    for word in str(interaction.output_text).split(" "):
        live_text += word + " "
        output_placeholder.markdown(
            f'<div class="glass-output-card">{live_text}</div>',
            unsafe_allow_html=True,
        )
        time.sleep(0.02)  # Typing speed (adjust kar sakte hain)