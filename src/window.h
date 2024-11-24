#include <stdbool.h>

typedef struct Window_Private Window_Private;

typedef struct Window {
  void (*Draw)(struct Window *);
  void (*Process_Events)(struct Window *);
  bool (*Is_Running)(struct Window *);
  Window_Private *_private;
} Window;

Window *Window_Construct();
void Window_Desconstruct(Window *);
