# Interview-Prep-Toolkit/trie.py

class TrieNode:
    """
    Node component for the Trie (Prefix Tree).
    Each node contains a dictionary of children nodes and a boolean flag
    indicating if it marks the end of a complete valid word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Prefix Tree implementation supporting O(m) insertions, searches,
    and prefix matching (where m is the length of the word).
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie in O(m) time."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie (exact match), else False."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any previously inserted word that has the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Verification & Testing
if __name__ == "__main__":
    print("Trie (Prefix Tree) Demo")

    trie = Trie()

    # Insert words
    words_to_insert = ["interview", "intern", "internet", "computer", "code"]
    for w in words_to_insert:
        trie.insert(w)
        print(f"Inserted: '{w}'")

    print("\nRunning Searches")
    print(f"Search 'intern' (Expect True): {trie.search('intern')}")
    print(f"Search 'inter' (Expect False - valid prefix, but not a full word): {trie.search('inter')}")
    print(f"Starts with prefix 'inter' (Expect True): {trie.starts_with('inter')}")
    print(f"Starts with prefix 'comp' (Expect True): {trie.starts_with('comp')}")
    print(f"Search 'science' (Expect False): {trie.search('science')}")

    print("\nTrie verification completed successfully.")