# MD5 (string - hexadecimal)
import hashlib

str2hash = "Jl2wAQRT17ARIqZ2Q0SL"
result = hashlib.md5(str2hash.encode())

print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())