typedef struct Board {
  void (*Draw)();
  void (*Update)();
} Board;

struct Board *Board_Constructor();
struct Board *Board_Desconstructor();
