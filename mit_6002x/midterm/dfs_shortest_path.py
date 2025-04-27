def find_shortest_path(start, goal):
    def dfs(position, path, shortest):
        path = path + [position]

        if position == goal:
            return path

        if shortest is None or len(path) < len(shortest):
            for move in [-1, 1]:  # possible moves
                next_pos = position + move

                # Avoid negative numbers and avoid revisiting
                if next_pos >= 0 and next_pos not in path:
                    new_path = dfs(next_pos, path, shortest)
                    if new_path is not None:
                        shortest = new_path

        return shortest

    return dfs(start, [], None)


# Example usage:
print(find_shortest_path(0, 4))
