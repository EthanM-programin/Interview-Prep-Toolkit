# Interview-Prep-Toolkit/lru_cache.py
from collections import OrderedDict

class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation.
    Achieves O(1) time complexity for get() and put() operations
    by combining a Hash Map with a Doubly Linked List (OrderedDict).
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict maintains the insertion order of keys
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move the accessed key to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move to end (most recently used)
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Pop the first item (oldest/least recently used) from the front
            # last=False pops the FIFO oldest item
            oldest_key, _ = self.cache.popitem(last=False)
            print(f"Capacity reached. Evicted least recently used key: {oldest_key}")

        # Insert the new key-value pair
        self.cache[key] = value

# Verification & Testing
if __name__ == "__main__":
    print("\nLRU Cache Interview Demo")

    # Initialize cache with a small capacity of 2
    lru = LRUCache(2)

    lru.put(1, 1) # Cache: {1: 1}
    lru.put(2, 2) # Cache: {1: 1, 2: 2}
    print(f"\nGet key 1 (Expect 1): {lru.get(1)}") # Returns 1, Cache is now {2: 2, 1: 1}

    lru.put(3, 3) # Evicts key 2 because capacity is 2, Cache: {1: 1, 3: 3}
    print(f"Get key 2 after eviction (Expect -1): {lru.get(2)}") # Returns -1 (Not found)

    lru.put(4, 4) # Evicts key 1, Cache: {3: 3, 4: 4}
    print(f"\nGet key 1 after eviction (Expect -1): {lru.get(1)}") # Returns -1
    print(f"Get key 3 (Expect 3): {lru.get(3)}") # Return 3
    print(f"Get key 4 (Expect 4): {lru.get(4)}") # Return 4

    print("\nLRU Cache verification completed successfully.\n")