objects = allocator.c
testObjects = tests/testAllocator.c
make: $(objects)
	gcc -std=c99 -Wall -o regex regex.c $(objects)
t: $(testObjects) $(objects)
	gcc -std=c99 -Wall -o test tests/test.c $(testObjects) $(objects)
