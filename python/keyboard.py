from getch import getch, pause
 
print "Push any key. (ESC : exit)"
 
while True:
  key = ord(getch())

  if key == 13: # Enter
    print "Enter"
    pass

  elif key == 27: # ESC
    key = ord(getch())

    if key == 91: # Arrow keys
      key = ord(getch())
      if key == 66:
        print "Down Arrow"
      elif key == 65:
        print "Up Arrow"
      elif key == 68:
        print "Left Arrow"
      elif key == 67:
        print "Right Arrow"

    elif key == 27: # ESC
      print "ESC : exit."
      break

  else:
    print "You pressed: %s (%d)" % (chr(key), key)
    if key == "x":
      print "exit."
      break
 
pause()