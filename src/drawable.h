#include <SDL2/SDL_surface.h>

typedef struct Draweble {
  void (*Draw)(Draweble *, SDL_Surface *);
  void (*Update)(Draweble *);
} Draweble;
