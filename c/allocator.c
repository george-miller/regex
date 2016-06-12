#include "regex.h"


NodeList *allocateNodeList(int initialLength){
  NodeList *nl = malloc(sizeof(NodeList));
  nl->nodes = malloc(sizeof(Node) * initialLength);
  nl->length = initialLength;
  nl->sizeOfArray = initialLength;
  return nl;
}
Graph *allocateGraph(int inputSize, int outputSize){
  Graph *g = malloc(sizeof(Graph));
  g->input = allocateNodeList(inputSize);
  g->output = allocateNodeList(outputSize);
  return g;
}

Node * allocateNode(int matchLength, int edges){
  Node *n = malloc(sizeof(Node));
  n->matchLength = matchLength;
  n->matches = malloc(sizeof(char) * matchLength);
  n->edges = allocateNodeList(edges);
  return n;
}



void deallocateNodeList(NodeList *nl){
  free(nl->nodes);
  free(nl);
}

void deallocateNode(Node *n){
  deallocateNodeList(n->edges);
  free(n->matches);
  free(n);
}

void deallocateGraph(Graph *g){
  deallocateNodeList(g->input);
  deallocateNodeList(g->output);
  free(g);
}
