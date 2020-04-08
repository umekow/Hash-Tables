# '''
# Linked List hash table key/value pair
# '''
import warnings


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"({self.key}, {self.value})"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) ** i) % self.capacity
        return hash

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """

        address = self._hash(key)

        if self.storage[address]:

            warnings.warn("Hash collision")
            # start at the first node
            current = self.storage[address]
            # keep track of previous node
            prev = None

            # while current: handles if
            while current:
                # check to see if the current.key = key
                if current.key == key:
                    # if true:  current.value = value
                    current.value = value
                    return
                # move to next node
                prev = current
                current = current.next

            # if we have reached the end of list: add to end of list
            prev.next = LinkedPair(key, value)

        else:
            self.storage[address] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        # create address for key
        address = self._hash(key)

        # go to first node located at that address
        current = self.storage[address]

        # keep track of previous node
        prev = None

        # if there is a node and that node's key is the key we are looking for
        if current is not None and current.key == key:

            # replace the head with the next node
            self.storage[address] = current.next
            return

        # while there is a node and the node's key is not the key we are trying to remove go to the next until we find correct node
        while current is not None and current.key != key:

            # current node becomes previous
            prev = current

            # current node is the next node
            current = current.next

        # replace the node with the next node
        prev.next = current.next

        # return not found
        if current is None:
            warnings.warn("Key is not found")

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        address = self._hash(key)

        current = self.storage[address]

        # linked list
        # if current is not none and its key is not the key we are looking for ,iterate through linked list until found
        while current is not None and current.key != key:
            current = current.next

        # if current is not None
        if current:
            return current.value

        # reached the end of list and key has not been found
        else:
            return None

        # arrays
        # if len(current):
        #     return current[1]
        #     # for i in range(len(self.storage)):
        #     #     if current[i][0] == key:
        #     #         return current[i][1]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """

        # double the capacity
        self.capacity *= 2

        # store self.storage in new variable
        old_storage = self.storage

        # replace storage with new array that has the right lenght
        self.storage = [None] * self.capacity

        current = None
        # for each element in old_storage
        for i in old_storage:
            # insert linked list into self storage :
            if i is not None:
                current = i
                # while there is another node
                while current is not None:
                    # insert the node into hashtable
                    self.insert(current.key, current.value)

                    # move to next node
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
