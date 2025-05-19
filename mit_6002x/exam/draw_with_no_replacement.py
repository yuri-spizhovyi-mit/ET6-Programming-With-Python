import random


def draw_three_balls():
    """Simulate drawing 3 balls without replacement from a basket with 4R and 4G."""
    basket = ["R", "R", "R", "R", "G", "G", "G", "G"]
    random.shuffle(basket)
    result = "".join(basket[:3])
    return result


def drawing_without_replacement_sim(numTrials):
    """Estimate probability of drawing 3 same-color balls in many trials."""
    num_same_color = 0
    for _ in range(numTrials):
        result = draw_three_balls()
        if result == "RRR" or result == "GGG":
            num_same_color += 1
    return num_same_color / numTrials


# Example usage
print(draw_three_balls())
print("Probability of RRR or GGG:", drawing_without_replacement_sim(1000))
