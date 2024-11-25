cmake_minimum_required(VERSION 3.10)

set(PROJECT_NAME chess)

project(${PROJECT_NAME})

find_package(SDL2 REQUIRED)
include_directories(${PROJECT_NAME} ${SDL2_INCLUDE_DIRS})

file(GLOB_RECURSE SOURCES "src/*.c" "src/util/*.c")
file(GLOB_RECURSE HEADERS "src/*.h" "src/util/*.h")
add_executable(chess ${SOURCES} ${HEADERS})

target_link_libraries(${PROJECT_NAME} ${SDL2_LIBRARIES})
