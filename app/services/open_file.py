def open_file(path):
    with open(path, 'r') as f:
        content = f.read()

    return content
