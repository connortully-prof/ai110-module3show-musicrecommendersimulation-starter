# 🎵 Music Recommender Simulation

## Project Summary

This project builds a lightweight content-based recommender that suggests songs from a small catalog by matching a user profile to musical attributes such as genre, mood, energy, and emotional tone. The system is intentionally simple so it can show how raw data is transformed into recommendations and how those recommendations can reflect both taste and bias.

---

## How The System Works

Real music platforms use many signals to predict what a listener might enjoy next, including playlists, skips, likes, and audio features. In this version, the recommender uses a much smaller set of features that are easy to understand: genre, mood, energy, valence, and acousticness. Each song is scored against a user profile by rewarding close matches in genre and mood and by giving extra points when the song’s energy and emotional tone are near the target. The songs with the highest scores are returned as recommendations.

The core recipe is:
- +2.0 points for a genre match
- +1.0 point for a mood match
- +energy closeness points based on how near the song is to the target energy
- +valence similarity points for matching emotional mood
- +0.5 points for acoustic preference when the song is highly acoustic

The data flow is simple: Input user preferences → score each song in the catalog → rank the songs → return the top results.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the starter tests with:

```bash
pytest
```

---

## Sample Recommendation Output

Example output for a happy pop profile:

```text
Happy pop profile:

Sunrise City - Score: 4.47
Because: genre match (+2.0); mood match (+1.0); energy closeness (+1.47)

Gym Hero - Score: 3.47
Because: genre match (+2.0); mood mismatch (expected happy); energy closeness (+1.47)

Rooftop Lights - Score: 2.47
Because: genre mismatch (expected pop); mood match (+1.0); energy closeness (+1.47)
```

---

## Experiments I Tried

I tested the recommender with a few different user profiles to see whether the ranking felt intuitive. The system performs best when the user profile is clear and consistent, such as “happy pop” or “chill lofi.” I also noticed that genre, mood, and emotional tone all shape the rankings, which makes the output easy to explain but still somewhat narrow.

---

## Limitations and Risks

This recommender is intentionally simple and works best on a small catalog. It does not understand lyrics, artist history, or listening context, and it can over-prioritize obvious genre or mood matches. Because the system uses a small number of hand-picked features, it may miss songs that feel right for the user in a more subtle way.

---

## Reflection

The main lesson was that even simple scoring rules can create recommendations that feel meaningful. I also learned that recommender systems can appear thoughtful while still being biased toward the features they were given, which makes documentation and careful testing important.


