class MyHashSet:

    def __init__(self):
        self._data = set();

    def add(self, key: int) -> None:
        self._data.add(key)

    def remove(self, key: int) -> None:
        if key not in self._data:
            return

        self._data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._data


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)