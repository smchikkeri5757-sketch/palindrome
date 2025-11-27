import sys
if len(sys.argv) != 2:
    print("ERROR: Please provide exactly 1 string as a parameter.")
    print("Usage: python3 palindrome.py <STRING>")
    sys.exit(1)
input_str = sys.argv[1]
print("\n=== INPUT RECEIVED FROM JENKINS PARAMETERS ===")
print("String:", input_str)
normalized = input_str.replace(" ", "").lower()
is_palindrome = normalized == normalized[::-1]
print("\n===== RESULT =====")
if is_palindrome:
    print(f"'{input_str}' is a Palindrome ✅")
else:
    print(f"'{input_str}' is NOT a Palindrome ❌")
