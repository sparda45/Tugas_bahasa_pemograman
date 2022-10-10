#biner dari angka 0
print(format(0,'08b'))

#biner dari angka 1
print(format(1,'08b'))

#biner dari angka 2
print(format(2,'08b'))


a=1
b=33
print('a=',a,'=',format(a,'08b'))
print('b=',b,'=',format(b,'08b'), '\n')

print('[AND]')
print('a & b' , a & b)
print(format(a,'08b'),'&', format(b,'08b'), '=', format(a & b, '08b'),'\n')

print('[OR]')
print('a OR b' , a | b)
print(format(a,'08b'),'|', format(b,'08b'), '=', format(a | b, '08b'),'\n')

print('[XOR]')
print('a ^ b' , a ^ b)
print(format(a,'08b'),'^', format(b,'08b'), '=', format(a ^ b, '08b'),'\n')

print('[NOT]')
print('~a  ~b' , ~a , ~b )
print('~' + format(a,'08b'),'~'+ format(b,'08b'), '=', format(~a , '08b'), format(~b , '08b'),'\n')

print('[SHIFT LEFT]')
print('b << a' , b << a)
print(format(b,'08b'),'<<', format(a,'08b'), '=', format(b << a, '08b'),'\n')

print('[SHIFT RIGHT]')
print('a >> b' , a >> b)
print(format(a,'08b'),'>>', format(b,'08b'), '=', format(a >> b, '08b'),'\n')