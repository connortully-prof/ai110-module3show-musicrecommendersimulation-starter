# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This recommender is designed for classroom exploration and simple music recommendation demos. It suggests songs from a small catalog based on a user’s preferred genre, mood, energy level, and acoustic preference. It is best used as a transparent example of how a content-based recommender works rather than as a production-grade music service.

---

## 3. How the Model Works

The model uses a few easy-to-understand song features to estimate whether a track fits a user’s taste. It compares the song’s genre and mood to the user’s favorites, then checks whether the song’s energy and emotional tone are close to the target. If the user prefers acoustic songs, that can give the song a small extra boost. The highest-scoring songs are returned first.

---

## 4. Data

The dataset includes 10 songs with features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog is small, so the system only reflects the songs in this file. It also does not include listening history, lyrics, or artist popularity, which means it cannot capture the full complexity of real music taste.

---

## 5. Strengths

The system works well for simple cases where a user clearly prefers a certain genre and mood. It gives intuitive results for profiles like “happy pop” or “chill lofi,” and its scoring logic is easy to explain because each recommendation comes with a reason list that highlights the matching features.

---

## 6. Limitations and Bias

This system can over-prioritize obvious matches in genre and mood. Because the catalog is small and the data is hand-curated, it may reinforce narrow taste patterns and miss songs that are good matches in a less obvious way. It also does not capture social context or long-term listening behavior, so it can create a filter bubble around the features it already knows about.

---

## 7. Evaluation

I tested the recommender with several profiles, including happy pop, chill lofi, and intense rock. The recommendations changed in a sensible way when the user profile changed, which suggests the scoring logic is doing useful work. I also compared the top results against my own intuition and found that the system made sense for straightforward taste profiles, though it was less convincing for more mixed preferences.

---

## 8. Future Work

Future improvements could include adding more songs and more features such as artist similarity or playlist context. A more advanced version could also use learned weights instead of fixed scores and could add diversity controls so the top results do not all come from one genre or mood.

---

## 9. Personal Reflection

This project showed me that even a very simple recommender can feel surprisingly useful when the scoring rules are clear. I also learned that the strongest part of a recommender is often not the algorithm alone, but the quality of the data and the way the system is documented and tested.
