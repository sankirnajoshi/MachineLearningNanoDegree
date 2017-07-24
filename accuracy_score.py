def my_accuracy(True_labels, Pred_labels):
    countsum = np.sum(np.logical_xor(Pred_labels,True_labels))
    counttot = len(Pred_labels)
    accuracy = (counttot - countsum)/(counttot*1.0)
    return accuracy