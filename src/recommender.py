import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union


@dataclass
class Song:
    """Represents a song and its attributes."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """OOP implementation of the recommendation logic."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: Union[UserProfile, Dict], k: int = 5) -> List[Song]:
        """Return the top-scoring songs for a user profile."""
        scored_songs = []
        for song in self.songs:
            score, _ = score_song(user, _song_to_dict(song))
            scored_songs.append((score, song))
        scored_songs.sort(key=lambda item: (-item[0], item[1].id))
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: Union[UserProfile, Dict], song: Song) -> str:
        """Create a simple explanation for why a song was recommended."""
        score, reasons = score_song(user, _song_to_dict(song))
        return "; ".join(reasons) if reasons else f"Score {score:.2f}"


def _song_to_dict(song: Song) -> Dict[str, object]:
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }


def _normalize_user(user_prefs: Union[UserProfile, Dict]) -> Dict[str, object]:
    if isinstance(user_prefs, UserProfile):
        return {
            "genre": user_prefs.favorite_genre,
            "mood": user_prefs.favorite_mood,
            "energy": user_prefs.target_energy,
            "likes_acoustic": user_prefs.likes_acoustic,
        }
    if isinstance(user_prefs, dict):
        return {
            "genre": user_prefs.get("genre"),
            "mood": user_prefs.get("mood"),
            "energy": user_prefs.get("energy", 0.5),
            "likes_acoustic": user_prefs.get("likes_acoustic", False),
        }
    raise TypeError("user_prefs must be a UserProfile or dictionary")


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries with numeric values parsed."""
    with open(csv_path, newline="", encoding="utf-8") as handle:
        songs = []
        for row in csv.DictReader(handle):
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def score_song(user_prefs: Union[UserProfile, Dict], song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against a user's preferences and return a score plus reasons."""
    prefs = _normalize_user(user_prefs)
    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")
    else:
        reasons.append(f"genre mismatch (expected {prefs.get('genre')})")

    if song.get("mood") == prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")
    else:
        reasons.append(f"mood mismatch (expected {prefs.get('mood')})")

    target_energy = float(prefs.get("energy", 0.5))
    energy_gap = abs(float(song.get("energy", 0.0)) - target_energy)
    energy_similarity = max(0.0, 1.0 - energy_gap)
    energy_bonus = round(energy_similarity * 1.5, 2)
    score += energy_bonus
    reasons.append(f"energy closeness (+{energy_bonus:.2f})")

    target_valence = float(prefs.get("valence", 0.5))
    valence_gap = abs(float(song.get("valence", 0.0)) - target_valence)
    valence_similarity = max(0.0, 1.0 - valence_gap)
    valence_bonus = round(valence_similarity * 0.75, 2)
    score += valence_bonus
    reasons.append(f"valence similarity (+{valence_bonus:.2f})")

    if bool(prefs.get("likes_acoustic", False)):
        acoustic_bonus = 0.5 if float(song.get("acousticness", 0.0)) >= 0.7 else 0.0
        score += acoustic_bonus
        if acoustic_bonus:
            reasons.append("acoustic preference (+0.50)")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Union[UserProfile, Dict], songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by relevance and return the top-k results with scores and explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: (-item[1], item[0]["id"]))
    return scored_songs[:k]
