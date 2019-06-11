from decimal import *
import string
import random
import pysynth as ps

getcontext().prec = 512
FIBONACCI_MAX = 512

# ============================================
def fibrec(v, pv, nCt):
    """
    Get Fibonacci value at nCt 'place'
    """
    if nCt == 0:
        return 1
    return v + fibrec(v+pv, v, nCt-1)

# ============================================
def convert(num, base):
    """
    Convert num in base (base <= 36)
    """
    res = ''
    while num > 0:
        res = string.printable[num % base] + res
        num //= base
    return res
	
def main():
	# ============================================
	# CALCUL DE PHI et CONVERSION en base 36 des décimales
	# ============================================
	v1 = fibrec(0, 1, FIBONACCI_MAX-1)
	v2 = fibrec(0, 1, FIBONACCI_MAX)
	phi = Decimal(v1)/Decimal(v2)
	phiDec = str(phi)[2:128+2] 
	base36PhiDecimals = convert(int(phiDec), 36)
	print('fib1  = ' + str(v1))
	print('fib2  = ' + str(v2))
	print("PHI decimals = " + phiDec)
	print("PHI values = " + base36PhiDecimals)

	# ============================================
	# PARCOURS et converti chaque caractère en base 10
	# MAP cette valeur avec les NOTES / OCTAVES / TIMING
	# AJOUT ds le tuple SONG pr export via PySynth
	# ============================================
	notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
	base36= {'0': 0, '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,  '7': 7,  '8': 8,  '9': 9,
			'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19,
			'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
			'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}
	timings=[16, 8, 4, 2]#, -4, -8, -16]
	song = ()
	for i in range(len(base36PhiDecimals)):
		bas10note = base36[base36PhiDecimals[i]]
		bas10note2= ord(base36PhiDecimals[i])-48 	#on fait matcher les digits
		if bas10note2 > 9:
			bas10note2 -= 39						#on fait matcher les lettres
		note = notes[bas10note % len(notes)]
		octave = bas10note // len(notes)
		note += str(octave+4) # on commence octave 4
		timing = timings[bas10note % len(timings)]
		song = (*song, (note, timing))
		#print("" + str(i) + "\t" + str(base36PhiDecimals[i]) + "\t" + str(bas10note) + "\t" + str(bas10note2) + "\t" + str(note) + "\t" + str(octave))

	# ==============================================
		
	# ==============================================
	wavname = "phitimed01.wav"
	ps.make_wav(song, fn = wavname, silent=True)
	print("File '" + wavname + "' generated")

if __name__ == '__main__':
	main()
