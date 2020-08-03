class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # set capacity attribute
        self.capacity = capacity
        
        # if capacity attribute is less than MIN
        if self.capacity < MIN_CAPACITY:
            # set capacity attribute equal to the MIN
            self.capacity = MIN_CAPACITY

        # set the storage space as nothing multiplied by the entire capacity
        self.storage = [None] * self.capacity
        # instantiate count attribute
        self.count = 0
        # instantiate loadfactor attribute
        self.loadfactor = self.count / self.capacity
        




    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # return capacity attribute
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # return loadfactor attribute
        return self.loadfactor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # encoding the key
        key = key.encode()

        # hash value equals
        hash = 14695981039346656037
        # loop over the elements in the key
        for i in key:
            # hash equals
            hash = (hash * 1099511628211) ^ i
        # return specific hash value
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # encode the 
        key = key.encode()

        # hash value equals
        hash = 5381
        # loop over the elements in the key
        for i in key:
            # hash equals
            hash = ((hash << 5) + hash) + i
        # return specific hash value
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # add to count for each addition
        self.count += 1
        # index equals the hash_index with that specific key
        index = self.hash_index(key)
        # set the node equal to the storage place with that index
        node = self.storage[index]
        # set the prev value as None
        prev = None
        # while the node is not None and the key != an existing key
        while node is not None and node.key != key:
            # set the prev as the node
            prev = node
            # set the node as the current (prev.next)
            node = prev.next
        # if the node is not None
        if node is not None:
            # set the node value equal to the value parameter
            node.value = value
        # else
        else:
            # create a new entry with the specified key and value
            new = HashTableEntry(key, value)
            # let the next node after the new one equal the specified storage index
            new.next = self.storage[index]
            # set the storage index as the new entry
            self.storage[index] = new


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # index equals the hash_index with that specific key
        index = self.hash_index(key)
        # set the node equal to the storage place with that index
        node = self.storage[index]
        # set the prev value as None
        prev = None
        
        # while the node is not None and the key != an existing key
        while node is not None and node.key != key:
            # set the prev as the node
            prev = node
            # set the node as the current (prev.next)
            node = prev.next
        # if the node is None
        if node is None:
            # return None
            return None
        # else
        else:
            # subtract from count
            self.count -= 1
            # if there is no prev value
            if prev is None:
                # set the current storage index as the next one
                self.storage[index] = node.next
            # else
            else:
                # set the current as the next node as a replacement
                prev.next = node.next
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index equals the hash_index with that specific key
        index = self.hash_index(key)
        # set the node equal to the storage place with that index
        node = self.storage[index]
        # while the node is not None and the key != an existing key
        while node is not None and node.key != key:
            # set the node equal to the next one
            node = node.next
        # if the node is None
        if node is None:
            # return None
            return None
        # else
        else:
            # return the node value
            return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # if the loadfactor is greater than 0.7
        if self.get_load_factor() > 0.7:
            # instantiate tracker variable equal to the current storage
            old_storage = self.storage
            # set the capacity attribute equal to the new_capacity param
            self.capacity = new_capacity
            # self.storage now equals the capacity attribute multiples by None
            # to get the correct amount of spaces 
            self.storage = [None] * self.capacity
            # set the node equal to nothing
            node = None
            # loop over the element in the old_storage variable
            for i in old_storage:
                # set the node equal to the element
                node = i
                # while the node is not None
                while node is not None:
                    # put (or insert) the specific node.key, node.value
                    self.put(node.key, node.value)
                    # set the node equal to the next to move forward in the list
                    node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
