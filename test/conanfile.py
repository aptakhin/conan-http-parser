from conans import ConanFile, CMake
import os

class HttpParserConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "http-parser/2.6.0@aptakhin/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake . %s" % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(os.sep.join([".", "bin", "test"]))
