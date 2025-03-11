import re
from collections import Counter
import emoji

def get_most_used_words(parsed_data, top_n=5):
    word_counts = Counter()
    for entry in parsed_data:
        words = re.findall(r'\b\w+\b', entry["message"].lower())  # Extract words
        word_counts.update(words)

    return word_counts.most_common(top_n)

def get_most_used_emojis(parsed_data, top_n=5):
    emoji_counts = Counter()
    for entry in parsed_data:
        emojis = [char for char in entry["message"] if char in emoji.UNICODE_EMOJI["en"]]
        emoji_counts.update(emojis)

    return emoji_counts.most_common(top_n)
