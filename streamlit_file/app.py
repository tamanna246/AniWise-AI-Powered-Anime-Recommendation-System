import streamlit as st
from recommender import recommend_anime, get_anime_details
st.set_page_config(
    page_title="AniWise",
    page_icon="🎌",
    layout="wide"
)

st.title("🎌 AniWise")
with st.sidebar:

    st.header("📖 About AniWise")

    st.write("""
AniWise recommends similar anime based on:

- 🎭 Genres
- 🎬 Themes
- 👥 Demographics
- 🏢 Studios

Algorithm:
- TF-IDF
- MultiLabelBinarizer
- KNN (Cosine Distance)
    """)

    st.divider()

    st.metric(
        "Anime Database",
        "28,491"
    )

    st.metric(
        "Recommendation Model",
        "KNN"
    )

st.markdown("""
### AI-Powered Anime Recommendation System

Find anime similar to your favourite shows using a **Content-Based Recommendation System**
built with **TF-IDF**, **MultiLabelBinarizer**, and **K-Nearest Neighbors (KNN)**.
""")

st.divider()

anime_name = st.text_input(
    "Enter Anime Name",
    placeholder="Naruto"
)

top_n = st.slider(
    "Number of Recommendations",
    1,
    10,
    5
)

if st.button(
    "🎯 Get Recommendations",
    use_container_width=True
):

    if anime_name.strip() == "":
        st.warning("Please enter an anime name.")

    else:
        details = get_anime_details(anime_name)
        if details:
             st.success("Anime Found!")
             st.subheader(details["Title"])
             col1, col2 = st.columns(2)
             with col1:
                 st.write(f"⭐ **Score:** {details['Score']}")
                 st.write(f"📺 **Type:** {details['Type']}")
             with col2:
                 st.write(f"🏢 **Studio:** {details['Studio']}")
                 st.write(f"🎭 **Genres:** {details['Genres']}")
             st.link_button(
                "🔗 View on MyAnimeList",
                details["URL"]
            )
        st.markdown("---")
        with st.spinner("🔍 Finding similar anime..."):
            result = recommend_anime(anime_name, top_n)
        st.success(f"Found Top {top_n} Recommendations!")
        st.subheader("🎯 Recommended Anime")
        st.dataframe(
            result,
            hide_index=True,
            use_container_width=True
        )
st.divider()

st.caption(
    "🎌 AniWise • AI-Powered Anime Recommendation System | Built with ❤️ using Python, Scikit-Learn & Streamlit"
)