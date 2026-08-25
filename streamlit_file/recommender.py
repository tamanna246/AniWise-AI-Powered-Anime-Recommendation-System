import ast
import joblib
import pandas as pd
from scipy.sparse import load_npz

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv("anime.csv")

# Convert string lists back to Python lists
list_columns = [
    "genres",
    "themes",
    "demographics",
    "studios"
]

for col in list_columns:
    if col in df.columns:
        df[col] = df[col].apply(
            lambda x: ast.literal_eval(x)
            if isinstance(x, str)
            else []
        )

# =====================================================
# Load Saved Model
# =====================================================

knn_model = joblib.load("knn_model.pkl")
final_matrix = load_npz("final_matrix.npz")

# =====================================================
# Recommendation Function
# =====================================================
# =====================================================
# English Title Aliases
# =====================================================

english_alias = {

    "attack on titan": "shingeki no kyojin",
    "aot": "shingeki no kyojin",

    "demon slayer": "kimetsu no yaiba",

    "jjk": "jujutsu kaisen",

    "my hero academia": "boku no hero academia",

    "fmab": "fullmetal alchemist: brotherhood",

    "konosuba": "kono subarashii sekai ni shukufuku wo!",

    "oshi no ko": "oshi no ko",

    "spy x family": "spy x family",

    "one punch man": "one punch man",

    "tokyo ghoul": "tokyo ghoul",

    "bleach": "bleach",

    "naruto shippuden": "naruto: shippuuden",

    "dragon ball super": "dragon ball super",

    "steins gate": "steins;gate",

    "code geass": "code geass: hangyaku no lelouch"

}

def recommend_anime(anime_name, top_n=5):

    anime_name = anime_name.lower().strip()
    anime_name = english_alias.get(
        anime_name,
        anime_name
    )

    # --------------------------------------------
    # Search Anime
    # --------------------------------------------

    matches = df[
        df["search_title"].str.contains(
            anime_name,
            case=False,
            na=False
        )
    ]

    if matches.empty:
        return pd.DataFrame({
            "Message": ["Anime not found."]
        })

    exact = matches[
        matches["search_title"] == anime_name
    ]

    if not exact.empty:
        selected_index = exact.index[0]
    else:
        selected_index = matches.index[0]

    selected_title = df.loc[selected_index, "title"]

    # --------------------------------------------
    # Find Neighbours
    # --------------------------------------------

    distances, indices = knn_model.kneighbors(
        final_matrix[selected_index],
        n_neighbors=50
    )

    recommendations = []

    used_titles = set()

    franchise = (
        selected_title
        .split(":")[0]
        .split("-")[0]
        .strip()
        .lower()
    )

    for distance, idx in zip(distances[0], indices[0]):

        if idx == selected_index:
            continue

        anime = df.iloc[idx]

        title = anime["title"].strip()

        if title.lower().startswith(franchise):
            continue

        if title in used_titles:
            continue

        anime_type = str(anime["type"]).upper()

        if anime_type in ["PV", "CM", "MUSIC"]:
            continue

        score = anime["score"]

        if pd.notna(score):

            if score < 6.5:
                continue

        similarity = round((1 - distance) * 100, 2)

        recommendations.append({

            "Title": title,

            "Similarity (%)": similarity,

            "Genres": ", ".join(anime["genres"]).title(),

            "Studio": ", ".join(anime["studios"]).title(),

            "Type": anime_type,

            "Score": round(score, 2)
            if pd.notna(score)
            else "N/A",

            "URL": anime["url"]

        })

        used_titles.add(title)

        if len(recommendations) == top_n:
            break

    result = pd.DataFrame(recommendations)

    return result.reset_index(drop=True)


def get_anime_details(anime_name):

    anime_name = anime_name.lower().strip()
    anime_name = english_alias.get(
        anime_name,
        anime_name
    )

    matches = df[
        df["search_title"].str.contains(
            anime_name,
            na=False
        )
    ]

    if matches.empty:
        return None

    exact = matches[
        matches["search_title"] == anime_name
    ]

    if not exact.empty:
        row = exact.iloc[0]
    else:
        row = matches.iloc[0]

    return {
        "Title": row["title"],
        "Genres": ", ".join(row["genres"]).title(),
        "Studio": ", ".join(row["studios"]).title(),
        "Type": row["type"].upper(),
        "Score": round(row["score"],2) if pd.notna(row["score"]) else "N/A",
        "URL": row["url"]
    }

    