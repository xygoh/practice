# various transformations of a 2d array
# version 1: works for nxn
# version 2: works for nxm

# rotates a 2d array 90 degrees clockwise
# opposite of counter
def rotateImage_clock(a):
    w=len(a[0])
    h=len(a)
    b=[x[:] for x in [[None]*h]*w] # initialise all to None
    for row in range(w):
        for col in range(h):
                    b[row][col]=a[h-1-col][row]
    return b

# rotates a 2d array 90 degrees counter clockwise
# row is col, col is row backwards
def rotateImage_counter(a):
	w=len(a[0])
	h=len(a)
	b=[x[:] for x in [[None]*h]*w] # initialise all to None
	for row in range(w):
		for col in range(h):
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

