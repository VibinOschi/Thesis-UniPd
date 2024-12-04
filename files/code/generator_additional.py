def _load_single_ecg(self, element):
    pre_data = [wfdb.rdsamp(ConfigGetter().get_dataset_path() + str(element[4]))]
    data = np.array([signal for signal, meta in pre_data])[0]

    data = self._downsample_ecg(data)

    if self._preprocessing:
        data = self._preprocess_ecg(data)

    # ...

    # Adds the Age and the Sexuality
    additional_information = [element[0], element[1]]

    return data, additional_information, label

def _ecg_generator(self, elements):
    for element in elements:
        x, x_add, y = self._load_single_ecg(element)
        yield (x, x_add), y