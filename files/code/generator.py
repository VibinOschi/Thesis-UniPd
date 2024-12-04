training_dataset = create_data_generator(sampling_rate=samp_rate)
training_dataset = training_dataset.batch(batch_size)
training_dataset = training_dataset.prefetch(buffer_size=2)