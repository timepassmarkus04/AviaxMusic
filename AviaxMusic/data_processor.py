import struct

def process_data():
    # Assume buffer is being read from a file or network
    buffer = some_data_source()

    # Check if buffer is the expected size
    if len(buffer) >= 271:
        data = struct.unpack('format', buffer)
    else:
        raise ValueError("Buffer is too small, received only {} bytes".format(len(buffer)))

    # Process the unpacked data
    # ...

# Example function for data source
def some_data_source():
    # This function should return the buffer, e.g., reading from a file
    with open('datafile.bin', 'rb') as file:
        return file.read(271)

# Run the process
if __name__ == "__main__":
    process_data()
