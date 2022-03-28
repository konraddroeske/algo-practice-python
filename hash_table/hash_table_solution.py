from typing import Any, Union


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # insert values into hash map
    def set_val(self, key: Union[str, int], val: Any):
        # get the index from the key using the hash function
        hashed_key = hash(key) % self.size

        # get the bucket corresponding to the index
        bucket = self.hash_table[hashed_key]

        found_key = False
        found_index = None

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_index = index
                found_key = True
                break

        # if the bucket has the same key to be inserted, update the key value
        # otherwise, append the new key value pair to the bucket
        if found_key and found_index is not None:
            bucket[found_index] = (key, val)
        else:
            bucket.append((key, val))

    # return searched value with specific key
    def get_val(self, key):
        # get index from the key using the hash function
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        found_record = None

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_record = record_val
                found_key = True
                break

        if found_key:
            return found_record
        else:
            raise KeyError("No record found")

    def delete_val(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        found_index = None

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                found_index = index
                break

        if found_key:
            bucket.pop(found_index)

        return

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(20)

hash_table.set_val('kdroeske@gmail.com', 'some value')
print(hash_table)
print()

hash_table.set_val('nancy@gmail.com', 'another value')
print(hash_table)
print()

print(hash_table.get_val('kdroeske@gmail.com'))
print()

hash_table.delete_val('nancy@gmail.com')
print(hash_table)
