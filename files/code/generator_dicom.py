def _load_single_ecg(self, element):
    # Loads from a DICOM file the ECG signals
    pre_data = dcmread(ConfigGetter().get_dicom_dataset_path() + str(element[4]))
    data = pre_data.waveform_array(0) / 1000

    data = self._downsample_ecg(data)

    if self._preprocessing:
        data = self._preprocess_ecg(data)

    if self._binary_labels:
        return data, binarize_label(element[2])
    else:
        return data, encode_label_for_multilabel(element[2])
    
def _ecg_generator(self, elements):
    for element in elements:
        x, y = self._load_single_ecg(element)
        yield x, y