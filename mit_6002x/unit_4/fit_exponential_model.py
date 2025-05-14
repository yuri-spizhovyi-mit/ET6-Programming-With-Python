import math
import pylab


def create_data(f, x_vals):
    """
    Applies function f to each element of x_vals.

    Args:
        f: a function that takes one argument
        x_vals: list or range of numbers

    Returns:
        pylab.array of results
    """
    return pylab.array([f(x) for x in x_vals])


def fit_exp_data(x_vals, y_vals):
    """
    Fits an exponential curve y = c * b^x using log base 2.

    Args:
        x_vals: x input values
        y_vals: actual y output values

    Returns:
        fit: coefficients (a, b) for log(y) = a*x + b
        base: base used for log (2.0 in this case)
    """
    log_vals = [math.log(y, 2.0) for y in y_vals]
    fit = pylab.polyfit(x_vals, log_vals, 1)
    return fit, 2.0


def predict_y(fit, base, x_vals):
    """
    Predict y values from exponential fit.

    Args:
        fit: coefficients from polyfit
        base: base of exponent (e.g., 2)
        x_vals: list of x values to predict

    Returns:
        List of predicted y values
    """
    return [base ** pylab.polyval(fit, x) for x in x_vals]


# === Example usage ===
if __name__ == "__main__":
    # Define input data
    x_vals = list(range(10))
    f = lambda x: 3**x  # Exponential function

    # Generate y values using f(x)
    y_vals = create_data(f, x_vals)

    # Plot actual values
    pylab.plot(x_vals, y_vals, "ko", label="Actual values")

    # Fit exponential model
    fit, base = fit_exp_data(x_vals, y_vals)

    # Predict values using the fit
    predicted_y_vals = predict_y(fit, base, x_vals)
    pylab.plot(x_vals, predicted_y_vals, label="Predicted values")

    # Show title and legend
    pylab.title("Fitting an Exponential Function")
    pylab.legend(loc="upper left")
    pylab.grid(True)
    pylab.show()

    # Predict f(20) using actual and model
    actual = f(20)
    predicted = base ** pylab.polyval(fit, 20)

    print(f"f(20) = {actual}")
    print(f"Predicted value = {int(predicted)}")
