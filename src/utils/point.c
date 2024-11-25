#include "./point.h"
#include <stdlib.h>

Point *Point_Constructor(int x, int y) {
  Point *point = malloc(sizeof(Point));
  point->x = x;
  point->y = y;

  return point;
}
