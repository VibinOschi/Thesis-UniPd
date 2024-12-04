self._model = keras.Sequential([
    layers.Input(shape=(self._sampling_rate * 10, 12)),
    layers.Bidirectional(layers.LSTM(32, return_sequences=True)),
    layers.AveragePooling1D(),
    layers.Dropout(rate=0.5),
    layers.BatchNormalization(),
    layers.Bidirectional(layers.LSTM(24, return_sequences=True)),
    layers.Dropout(rate=0.5),
    layers.Flatten(),
    layers.Dense(176, kernel_regularizer=regularizers.l2(0.02)),
    layers.Dense(44, kernel_regularizer=regularizers.l1(0.02)),
    layers.Dense(ConfigGetter().get_number_of_res_classes(), activation='sigmoid')
])