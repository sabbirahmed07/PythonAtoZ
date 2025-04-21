# encode(encoding) - Return encoded string
txt = "My name is Ståle"
print(txt.encode())  # Default: UTF-8
print(txt.encode("ascii", "ignore"))  # Ignore error
