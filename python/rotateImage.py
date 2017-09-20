# various transformations of a 2d array

# rotates a 2d array 90 degrees clockwise
# opposite of counter
def rotateImage_clock(a):
	b=[row[:] for row in a]
	w=len(a[0])
	h=len(a)
	for row in range(h):
		for col in range(w):
			b[col][w-1-row]=a[row][col]
	return b

# rotates a 2d array 90 degrees counter clockwise
# row is col, col is row backwards
def rotateImage_counter(a):
  b=[row[:] for row in a]
    w=len(a[0])
    h=len(a)
    for row in range(h):
      for col in range(w):
        b[row][col]=a[col][w-1-row]
  return b

# horizontal flip a 2d array
# row same, col backwards
def horizontal_flip(a):
  b=[row[:] for row in a]
    w=len(a[0])
    h=len(a)
    for row in range(h):
      for col in range(w):
        b[row][col]=a[row][w-1-col]
  return b

# vertical flip a 2d array
# row backwards, col same
def vertical_flip(a):
	b=[row[:] for row in a]
	w=len(a[0])
	h=len(a)
	for row in range(h):
		for col in range(w):
			b[row][col]=a[h-1-row][col]
	return b
  
# translates array up a row
def translateUp(a):
	b=[row[:] for row in a]
	w=len(a[0])
	h=len(a)
	for row in range(h):
		for col in range(w):
			b[row][col]=a[(row+1)%h][col]
	return b
  
