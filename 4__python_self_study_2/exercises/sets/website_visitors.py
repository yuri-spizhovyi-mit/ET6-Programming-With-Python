"""Website Visitors
Track unique visitors to a website over a week"""

daily_visitors = [
    {"Alice", "Bob", "Charlie"},
    {"Bob", "Charlie", "Dave"},
    {"Alice", "Eve", "Bob"},
]

unique_visitors = set()
for visitor in daily_visitors:
    unique_visitors = unique_visitors.union(visitor)

weekly_visitors = set.union(*daily_visitors)


print("Unique visitors: ", unique_visitors)
print("Weekly visitors: ", weekly_visitors)
