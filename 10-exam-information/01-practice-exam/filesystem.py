# Enter your code here:
from abc import ABC, abstractmethod, abstractproperty
import re


class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__available_blocks = {n for n in range(0, block_count)}
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_blocks(self):
        return self.__available_blocks

    @property
    def used_block_count(self):
        return len(self.__used_blocks)

    @property
    def total_block_count(self):
        return len(self.__available_blocks) + len(self.__used_blocks)

    @property
    def block_size(self):
        return self.__block_size

    def allocate(self, block_count):  # GIVES AMOUNT OF BLOCKS, NOT WHICH BLOCKS
        # takes block_count from available blocks starting from start of list,
        # puts them in used_blocks
        if block_count > len(self.__available_blocks):
            raise RuntimeError("Block count cannot be greater than available blocks")

        result = []
        available_blocks = sorted(list(self.__available_blocks))

        for _ in range(block_count): # do everything as a sorted list, then overwrite set with list
            # for x amount of blocks, take amount of available_blocks
            block = available_blocks[0]
            result.append(block)
            available_blocks.remove(block)
            self.__used_blocks.add(block)
        self.__available_blocks = set(available_blocks)

        return result

    def free(self, blocks): # PASS WHICH BLOCKS NOT AMOUNT
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError("Block is not in use")

        for block in blocks:
            self.__available_blocks.add(block)
            self.__used_blocks.remove(block)


class Entity(ABC):
    @staticmethod
    def is_valid_name(value):
        return re.fullmatch(r'[a-zA-Z\d.]{1,16}', value)

    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError("Name is not valid")

        self.name = name
        self.storage = storage

        @property
        def name(self):
            return self.__name

        @property
        def storage(self):
            return self.__storage

        @name.setter
        def name(self, value):
            if self.is_valid_name(value):
                self.__name = value
            else:
                raise RuntimeError("Name must be a valid name")

        @property
        @abstractmethod
        def size_in_blocks():
            ...

        @property
        def size_in_bytes(self):
            return self.size_in_blocks() * self.__storage.block_size

        @abstractmethod
        def clear():
            ...


class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.blocks = []

    def grow(self, block_count):
        self.blocks += self.storage.allocate(block_count)

    @property
    def size_in_blocks(self):
        return self.blocks

    def clear(self):
        self.storage.free(self.blocks)
        self.blocks.clear()

class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.children = []

    def add(self, entity):
        self.children.append(entity)

    @property
    def size_in_blocks(self):
        return sum(child.size_in_blocks for child in self.children)



# testing ground
device = StorageDevice(9, 20)
file = File(device, "test.txt")
dir = Directory(device, "dir")

# prints for device
print(
    f"Available blocks: {device.available_blocks}, used blocks: {device.used_block_count}, total blocks: {device.total_block_count}")
print(f"Allocate 3: {device.allocate(3)}")
print(
    f"Available blocks: {device.available_blocks}, used blocks: {device.used_block_count}, total blocks: {device.total_block_count}")
print("Free 3")
device.free([0, 1, 2])
print(
    f"Available blocks: {device.available_blocks}, used blocks: {device.used_block_count}, total blocks: {device.total_block_count}")

# prints for file
print("FILE PRINTING ----------------------------")
print(f"Storage: {file.storage}, Name: {file.name}, Size: {file.size_in_blocks}")
print(
    f"Available blocks: {device.available_blocks}, used blocks: {device.used_block_count}, total blocks: {device.total_block_count}")

print("Grow 7")
file.grow(7)
print(f"Storage: {file.storage}, Name: {file.name}, Size: {file.size_in_blocks}")
print(
    f"Available blocks: {device.available_blocks}, used blocks: {device.used_block_count}, total blocks: {device.total_block_count}")

print("Free")
file.clear()
print(f"Storage: {file.storage}, Name: {file.name}, Size: {file.size_in_blocks}")
print(
    f"Available blocks: {device.available_blocks}, used blocks: {device.used_block_count}, total blocks: {device.total_block_count}")

# DIRECTORY TESTING
dir.add(file)
print(f"Dir name: {dir.name} Children: {dir.children}")

