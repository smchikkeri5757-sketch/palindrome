import sys

if len(sys.argv)==2:
  script_name = sys.argv[0]
  name = sys.argv[1]

else:
  name = "gadag"

if name == name[::-1]:
  print(f"{name} is a palindrome")

else:
  print(f"{name} is not a palindrome")
