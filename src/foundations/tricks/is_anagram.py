from collections import Counter


def is_anagram(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)


print(f"taste and state is an anagram? {is_anagram("taste", "state")}")
print(f"york and kroy is an anagram? {is_anagram("york", "kroy")}")
print(f"trick and track is an anagram? {is_anagram("trick", "track")}")
