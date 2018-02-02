import sys
import termios

fd = sys.stdin.fileno()

old = termios.tcgetattr(fd)
new = termios.tcgetattr(fd)


while True :
	new[3] &= ~termios.ICANON
	new[3] &= ~termios.ECHO

	try:
	  termios.tcsetattr(fd, termios.TCSANOW, new)
	  ch = sys.stdin.read(1)

	finally:
	  termios.tcsetattr(fd, termios.TCSANOW, old)

	print(ch)