import streamlit as st


# Global css

st.markdown("""
    <style>
        .css-1dp5vir {
            background-image: None;
        }
        
        .e1nzilvr2 {
            display: inline-block;
        }
            
        .page-link {
            text-decoration: underline !important;
        }
        
    
        .block-container {
            max-width: 70%;
            margin-left: auto;
            margin-right: auto;
        }
            
        a {
            text-decoration: none !important;
            color: inherit !important;

            user-select: none;
            -webkit-user-drag: none;
        }
        
        .twitter-icon {
            color: #1DA1F2 !important;
            text-decoration: none;
        }
            
        .icon {
            color: black;
            text-decoration: none;
        }
    </style>
    """, unsafe_allow_html=True)


# Title and Introduction
st.markdown("""
<h1>Hey, I'm Winnie 👋</h1> 

<div style="display:inline-block; color: gray;">
    <span style="font-size: medium">Connect with me</span>
    <span>  </span>
    <a classname="twitter-icon" href="https://twitter.com/winnieh_c" target="_blank">
        <i class="fab fa-twitter" style="font-size: 24px;"></i>
    </a>
    <span>  </span>
    <a classname="icon" href="https://github.com/winnie9197" target="_blank">
        <i class="fab fa-github" style="font-size: 24px;"></i>
    </a>
    <span style="margin-right: 40px;">  </span>
    # <a classname="page-link">Moodboard</a>
</div>
""", unsafe_allow_html=True)

st.write("""
Hello there! I'm Winnie, a passionate software creator who loves showcasing my work on Twitter.
I hope you enjoy the demos I've put together on this site!
""")
         


# Using HTML for prettier social media links
st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">""", unsafe_allow_html=True)



# Demo Card Section (Two-Column Layout)
col1, col2 = st.columns(2)

# Tweet embed
# def generate_iframe(tweet_embed_code, width="100%", height="600"):
#     iframe_code = f"""
#     <iframe srcdoc='{tweet_embed_code}' width='{width}' height='{height}' style='border:none; overflow: hidden;'></iframe>
#     """
#     return iframe_code

# Organizing tweets in a two-dimensional list:
tweets_grid = [
    [
        # tweet 1
        """<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Since the official web browsing is no longer available... <br><br>I made a search-based visualization widget with <a href="https://twitter.com/streamlit?ref_src=twsrc%5Etfw">@streamlit</a>😶 <a href="https://t.co/mdCeSlWDyS">pic.twitter.com/mdCeSlWDyS</a></p>&mdash; Winnie Yeung (@winnieh_c) <a href="https://twitter.com/winnieh_c/status/1690516170640957441?ref_src=twsrc%5Etfw">August 13, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>""",
        
        # tweet 2
        """<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Streamlining React + <a href="https://twitter.com/tailwindcss?ref_src=twsrc%5Etfw">@tailwindcss</a> with GPT: modular code files for easier export <br><br>1/2 <a href="https://t.co/X0B134tMMt">pic.twitter.com/X0B134tMMt</a></p>&mdash; Winnie Yeung (@winnieh_c) <a href="https://twitter.com/winnieh_c/status/1692378103861887333?ref_src=twsrc%5Etfw">August 18, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>"""
    ],
#     # [
#     #     """
#     #     <!-- Embed code for Tweet 3 goes here -->
#     #     """,
#     #     """
#     #     <!-- Embed code for Tweet 4 goes here -->
#     #     """
#     # ],
#     # # Add more rows of tweets as needed...
]

youtube_links = ['https://youtu.be/Vad1kO2FKoE',
    'https://youtu.be/CGaK1NqG2Oc']

descriptions = ['[Bing Search Visualizer](#BingSearchVisualizer)', '[React + Tailwind Coder](#ReactTailwindCoder)']
for row in tweets_grid:
    cols = st.columns(len(row))
    for i, tweet_embed in enumerate(row):
        with cols[i]:
            st.video(youtube_links[i])
            # st.markdown(generate_iframe(tweet_embed), unsafe_allow_html=True)
            st.caption(descriptions[i])


# Additional Sections can be added here.
