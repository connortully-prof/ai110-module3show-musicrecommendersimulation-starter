"""Command line runner for the Music Recommender Simulation."""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        ("Happy pop", {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False}),
        ("Chill lofi", {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True}),
        ("Intense rock", {"genre": "rock", "mood": "intense", "energy": 0.9, "likes_acoustic": False}),
    ]

    for name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{name} profile:\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
