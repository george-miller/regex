objects = allocator.c
testObjects = tests/testAllocator.c
make:
	gcc -std=c99 -Wall -o regex regex.c $(objects)
t:
	gcc -std=c99 -Wall -o test tests/test.c $(objects) $(testObjects)
