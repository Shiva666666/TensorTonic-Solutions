def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    curr_step = 0
    
    def compute(loc_a, loc_b, x):
        fx = (2*loc_a*x) + loc_b
        return x - (lr*fx)

    while curr_step < steps:
        x0 = compute(a,b,x0)
        curr_step+=1

    return x0
        
    pass