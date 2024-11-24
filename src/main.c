#include "window.h"
#include <SDL2/SDL.h>

int main() {
  Window *window = Window_Construct();

  while (window->Is_Running(window)) {
    window->Process_Events(window);
    window->Draw(window);
  }

  Window_Desconstruct(window);

  return 1;
}
