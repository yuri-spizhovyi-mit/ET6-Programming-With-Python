from matplotlib_venn import venn2

players_match_first = {"John", "Bob", "Edward", "George"}
players_match_second = {"Alice", "Bob", "George", "Evan"}

venn2([players_match_first, players_match_second], ("Match 1", "Match 2"))


from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Define the player lists for Match 1 and Match 2
match_1_players = {"Alice", "Bob", "Charlie", "David"}
match_2_players = {"Charlie", "David", "Eve", "Frank"}

# Find players who participated in both matches
consistent_players = match_1_players & match_2_players

# Create the Venn diagram
venn = venn2([match_1_players, match_2_players], ("Match 1", "Match 2"))

# Customize labels
venn.get_label_by_id("10").set_text(
    "\n".join(match_1_players - match_2_players)
)  # Only Match 1
venn.get_label_by_id("01").set_text(
    "\n".join(match_2_players - match_1_players)
)  # Only Match 2
venn.get_label_by_id("11").set_text("\n".join(consistent_players))  # Both matches

# Display the Venn diagram
plt.title("Players Participation in Matches")
plt.show()
