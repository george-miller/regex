#ifndef REGEX
#define REGEX

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node;

typedef struct NodeList {
  struct Node *nodes;
  int length;
  int sizeOfArray;
} NodeList;

typedef struct Node {
  int matchLength;
  char *matches;
  NodeList *edges;
} Node;

typedef struct Graph {
  NodeList *input;
  NodeList *output;
} Graph;

typedef struct Found {
  char *text;
  int start;
  int end;
} Found;

void allocateNodeList

#endif
