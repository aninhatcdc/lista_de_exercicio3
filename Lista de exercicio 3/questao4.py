x=int(input('digite um numero: '))
y=int(input('digite outro numero: '))
soma= x+y

for count in range(10):
    print("%d x %d = %d" % (soma, count+1, soma*(count+1)) )