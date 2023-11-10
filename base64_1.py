import base64

code = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
code_bytes = code.encode("utf-8")
encode = base64.b64encode(code_bytes)

print(encode)
