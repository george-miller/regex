#include "test.h"
#include "../regex.h"

int testtest(){
  return 1;
}

int (*tests[])() = {
  &testtest,
};

Results testAllocator(){
  Results r = testAll(tests, 1);
  r.moduleName = malloc(15 * sizeof(char));
  strcpy(r.moduleName, __func__);
  return r;
}
