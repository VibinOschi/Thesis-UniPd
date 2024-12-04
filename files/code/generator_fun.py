def create_data_generators(sampling_rate):
    y = pd.read_csv(path_to_dataset + 'new_ptb_xl.csv')

    train_df = y[(y.strat_fold == 'train')].to_numpy()

    np.random.shuffle(train_df)

    output_types = (tf.float32, tf.float32)
    output_shapes = (tf.TensorShape([sampling_rate * 10, 12]), tf.TensorShape([]))

    train_generator = tf.data.Dataset.from_generator(
        lambda: ecg_generator(train_df),
        output_types=output_types,
        output_shapes=output_shapes
    )

    return train_generator