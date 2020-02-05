#include <ziplib/ZipFile.h>

int main() {
    auto archive = ZipFile::Open("test.zip");
    return 0;
}
