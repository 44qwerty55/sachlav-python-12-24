print(True ^ True)

#      1   True   3 True      2  False
print(True ^ False or True and False)

# 1000 0001
# 1000 0001
# ----------
# 0000 0000   -> False

# 1000 0000
# 1000 0001
# ----------
# 0000 0001   -> True