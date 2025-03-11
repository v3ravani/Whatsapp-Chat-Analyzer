import re
import json
from datetime import datetime, timedelta
from collections import Counter
import emoji
from textblob import TextBlob
import nltk
from nltk.util import ngrams
import random
nltk.download('punkt')


def parse_chat(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    chat_data = []
    message_pattern = re.compile(r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}\s?[APM]{2}) - ([^:]+?): (.+)")
    
    for line in lines:
        line = line.replace("\u202f", " ")
        match = message_pattern.match(line)
        if match:
            date_str, time_str, sender, message = match.groups()
            timestamp = datetime.strptime(date_str + ", " + time_str, "%m/%d/%y, %I:%M %p")
            chat_data.append({"timestamp": timestamp, "sender": sender, "message": message})
    
    return chat_data


def extract_words(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    stopwords = {"the", "is", "and", "to", "you", "a", "in", "for", "of", "on", "it", "this"}
    return [word for word in words if word not in stopwords]


def extract_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]


def extract_links(text):
    return re.findall(r'https?://\S+', text)


def analyze_chat(chat_data):
    word_counter = Counter()
    emoji_counter = Counter()
    user_word_count = {}
    user_emoji_count = {}
    message_counts = Counter()
    message_lengths = {}
    sentiment_scores = {}
    sarcasm_scores = {}
    link_counts = Counter()
    question_counts = Counter()
    ignored_messages = Counter()
    chat_energy = {}
    conversation_starters = Counter()
    user_phrases = {}

    previous_message = None
    for msg in chat_data:
        text = msg["message"]
        sender = msg["sender"]
        timestamp = msg["timestamp"]

        # Word Analysis
        words = extract_words(text)
        word_counter.update(words)
        user_word_count.setdefault(sender, Counter()).update(words)

        # Emoji Analysis
        emojis_found = extract_emojis(text)
        emoji_counter.update(emojis_found)
        user_emoji_count.setdefault(sender, Counter()).update(emojis_found)

        # Message Length
        message_lengths[sender] = max(message_lengths.get(sender, 0), len(text))

        # Sentiment Analysis
        polarity = TextBlob(text).sentiment.polarity
        sentiment_scores[sender] = sentiment_scores.get(sender, []) + [polarity]

        # Sarcasm Detection (Random for now)
        sarcasm_scores[sender] = sarcasm_scores.get(sender, []) + [random.uniform(0, 1)]

        # Links Shared
        links = extract_links(text)
        link_counts.update(links)

        # Questions Asked
        if "?" in text:
            question_counts[sender] += 1

        # Ignored Messages
        if previous_message and previous_message["sender"] != sender:
            ignored_messages[previous_message["sender"]] += 1
        previous_message = msg

        # Common Phrases
        tokenized_text = nltk.word_tokenize(text)
        bigrams = list(ngrams(tokenized_text, 2))
        user_phrases.setdefault(sender, Counter()).update([" ".join(bigram) for bigram in bigrams])

        # Message Count
        message_counts[sender] += 1

    avg_response_time = {user: sum(times)/len(times) if times else 0 for user, times in sarcasm_scores.items()}
    avg_daily_chat_time = str(timedelta(seconds=sum(message_lengths.values()) / len(chat_data) if chat_data else 0))
    sentiment_summary = {user: ((sum(scores)/len(scores) + 1) / 2) * 10 if scores else 5 for user, scores in sentiment_scores.items()}
    sarcasm_summary = {user: (sum(scores)/len(scores)) * 10 if scores else 0 for user, scores in sarcasm_scores.items()}
    chat_energy_score = {user: ((message_counts[user] + sentiment_summary[user] - sarcasm_summary[user]) / 2) for user in message_counts.keys()}

    print("\n📌 Top 10 words used:", word_counter.most_common(10))
    print("\n📌 Top 10 words per user:", {user: words.most_common(10) for user, words in user_word_count.items()})
    print("\n😊 Top 5 emojis per user:", {user: emojis.most_common(5) for user, emojis in user_emoji_count.items()})
    print("\n⏳ Average response time per user:", avg_response_time)
    print("\n📊 Total messages sent by each user:", message_counts)
    print("\n⌛ Average daily chatting time:", avg_daily_chat_time)
    print("\n📝 Longest message per user:", message_lengths)
    print("\n🔗 Most common links shared:", link_counts.most_common(5))
    print("\n🚀 Conversation starters:", conversation_starters)
    print("\n📈 Sentiment analysis per user:", sentiment_summary)
    print("\n🤖 Sarcasm scores (out of 10):", sarcasm_summary)
    print("\n🔥 Chat energy score (out of 10):", chat_energy_score)
    print("\n📌 Most common phrases per user:", {user: phrases.most_common(5) for user, phrases in user_phrases.items()})
    print("\n🚫 Most ignored messages:", ignored_messages)
    print("\n❓ Questions asked per user:", question_counts)

    return {
        "Top Words": word_counter.most_common(10),
        "Top 10 Words Per User": user_word_count,
        "Top 5 Emojis Per User": user_emoji_count,
        "Average Response Time": avg_response_time,
        "Total Messages Per User": message_counts,
        "Average Daily Chat Time": avg_daily_chat_time,
        "Longest Message Per User": message_lengths,
        "Most Common Links": link_counts.most_common(5),
        "Conversation Starters": conversation_starters,
        "Sentiment Analysis": sentiment_summary,
        "Sarcasm Scores": sarcasm_summary,
        "Chat Energy Score": chat_energy_score,
        "Most Common Phrases Per User": user_phrases,
        "Most Ignored Messages": ignored_messages,
        "Question Counts": question_counts
    }

chat_data = parse_chat("chat.txt")
analyze_chat(chat_data)