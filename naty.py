with open("./fd955f29-128a-4681-a9b0-443ee9dfb1f6_0_0", "rb") as binary_file:
    # read the binary data
    binary_data = binary_file.read()

# convert binary to text using the UTF-8 encoding
text_data = binary_data.decode('utf-8')

# write the text data to a file
with open("textfile.txt", "w") as text_file:
    text_file.write(text_data)
