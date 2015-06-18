from itertools import cycle

# Decryptez le message encrypte avec un XOR

# cycle can take care of repeting the key for you
# ex: pythonpythonpythonpythonpyt
key = cycle("python")

# The cipher is encoded in hex
cipher = "383c38384f3b2358543a0e015011151b4f1a111211064f0f07180d48001b0259121a0a0b14161949"

# Note: XOR can only be applied to integers
