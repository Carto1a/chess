#include <SDL2/SDL.h>
#include <SDL2/SDL_events.h>
#include <SDL2/SDL_video.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "./window.h"

const int SDL_FLAGS = SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE;

struct Window_Private {
  int screen_size_previus_x;
  int screen_size_previus_y;
  bool running;
  bool resized;
  SDL_Window *window;
  SDL_Surface *surface;
};

void Draw(Window *);
void Process_Events(Window *);
void Process_Window_Events(Window *this, SDL_WindowEvent event);
bool Is_Running(Window *);

Window *Window_Construct() {
  SDL_Window *sdl_window = NULL;
  SDL_Surface *sdl_window_suface = NULL;

  if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
    printf("Error initializing SDL: %s", SDL_GetError());
    return NULL;
  }

  sdl_window = SDL_CreateWindow("chess", SDL_WINDOWPOS_UNDEFINED,
                                SDL_WINDOWPOS_UNDEFINED, 1280, 720,
                                SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE);

  if (!sdl_window) {
    printf("Error creating window: %s", SDL_GetError());
    SDL_Quit();
    return NULL;
  }

  SDL_SetWindowResizable(sdl_window, true);

  sdl_window_suface = SDL_GetWindowSurface(sdl_window);
  if (!sdl_window_suface) {
    printf("Error getting surface: %s", SDL_GetError());
    SDL_DestroyWindow(sdl_window);
    SDL_Quit();
    return NULL;
  }

  Window *window = malloc(sizeof(Window));
  window->Draw = Draw;
  window->Is_Running = Is_Running;
  window->Process_Events = Process_Events;

  window->_private = malloc(sizeof(Window_Private));
  window->_private->window = sdl_window;
  window->_private->surface = sdl_window_suface;
  window->_private->screen_size_previus_x = 0;
  window->_private->screen_size_previus_y = 0;
  window->_private->running = true;

  return window;
}

void Window_Desconstruct(Window *this) {
  SDL_DestroyWindow(this->_private->window);
  SDL_Quit();

  free(this->_private);
  free(this);
}

void Draw(Window *this) {
  SDL_Surface *surface = NULL;
  if (this->_private->resized) {
    this->_private->surface = SDL_GetWindowSurface(this->_private->window);
    this->_private->resized = false;
  }

  surface = this->_private->surface;

  SDL_FillRect(surface, NULL, SDL_MapRGB(surface->format, 255, 255, 255));

  SDL_UpdateWindowSurface(this->_private->window);
}

void Process_Events(Window *this) {
  SDL_Event event;
  while (SDL_PollEvent(&event) != 0) {
    printf("Event: %x\n", event.type);
    switch (event.type) {
    case SDL_QUIT:
      this->_private->running = false;
      break;
    case SDL_WINDOWEVENT:
      Process_Window_Events(this, event.window);
      break;
    }
  }
  return;
}

void Process_Window_Events(Window *this, SDL_WindowEvent event) {
  switch (event.event) {
  case SDL_WINDOWEVENT_RESIZED:
    this->_private->resized = true;
    printf("Nova dimensão: %dx%d\n", event.data1, event.data2);
    break;
  }
}

bool Is_Running(Window *this) { return this->_private->running; }
