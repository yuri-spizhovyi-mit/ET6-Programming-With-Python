transactions = ["TXN001", "TXN002", "TXN003", "TXN003"]
# Step 1: Create an empty set to track seen transaction
seen = set()

# Step 2: Create another set to store duplicates
duplicates = set()

# Step 3: Iterate through the transactions
for transaction in transactions:
    if transaction in seen:
        duplicates.add(transaction)
    else:
        seen.add(transaction)

# Step 4: Display the duplicates
print("Duplicate transactions: ", duplicates)
