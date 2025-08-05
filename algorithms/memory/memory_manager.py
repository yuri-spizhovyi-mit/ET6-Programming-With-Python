class MemoryManager:
    def __init__(self, memory_blocks: list[int]):
        self.initial_blocks = memory_blocks.copy()
        self.reset()

    def reset(self):
        self.blocks = self.initial_blocks.copy()
        self.last_index = 0  # For next-fit

    def first_fit(self, size: int) -> int:
        for i, block in enumerate(self.blocks):
            if block >= size:
                self.blocks[i] -= size
                return i
        return -1

    def next_fit(self, size: int) -> int:
        pass

    def best_fit(self, size: int) -> int:
        pass

    def worst_fit(self, size: int) -> int:
        pass

    def deallocate(self, index: int, size: int):
        """Simulate deallocation by adding free space back"""
        self.blocks[index] += size

    def deallocate(self, index: int, size: int):
        """Simulate deallocation by adding free space back"""
        pass


if __name__ == "__main__":
    mm = MemoryManager([100, 500, 200, 300, 600])

    print("First-Fit Allocations:")
    print(mm.first_fit(120))  # Expected index 1
    print(mm.first_fit(50))  # Expected index 0
    print(mm.first_fit(600))  # Expected index 4
    print(mm.blocks)  # Show remaining sizes
