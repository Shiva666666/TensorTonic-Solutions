import numpy as np

def color_to_grayscale(image: list) -> list:
    """
    Returns the luminance value of every RGB pixel.
    """
    # Write code here

    imag = np.array(image)
    rgb = np.array([0.299, 0.587, 0.114])

    return np.dot(imag, rgb).tolist()

    
    pass