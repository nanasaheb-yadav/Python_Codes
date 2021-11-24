
try:
    w = open("text", "w")
    w.write("test write test")
except IOError as e:
    print("Cannot find file: " +e)
else:
    print(f"File END")

"""OUTPUT:
File END

"""
