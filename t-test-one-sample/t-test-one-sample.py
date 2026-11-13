import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    s = np.std(x, ddof = 1)
    mean = np.mean(x)

    return float((mean - mu0)/(s/(len(x)**(1/2))))
    pass