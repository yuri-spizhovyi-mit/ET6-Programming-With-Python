"""Dice Roll Probability
Model rolling a dice and finding the probability of even numbers"""
sample_space = {1, 2, 3, 4, 5, 6}
even_numbers = {2, 4, 6}
probability = len(even_numbers)/ len(sample_space)
print("Probability of rolling an even number: ", probability)
