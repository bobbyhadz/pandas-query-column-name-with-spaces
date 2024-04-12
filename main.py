# Pandas: How to Query a Column name with Spaces

import pandas

df = pandas.DataFrame({
    'first name': ['Alice', 'Bobby', 'Carl', 'Alice'],
    'age': [30, 40, 50, 60],
    'net salary': [75, 50, 100, 150]
})

# ✅ With String values
result = df.query("`first name` == 'Alice'")

#   first name  age  net_salary
# 0      Alice   30          75
# 3      Alice   60         150
print(result)


# ✅ Or with Integer Values
result = df.query("`net salary` > 50")

#   first name  age  net salary
# 0      Alice   30          75
# 2       Carl   50         100
# 3      Alice   60         150
print(result)
