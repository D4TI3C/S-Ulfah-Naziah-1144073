import time
start_time = time.time()
print("Menghitung Nilai Rumus Matematika Menggunakan Bahasa Jerman")
u = raw_input("Masukan Nilai 1: ")
l = raw_input("Masukan Nilai 2: ")
f = raw_input("Masukan Nilai 3: ")
a = raw_input("Masukan Nilai 4: ")
h = raw_input("Masukan Nilai 5: ")

if u == 'eins':
	u=1

if u == 'zwei':
	u=2

if u == 'drei':
	u=3

if u == 'vier':
	u=4

if u == 'funf':
	u=5

if u == 'sechs':
	u=6

if u == 'sieben':
	u=7

if u == 'acht':
	u=8

if u == 'neun':
	u=9

if u == 'null':
	u=0


if l == 'eins':
	l=1

if l == 'zwei':
	l=2

if l == 'drei':
	l=3

if l == 'vier':
	l=4

if l == 'funf':
	l=5

if l == 'sechs':
	l=6

if l == 'sieben':
	l=7

if l == 'acht':
	l=8

if l == 'neun':
	l=9

if l == 'null':
	l=0


if f == 'eins':
	f=1

if f == 'zwei':
	f=2

if f == 'drei':
	f=3

if f == 'vier':
	f=4

if f == 'funf':
	f=5

if f == 'sechs':
	f=6

if f == 'sieben':
	f=7

if f == 'acht':
	f=8

if f == 'neun':
	f=9

if f == 'null':
	f=0


if a == 'eins':
	a=1

if a == 'zwei':
	a=2

if a == 'drei':
	a=3

if a == 'vier':
	a=4

if a == 'funf':
	a=5

if a == 'sechs':
	a=6

if a == 'sieben':
	a=7

if a == 'acht':
	a=8

if a == 'neun':
	a=9

if a == 'null':
	a=0


if h == 'eins':
	h=1

if h == 'zwei':
	h=2

if h == 'drei':
	h=3

if h == 'vier':
	h=4

if h == 'funf':
	h=5

if h == 'sechs':
	h=6

if h == 'sieben':
	h=7

if h == 'acht':
	h=8

if h == 'neun':
	h=9

if h == 'null':
	h=0


jumlah =(u*l)+(f/a-h)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))