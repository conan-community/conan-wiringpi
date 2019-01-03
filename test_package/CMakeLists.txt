cmake_minimum_required(VERSION 2.8.11)
project(test_package C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

message("LIBS: ${CONAN_LIBS}")

add_executable(test_package test_package.c)
target_link_libraries(test_package ${CONAN_LIBS})
