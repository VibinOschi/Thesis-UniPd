input_layer = keras.Input(shape=(self._sampling_rate * 10, 12))

x1 = keras.layers.Conv1D(filters=24, kernel_size=40, strides=1, activation='relu')(input_layer)
x1 = keras.layers.AveragePooling1D()(x1)
x1 = keras.layers.Dropout(rate=0.4)(x1)
x1 = keras.layers.BatchNormalization()(x1)
x1 = keras.layers.Conv1D(filters=48, kernel_size=10, strides=1, activation='relu')(x1)
x1 = keras.layers.Dropout(rate=0.3)(x1)
x1 = keras.layers.Flatten()(x1)

additional_input = keras.Input(shape=(2,))
x2 = keras.layers.Dense(16)(additional_input)
x2 = keras.layers.Dense(16)(x2)
x2 = keras.layers.Dense(16)(x2)

x = concatenate([x1, x2])
x = keras.layers.Dense(125)(x)
x = keras.layers.Dense(25, kernel_regularizer=regularizers.l2(0.01))(x)

output_layer = tf.keras.layers.Dense(ConfigGetter().get_number_of_res_classes(), activation=activation)(x)

self._model = keras.Model(inputs=[input_layer, additional_input], outputs=output_layer)