#include "test.h"

int testtest(){return 1;}

int (*tests[])() = {
  &testtest,
};

Results testAllocator(){
  Results r = testAll(tests, 1);
  r.moduleName = __func__;
  return r;
}
