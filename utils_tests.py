import utils

u = utils.utils()

# Test the reversed function
print("Reversed tests:")

try:
    print(f"test 1 (string): {u.reversed('12345')}")
except Exception as e:
    print(f"test 1 (string): ERROR - {e}")

try:
    print(f"test 2 (float): {u.reversed(12345.)}")
except Exception as e:
    print(f"test 2 (float): ERROR - {e}")

try:
    print(f"test 3 (integer): {u.reversed(12345)}")
except Exception as e:
    print(f"test 3 (integer): ERROR - {e}")


# Test the formatter function
print("\nFormatter tests:")

try:
    print(f"test 1 (string): {u.formatter('64')}")
except Exception as e:
    print(f"test 1 (string): ERROR - {e}")

try:
    print(f"test 2 (float): {u.formatter(64.)}")
except Exception as e:
    print(f"test 2 (float): ERROR - {e}")

try:
    print(f"test 3 (integer): {u.formatter(64)}")
except Exception as e:
    print(f"test 3 (integer): ERROR - {e}")