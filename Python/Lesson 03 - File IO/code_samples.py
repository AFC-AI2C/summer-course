
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

text_to_write = [
    "This is a new line of text.\n",
    "Here is another line.\n",
    "And yet another line.\n"
]
with open('output.txt', 'w') as file:
    for text in text_to_write:
        file.write(text)


file_handle = open('output.txt', 'r')
content = file_handle.read()
file_handle.close()

with open('output.txt', 'r') as file_handle:
    content = file_handle.read()

with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
    for line in input:
        output.write(line.strip().upper() + '\n')

