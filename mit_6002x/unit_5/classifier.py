"""
🎯 Scenario: Spam Classifier Evaluation
You built a spam classifier and tested it on 100 email messages:

True Positives (TP): 40 → Spam emails correctly identified as spam

False Positives (FP): 10 → Non-spam emails incorrectly marked as spam

True Negatives (TN): 45 → Non-spam emails correctly identified

False Negatives (FN): 5 → Spam emails missed (classified as not spam)

Now let’s compute the evaluation metrics using your functions.


"""


# Define your existing functions
def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator / denominator


def sensitivity(truePos, falseNeg):
    try:
        return truePos / (truePos + falseNeg)
    except ZeroDivisionError:
        return float("nan")


def specificity(trueNeg, falsePos):
    try:
        return trueNeg / (trueNeg + falsePos)
    except ZeroDivisionError:
        return float("nan")


def posPredVal(truePos, falsePos):
    try:
        return truePos / (truePos + falsePos)
    except ZeroDivisionError:
        return float("nan")


def negPredVal(trueNeg, falseNeg):
    try:
        return trueNeg / (trueNeg + falseNeg)
    except ZeroDivisionError:
        return float("nan")


def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint=True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    npv = negPredVal(trueNeg, falseNeg)
    if toPrint:
        print(" Accuracy        =", round(accur, 3))
        print(" Sensitivity     =", round(sens, 3))  # Recall or True Positive Rate
        print(" Specificity     =", round(spec, 3))  # True Negative Rate
        print(" Pos. Pred. Val. =", round(ppv, 3))  # Precision
        print(" Neg. Pred. Val. =", round(npv, 3))  # NPV
    return (accur, sens, spec, ppv, npv)


# Example values for a spam classifier
truePos = 40
falsePos = 10
trueNeg = 45
falseNeg = 5

# Call the function
getStats(truePos, falsePos, trueNeg, falseNeg)
