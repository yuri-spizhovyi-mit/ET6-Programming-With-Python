import matplotlib.pyplot as plt
# Step 1: Improve categorization based on new user input


# Update the categorize_work function
def better_categorize_work(row):
    comments = row["Comments"]
    work_process = row["Work Order Process"]

    # Treat "sandblast" and "media blast" as sandblasting
    if (
        "sandblast" in comments
        or "sandblast" in work_process
        or "media blast" in comments
        or "media blast" in work_process
    ):
        return "Sandblasting"
    # Treat "milling", "machining", "fabricate" as Machining
    elif any(word in comments for word in ["milling", "machining", "fabricate"]) or any(
        word in work_process for word in ["milling", "machining", "fabricate"]
    ):
        return "Machining"
    # Use Comments column info for other manual categories
    elif "drill" in comments:
        return "Drilling"
    elif "clean" in comments or "clean" in work_process:
        return "Cleaning"
    else:
        return "Other Work"


# Apply new categorization
df["Work Category"] = df.apply(better_categorize_work, axis=1)

# Step 2: Group hours again
category_hours = df.groupby("Work Category")["Hours"].sum().to_dict()

# Step 3: Add the missing 16 hours to Sandblasting
category_hours["Sandblasting"] = (
    category_hours.get("Sandblasting", 0) + adjustment_hours
)

# Step 4: Recalculate total hours
adjusted_total_hours = sum(category_hours.values())

# Step 5: Recalculate sandblasting percentage
adjusted_sandblast_hours = category_hours.get("Sandblasting", 0)
adjusted_sandblast_percentage = (adjusted_sandblast_hours / adjusted_total_hours) * 100

# Step 6: Create new pie chart
labels = list(category_hours.keys())
sizes = list(category_hours.values())

plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("Corrected Breakdown of Time Spent by Work Type")
plt.axis("equal")  # Equal aspect ratio ensures the pie is circular.

# Step 7: Create corrected summary
corrected_summary = {
    "Adjusted Total Hours Worked": adjusted_total_hours,
    "Adjusted Total Sandblasting Hours": adjusted_sandblast_hours,
    "Sandblasting % of Total Hours (Corrected)": adjusted_sandblast_percentage,
}

tools.display_dataframe_to_user(
    name="Final Corrected Sandblasting Time Analysis",
    dataframe=pd.DataFrame([corrected_summary]),
)

plt.show()
