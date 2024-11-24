typedef struct GameProcess {
  void (*Draw)();
  void (*Update)();
} GameProcess;

GameProcess *GameProcess_Construct();
GameProcess *GameProcess_Desconstruct();
