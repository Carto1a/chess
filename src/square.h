#include <SDL2/SDL_surface.h>

typedef struct Square {
  void (*Draw)(Square *, SDL_Surface *);
  void (*Update)(Square *);
} Square;
