cmake_minimum_required(VERSION 2.8.11)
project(wiringPi C)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup()
endif()

FILE(GLOB SRC_FILES wiringPi/*.c)
if(NOT WITH_WPI_EXTENSIONS)
  list(FILTER SRC_FILES EXCLUDE REGEX ".*wpiExtensions.c")
  list(FILTER SRC_FILES EXCLUDE REGEX ".*drcNet.c")
endif()

add_library(${PROJECT_NAME} ${SRC_FILES})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/wiringPi)
target_link_libraries(${PROJECT_NAME} PUBLIC ${CONAN_LIBS})

if(WITH_DEV_LIB)
    FILE(GLOB SRC_FILES devLib//*.c)
    list(FILTER SRC_FILES EXCLUDE REGEX ".*piFaceOld.c")
    add_library(wiringPiDevLib ${SRC_FILES})
    target_include_directories(wiringPiDevLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/devLib ${CMAKE_CURRENT_SOURCE_DIR}/wiringPi)
endif()

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY wiringPi/ DESTINATION include
        FILES_MATCHING PATTERN "*.h")

if(WITH_DEV_LIB)

    install(TARGETS wiringPiDevLib
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

    install(DIRECTORY devLib/ DESTINATION include
            FILES_MATCHING PATTERN "*.h")
endif()