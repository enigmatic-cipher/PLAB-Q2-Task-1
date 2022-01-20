"""
Given a string as input. Give count of character 'x' and 'y' in given string.
Input-> "exactly"
Output-> 
x#1 
y#1
"""

st = "exactly"
ln = len(st)
pt = "#"
st_1 = 0
st_2 = 00
for i in range(0,ln):
  ch = st[i]
  if (ch=="x"):
    st_1 = st_1 + 1
  elif (ch=="y"):
    st_2 = st_2 + 1
print(f"x#{st_1}")
print(f"y#{st_2}")

