# Reuse getStats function to compute detailed evaluation metrics
def accuracy(true_pos, false_pos, true_neg, false_neg):
    return (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg)


def sensitivity(true_pos, false_neg):  # Recall
    try:
        return true_pos / (true_pos + false_neg)
    except ZeroDivisionError:
        return float("nan")


def specificity(true_neg, false_pos):
    try:
        return true_neg / (true_neg + false_pos)
    except ZeroDivisionError:
        return float("nan")


def pos_pred_val(true_pos, false_pos):  # Precision
    try:
        return true_pos / (true_pos + false_pos)
    except ZeroDivisionError:
        return float("nan")


def neg_pred_val(true_neg, false_neg):
    try:
        return true_neg / (true_neg + false_neg)
    except ZeroDivisionError:
        return float("nan")


def get_stats(true_pos, false_pos, true_neg, false_neg):
    return {
        "accuracy": round(accuracy(true_pos, false_pos, true_neg, false_neg), 3),
        "sensitivity (recall)": round(sensitivity(true_pos, false_neg), 3),
        "specificity": round(specificity(true_neg, false_pos), 3),
        "precision": round(pos_pred_val(true_pos, false_pos), 3),
        "negative predictive value": round(neg_pred_val(true_neg, false_neg), 3),
    }


# Calculate metrics from result (1, 0, 1, 0)
metrics = get_stats(1, 0, 1, 0)
print(metrics)
