import os

def get_stopwords():
    """
    Stop-so‘zlar ro‘yxatini qaytaradi.
    """
    path = os.path.join(os.path.dirname(__file__), 'data', 'stopwords_uz.txt')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def remove_stopwords(tokens):
    """
    Tokenlardan stop-so‘zlarni olib tashlaydi.
    """
    stopwords = get_stopwords()
    return [t for t in tokens if t not in stopwords]
