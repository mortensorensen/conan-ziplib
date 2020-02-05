from conans import ConanFile, CMake, tools
import os


class ZiplibConan(ConanFile):
    name = "ziplib"
    version = "1.0.0"
    license = "https://bitbucket.org/wbenny/ziplib/src/master/Licence.txt"
    url = "https://github.com/mortensorensen/conan-ziplib"
    homepage = "https://bitbucket.org/wbenny/ziplib"
    description = "Lightweight C++11 library for working with ZIP archives with ease"
    topics = ("conan", "zip", "compression")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
    }
    default_options = {
        "shared": False,
    }
    exports_sources = "CMakeLists.txt"
    _source_subfolder = "ziplib"

    def source(self):
        sha1 = "176e4b6d51fc"
        tools.get("{}/get/{}.zip".format(self.homepage, sha1))
        extracted_dir = "wbenny-ziplib-" + sha1
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        src_folder = "{}/Source/ZipLib".format(self._source_subfolder)
        self.copy("Licence.txt", dst="licenses", src=self._source_subfolder)
        self.copy("*.h", dst="include/ziplib", src=src_folder)
        self.copy("*.inc", dst="include/ziplib", src=src_folder)
        self.copy("*.a", dst="lib", src=".", keep_path=False)
        self.copy("*.lib", dst="lib", src=".", keep_path=False)
        self.copy("*.dylib", dst="lib", src=".", keep_path=False)
        self.copy("*.so", dst="lib", src=".", keep_path=False)
        self.copy("*.dll", dst="bin", src=".", keep_path=False)
