import numpy as np

def classification_metrics(y_true: list[int], y_pred: list[int], average: str = "micro", pos_label: int = 1) -> dict:
    """
    Returns a dictionary containing accuracy, precision, recall, and f1 rounded to six decimals.
    """
    # Write code here
    num_classes = len(set(y_pred + y_true))
    conf = np.zeros((num_classes, num_classes))

    for i in range(len(y_pred)):
        conf[y_true[i]][y_pred[i]] += 1

    tp = []
    fn = []
    fp = []
    support = []

    for c in range(num_classes):
        curr_tp = conf[c][c]
        curr_fn = np.sum(conf[c]) - curr_tp
        curr_fp = np.sum(conf[:, c]) - curr_tp

        tp.append(curr_tp)
        fn.append(curr_fn)
        fp.append(curr_fp)
        support.append(np.sum(conf[c]))

    def macro(tp, fn, fp):
        acc = np.trace(conf) / np.sum(conf)

        precision = []
        recall = []
        f1 = []

        for c in range(num_classes):

            p = tp[c] / (tp[c] + fp[c]) if tp[c] + fp[c] != 0 else 0
            r = tp[c] / (tp[c] + fn[c]) if tp[c] + fn[c] != 0 else 0
            f = 2 * p * r / (p + r) if p + r != 0 else 0

            precision.append(p)
            recall.append(r)
            f1.append(f)

        return acc, np.mean(precision), np.mean(recall), np.mean(f1)

    def micro(tp, fn, fp):
        acc = np.trace(conf) / np.sum(conf)

        total_tp = np.sum(tp)
        total_fn = np.sum(fn)
        total_fp = np.sum(fp)

        precision = total_tp / (total_tp + total_fp) if total_tp + total_fp != 0 else 0
        recall = total_tp / (total_tp + total_fn) if total_tp + total_fn != 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0

        return acc, precision, recall, f1

    def weighted(tp, fn, fp):
        acc = np.trace(conf) / np.sum(conf)

        precision = []
        recall = []
        f1 = []

        for c in range(num_classes):

            p = tp[c] / (tp[c] + fp[c]) if tp[c] + fp[c] != 0 else 0
            r = tp[c] / (tp[c] + fn[c]) if tp[c] + fn[c] != 0 else 0
            f = 2 * p * r / (p + r) if p + r != 0 else 0

            precision.append(p)
            recall.append(r)
            f1.append(f)

        total_support = np.sum(support)

        precision = np.sum(np.array(precision) * np.array(support)) / total_support
        recall = np.sum(np.array(recall) * np.array(support)) / total_support
        f1 = np.sum(np.array(f1) * np.array(support)) / total_support

        return acc, precision, recall, f1

    def binary(tp, fn, fp):
        acc = np.trace(conf) / np.sum(conf)

        p = tp[pos_label] / (tp[pos_label] + fp[pos_label]) if tp[pos_label] + fp[pos_label] != 0 else 0
        r = tp[pos_label] / (tp[pos_label] + fn[pos_label]) if tp[pos_label] + fn[pos_label] != 0 else 0
        f1 = 2 * p * r / (p + r) if p + r != 0 else 0

        return acc, p, r, f1

    if average == "macro":
        acc, precision, recall, f1 = macro(tp, fn, fp)

    elif average == "micro":
        acc, precision, recall, f1 = micro(tp, fn, fp)

    elif average == "weighted":
        acc, precision, recall, f1 = weighted(tp, fn, fp)

    elif average == "binary":
        acc, precision, recall, f1 = binary(tp, fn, fp)

    return {
        "accuracy": round(float(acc), 6),
        "precision": round(float(precision), 6),
        "recall": round(float(recall), 6),
        "f1": round(float(f1), 6)
    }