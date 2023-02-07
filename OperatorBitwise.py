# Bisa dikatakan operasi biner
# Bitwise, operasi masing - masing bit

a = 9
b = 5

# Bitwise OR (|)
c = a | b 
print('\n========OR=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('---------------------------(|)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# Bitwise AND (&)
c = a & b 
print('\n========AND=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('---------------------------(&)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b 
print('\n========OR=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('---------------------------(^)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# Bitwise NOT (~)
c = ~a 
print('\n========NOT=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('---------------------------(~)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# Shifting
# Shift Right
c = a >> 2 
print('\n========NOT=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('---------------------------(>>)')
print('nilai :',c,' ,binary :',format(c,'08b'))
# Shift Left
c = a << 2 
print('\n========NOT=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('---------------------------(<<)')
print('nilai :',c,' ,binary :',format(c,'08b'))
