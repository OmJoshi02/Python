import array

# Signed char
arr_b = array.array('b', [-5, 0, 5, 10])
print("Signed char (b):", arr_b)

# Unsigned char
arr_B = array.array('B', [0, 10, 20, 255])
print("Unsigned char (B):", arr_B)

# Signed short
arr_h = array.array('h', [-300, 100, 200, 300])
print("Signed short (h):", arr_h)

# Unsigned short
arr_H = array.array('H', [0, 100, 200, 65535])
print("Unsigned short (H):", arr_H)

# Signed int
arr_i = array.array('i', [-1000, 0, 1000, 2000])
print("Signed int (i):", arr_i)

# Unsigned int
arr_I = array.array('I', [0, 1000, 2000, 4000])
print("Unsigned int (I):", arr_I)

# Signed long
arr_l = array.array('l', [-50000, 0, 50000, 100000])
print("Signed long (l):", arr_l)

# Unsigned long
arr_L = array.array('L', [0, 50000, 100000, 200000])
print("Unsigned long (L):", arr_L)

# Signed long long
arr_q = array.array('q', [-10**12, -100, 0, 100, 10**12])
print("Signed long long (q):", arr_q)

# Unsigned long long
arr_Q = array.array('Q', [0, 100, 10**6, 10**12])
print("Unsigned long long (Q):", arr_Q)

# Float (single precision)
arr_f = array.array('f', [1.1, 2.2, 3.3, 4.4])
print("Float (f):", arr_f)

# Double (double precision float)
arr_d = array.array('d', [1.11, 2.22, 3.33, 4.44])
print("Double (d):", arr_d)

# Unicode characters (⚠ deprecated, but still works in Python 3)
arr_u = array.array('u', ['a', 'b', 'c', 'd']) 
print(arr_u)
