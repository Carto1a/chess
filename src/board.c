#include "./board.h"
#include <SDL2/SDL_rect.h>
#include <stdlib.h>

struct Board_Private {};

static void Draw(Board *, SDL_Surface *);
static void Update(Board *);

Board *Board_Constructor() {
  Board *board = malloc(sizeof(Board));

  board->Draw = Draw;
  board->Update = Update;

  board->_private = malloc(sizeof(Board_Private));

  return board;
}

void Draw(Board *this, SDL_Surface *surface) {
  SDL_Rect rect = {-50, -50, 100, 100};
  SDL_FillRect(surface, &rect, SDL_MapRGB(surface->format, 0, 0, 0));
}
void Update(Board *this) {}

void Board_Desconstructor(Board *this) {
  free(this->_private);
  free(this);
}
