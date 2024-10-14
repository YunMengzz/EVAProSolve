import base64
base64_string = "SGVsbG8sIHdvcmxkIQ=="
decoded_bytes = base64.b64decode(base64_string)
binary_data = bytes(decoded_bytes)
print(binary_data)
