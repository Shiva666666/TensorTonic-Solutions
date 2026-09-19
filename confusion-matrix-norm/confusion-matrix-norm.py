import numpy as np

def confusion_matrix_norm(y_true: list, y_pred: list, num_classes: int | None = None, normalize: str = "none") -> np.ndarray:
    """
    Returns the confusion matrix as a NumPy array.
    """
    Data_size = len(y_true)

    if not num_classes:
        temp = set(y_pred + y_true)
        num_classes = max(temp)+1

    conf_matrix = np.zeros((num_classes, num_classes))

    for i in range(Data_size):
        conf_matrix[y_true[i]][y_pred[i]] += 1

    if normalize == "none":
        return conf_matrix

    elif normalize == "true":
        row_sum = conf_matrix.sum(axis = 1)
        row_sum = row_sum[:, None]
        return conf_matrix/row_sum
    
    elif normalize == "pred":
        col_sum = conf_matrix.sum(axis = 0)
        return conf_matrix/col_sum 
        
    else:
        overall_sum = conf_matrix.sum()
        return conf_matrix/overall_sum 
    pass