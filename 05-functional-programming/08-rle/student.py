def rle_encode(data):
    data = iter(data)  # Ensure the data is an iterator
    try:
        current_char = next(data)
    except StopIteration:
        return  # Handle the case where the input data is empty
    count = 1
    for char in data:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char