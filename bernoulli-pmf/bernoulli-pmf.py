import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here

    for i in range(len(x)):
        x[i] = 1-p if not x[i] else p

    arr = np.array(x)

    return {"pmf": arr, "mean": float(p), "variance": float(p*(1-p))}
    pass