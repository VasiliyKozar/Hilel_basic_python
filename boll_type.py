# # 1.Fix the eror
fix = 3 != 5
print(fix)

# 2.Arithmetic comparsions

comprasions1 = 5 == 5
print(comprasions1)

comprasions2 = 5<=5
print(comprasions2)

comprasions3 = 5>=5
print(comprasions3)

# 3. Five combination
# or
is_true1 = (4 > 3 + 0) or (3 < 5-1)
print(is_true1)

is_true2 = (1 > 1 - 2 ) or (3 + 5 < 10)
print(is_true2)

# and
is_true3 = (2 > 1 - 1) and (0 > 0 - 1)
print(is_true3)

is_true4 = (1 + 1 > 0) and (2 + 2 < 10)
print(is_true4)

# not
nicht = not False -(-2) > 3
print(nicht)

# 4. logical values
# 1.
print(bool(None) == bool(7))

print(bool(" ") == bool(10 - 1))

print(bool(True or False) == bool(print("Hello")))

print(bool(type(None)) == bool(id(None)))