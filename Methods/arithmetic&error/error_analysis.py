
import math


# 1. Absolute error
def absolute_error(actual, approximate):

    return abs(actual - approximate)


# 2. Relative error
def relative_error(actual, approximate):

    if actual == 0:
        return None

    return abs(actual - approximate) / abs(actual)


# 3. Percentage error
def percentage_error(actual, approximate):

    error = relative_error(actual, approximate)

    if error is None:
        return None

    return error * 100


# 4. Calculate all errors together
def compare_errors(actual, approximate):

    absolute = absolute_error(actual, approximate)
    relative = relative_error(actual, approximate)

    percentage = None if relative is None else relative * 100

    return {
        "actual": actual,
        "approximate": approximate,
        "absolute_error": absolute,
        "relative_error": relative,
        "percentage_error": percentage
    }


# 5. Rounding error
def rounding_error(number, decimal_places):

    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative")

    rounded = round(number, decimal_places)

    return {
        "original": number,
        "rounded": rounded,
        "error": abs(number - rounded)
    }


# 6. Compare different rounding precisions
def rounding_comparison(number):

    results = []

    for places in [2, 4, 6, 8]:

        result = rounding_error(number, places)

        results.append(result)

    return results


# 7. Taylor series approximation of sin(x)
def taylor_sine_approximation(x, terms):

    if terms < 1:
        raise ValueError("Terms must be at least 1")

    approximation = 0

    term_details = []

    for n in range(terms):

        power = 2 * n + 1

        term = ((-1) ** n) * (x ** power) / math.factorial(power)

        approximation += term

        term_details.append({
            "term": n + 1,
            "value": term,
            "running_sum": approximation
        })

    actual = math.sin(x)

    return {
        "x": x,
        "approximation": approximation,
        "actual_value": actual,
        "truncation_error": abs(actual - approximation),
        "terms": term_details
    }
