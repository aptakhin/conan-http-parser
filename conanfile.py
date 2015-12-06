from conans import ConanFile, CMake
from conans.tools import get
import os
import shutil

class HttpParser(ConanFile):
    name = "http-parser"
    version = "2.6.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "http://github.com/aptakhin/conan-http-parser"
    exports = "HttpParserCMakeLists.txt"

    def source(self):
        zip_name = "http-parser-v2.6.0.zip"
        get("https://github.com/nodejs/http-parser/archive/v2.6.0.zip")
        shutil.move("http-parser-2.6.0", "http-parser")

        shutil.move("HttpParserCMakeLists.txt", "http-parser/CMakeLists.txt")

    def build(self):
        cmake = CMake(self.settings)
        self.run("cd http-parser && cmake . %s" % cmake.command_line)
        self.run("cd http-parser && cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="http-parser")
        self.copy("*.lib", dst="lib", src="http-parser/lib")
        self.copy("*.a", dst="lib", src="http-parser/lib")

    def package_info(self):
        self.cpp_info.libs = ["http-parser"]
