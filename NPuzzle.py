import sys
import heapq

class PuzzleState:
    def __init__(self, board, empty_pos, moves):
        self.board = board
        self.empty_pos = empty_pos
        self.size = int(len(board) ** 0.5)
        self.moves = moves
        self.goal = self.create_goal()

    def create_goal(self):
        return list(range(1, self.size * self.size)) + [0]

    def is_goal(self):
        return tuple(self.board) == tuple(self.goal)

    def get_neighbors(self):
        x, y = self.empty_pos
        directions = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1)
        }
        neighbors = []
        
        for direction, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                new_board = self.board[:]
                # Swap the empty tile with the adjacent tile
                new_board[x * self.size + y], new_board[new_x * self.size + new_y] = new_board[new_x * self.size + new_y], new_board[x * self.size + y]
                neighbors.append((new_board, (new_x, new_y), direction))
        
        return neighbors

def solve_puzzle(initial_board):
    empty_pos = initial_board.index(0)
    puzzle_state = PuzzleState(initial_board, (empty_pos // puzzle_state.size, empty_pos % puzzle_state.size), [])

    pq = []
    heapq.heappush(pq, (0, puzzle_state))
    visited = set()

    while pq:
        moves_count, current_state = heapq.heappop(pq)
        
        if current_state.is_goal():
            return current_state.moves
        
        visited.add(tuple(current_state.board))

        for neighbor_board, neighbor_empty_pos, move in current_state.get_neighbors():
            if tuple(neighbor_board) not in visited:
                new_moves = current_state.moves + [move]
                # Using Manhattan distance as heuristic
                priority = moves_count + 1 + sum(abs((val - 1) // current_state.size - i) + abs((val - 1) % current_state.size - j) 
                                                   for i, val in enumerate(neighbor_board) if val != 0)
                heapq.heappush(pq, (priority, PuzzleState(neighbor_board, neighbor_empty_pos, new_moves)))

    return []

def main():
    input_data = sys.stdin.read().strip().split()
    k = int(input_data[0])
    initial_board = list(map(int, input_data[1:]))
    
    moves = solve_puzzle(initial_board)
    
    print(len(moves))
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()
