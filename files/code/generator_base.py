def ecg_generator(elements):
    for element in elements:
        x, y = load_ecg_file(element)
        yield x, y