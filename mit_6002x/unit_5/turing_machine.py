import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Define a very simple Turing machine that increments a binary number (e.g. 011 -> 100)
# Tape symbols: 0, 1, B (blank)
# States: q0 (read), q1 (carry), HALT


# Simulate one step at a time
class TuringMachine:
    def __init__(self, tape, initial_state="q0"):
        self.tape = list(tape)
        self.head = len(tape) - 1  # Start at the rightmost digit
        self.state = initial_state
        self.steps = [list(tape)]  # Record each tape state

    def step(self):
        if self.state == "HALT":
            return False

        symbol = self.tape[self.head]

        if self.state == "q0":
            if symbol == "1":
                self.tape[self.head] = "0"
                self.state = "q0"
                self.head -= 1
            elif symbol == "0":
                self.tape[self.head] = "1"
                self.state = "HALT"
            elif symbol == "B":
                self.tape[self.head] = "1"
                self.state = "HALT"

        if self.head < 0:
            self.tape.insert(0, "B")
            self.head = 0

        self.steps.append(list(self.tape))
        return True


# Initialize machine with binary number: 011 (7 in binary)
initial_tape = ["0", "1", "1"]
tm = TuringMachine(initial_tape)

# Run steps until halt
while tm.step():
    continue

# Create animation
fig, ax = plt.subplots(figsize=(8, 2))
plt.axis("off")
boxes = []


def init():
    ax.clear()
    ax.set_xlim(0, len(tm.steps[-1]))
    ax.set_ylim(0, 1)
    return boxes


def update(frame):
    ax.clear()
    ax.set_xlim(0, len(tm.steps[-1]))
    ax.set_ylim(0, 1)
    ax.axis("off")
    current_tape = tm.steps[frame]
    for i, symbol in enumerate(current_tape):
        rect = patches.Rectangle((i, 0), 1, 1, edgecolor="black", facecolor="white")
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, symbol, ha="center", va="center", fontsize=16)
    return boxes


ani = FuncAnimation(
    fig, update, frames=len(tm.steps), init_func=init, blit=False, repeat=False
)
# Prevent garbage collection by assigning to a persistent variable
animation_ref = ani
# Now show the animation
plt.show()
