import re

def tokenize_words(text):
    """
    Matnni so‘zlarga bo‘ladi.
    """
    return re.findall(r'\b\w+\b', text.lower())

def tokenize_sentences(text):
    """
    Matnni gaplarga bo‘ladi.
    """
    return re.split(r'[.!?]+\s*', text.strip())
