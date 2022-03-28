# new hash table class
# init takes size and create list of lists (buckets) based on that size
# 3 major fns: set, get, delete, str

# SET - get bucket index, by hashing key modulo size
# get the bucket, iterate through and check if the provided key matches
# if value exists, replace index of bucket with key, value tuple
# else, append to bucket

# GET - get bucket index, by hashing key modulo size
# get the bucket, iterate through and check if the provided key matches
# if value exists, return value, else raise key error

# DELETE - get bucket index, by hashing key modulo size
# get the bucket, iterate through and check if the provided key matches
# if value exists, save index, pop from bucket
from typing import Union, Any


class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _get_bucket(self, key) -> list[tuple[Union[str, int], Any]]:
        bucket_index = hash(key) % self.size
        return self.buckets[bucket_index]

    def get(self, key: Union[str, int]) -> Any:
        bucket = self._get_bucket(key)

        for index, ele in enumerate(bucket):
            ele_key, ele_val = ele

            if ele_key == key:
                return ele_val

        raise KeyError("Key not found")

    def set(self, key: Union[str, int], val: Any) -> None:
        bucket = self._get_bucket(key)

        found_index = None

        for index, ele in enumerate(bucket):
            ele_key, _ = ele

            if ele_key == key:
                found_index = index
                break

        if found_index is not None:
            bucket[found_index] = (key, val)
        else:
            bucket.append((key, val))

    def delete(self, key: Union[str, int]) -> None:
        bucket = self._get_bucket(key)

        found_index = None

        for index, ele in enumerate(bucket):
            ele_key, ele_val = ele

            if ele_key == key:
                found_index = index
                break

        print('found index', found_index)

        if found_index is not None:
            bucket.pop(found_index)

    def __str__(self) -> str:
        return "".join(str(bucket) for bucket in self.buckets if bucket)


new_table = HashTable(20)

new_table.set('konrad', 'droeske')
new_table.set('nancy', 'chen')

print(new_table)

print(new_table.get('konrad'))

new_table.delete('nancy')

print(new_table)
