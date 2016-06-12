#include "../regex.h"
#include "test.h"

Results testAll(int (*tests[])(), int length){
  Results r;
  r.success = 0;
  r.fail = 0;
  int i = 0;
  for (; i < length; i++){
    if (tests[i]()){
      r.success++;
    }
    else{
      r.fail++;
    }
  }
  return r;
}


Results (*mainTests[])() = {
  &testAllocator,
};

int main(int argc, char **argv){
  for (int i = 0; i < 1; i++){
    Results r = mainTests[i]();
    printf("%s had %d successes and %d fails\n", r.moduleName, r.success, r.fail);
  }


  return 1;
}

void printResults(Results r){

}
