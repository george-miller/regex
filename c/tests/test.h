#ifndef TEST
#define TEST

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Results {
  int success;
  int fail;
  char *moduleName;
} Results;

Results testAllocator();
Results testAll();



#endif
