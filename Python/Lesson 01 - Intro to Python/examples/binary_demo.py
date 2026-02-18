import struct

# Step 1: Convert 'cool' to binary
text = 'cool'
binary_str = ''.join(format(ord(char), '08b') for char in text)
print(f"String: '{text}'")
print(f"Binary: {binary_str}")
print(f"Length: {len(binary_str)} bits")
print()

# Step 2: Convert binary to integer
as_int = int(binary_str, 2)
print(f"As integer: {as_int}")
print()

# Step 3: Interpret binary as IEEE 754 float (32-bit)
binary_int = int(binary_str, 2)
binary_bytes = binary_int.to_bytes(4, byteorder='big')
as_float = struct.unpack('!f', binary_bytes)[0]
print(f"As float (IEEE 754): {as_float}")
print()

# Step 4: Show breakdown by character
print('Character breakdown:')
for char in text:
    print(f"  '{char}' (ASCII {ord(char)}): {format(ord(char), '08b')}")
