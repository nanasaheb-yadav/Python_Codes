"""
Implementation of Break and Continue Statement without
using break and continue statement.
"""
class _Break(Exception):
    pass

class _Continue(Exception):
    pass

try:
    # This try block to break the loop and continue
    for i in range(10):
        try:
            if i is 8:
                # Break the loop when i is 8
                print(f"*****************I {i} value is {8} so breaking loop*****************")
                raise _Break
            if i is 5:
                print(f"I {i} value is 5 so Continue loop")
                raise _Continue
        except _Continue:
            pass
        print("Value: ", i)
except _Break:
    pass

# Continue execution after breaking loop using exception
print("\n\nContinue execution after breaking loop using exception")
