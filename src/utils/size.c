#include "./size.h"
#include <stdlib.h>

Size *Size_Constructor(int height, int width) {
  Size *size = malloc(sizeof(Size));
  size->width = width;
  size->height = height;

  return size;
}
