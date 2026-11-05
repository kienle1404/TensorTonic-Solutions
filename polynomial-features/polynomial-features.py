def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    # Write code here
    res = []
    for value in values:
        tens = []
        for i in range(degree+1):
           tens.append(pow(value, i))
        res.append(tens)
    return res