def binarize_label(label):
    if 'NORM' in label:
        return 0
    else:
        return 1

def load_ecg_file(element):
    pre_data = [wfdb.rdsamp('dataset/ptb-xl/' + str(element[4]))]
    return np.array([signal for signal, meta in pre_data])[0], binarize_label(element[2])