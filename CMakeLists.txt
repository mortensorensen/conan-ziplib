cmake_minimum_required(VERSION 3.10)

project(ziplib
  VERSION 1.0
  LANGUAGES C CXX)

set(ZIPLIB_SRC_DIR ${CMAKE_BINARY_DIR}/ziplib/Source/ZipLib)

file(GLOB ziplib_src ${ZIPLIB_SRC_DIR}/*.cpp)
file(GLOB ziplib_detail_src ${ZIPLIB_SRC_DIR}/detail/*.cpp)
file(GLOB src_zlib ${ZIPLIB_SRC_DIR}/extlibs/zlib/*.c)
file(GLOB src_lzma ${ZIPLIB_SRC_DIR}/extlibs/lzma/unix/*.c)
file(GLOB src_bzip2 ${ZIPLIB_SRC_DIR}/extlibs/bzip2/*.c)
add_library(${PROJECT_NAME}
  ${ziplib_src}
  ${ziplib_detail_src}
  ${src_zlib}
  ${src_lzma}
  ${src_bzip2})
target_compile_options(ziplib
  PUBLIC
    -Wno-enum-conversion
    -Wno-tautological-undefined-compare
    -Wno-shift-negative-value)
target_include_directories(${PROJECT_NAME} PUBLIC ${ZIPLIB_SRC_DIR})
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_11)
