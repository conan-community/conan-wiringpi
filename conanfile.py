from conans import ConanFile, AutoToolsBuildEnvironment, tools, CMake


class WiringpiConan(ConanFile):
    name = "wiringpi"
    version = "2.46"
    description = "GPIO Interface library for the Raspberry Pi"
    homepage = "http://wiringpi.com/"
    url = "https://github.com/conan-community/conan-wiringpi"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports = "CMakeLists.txt"
    generators = "cmake"

    def source(self):
        self.run("git clone git://git.drogon.net/wiringPi")
        with tools.chdir("wiringPi"):
            self.run("git checkout %s" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", src="wiringPi/wiringPi", dst="include", keep_path=True)
        self.copy("*.so*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["wiringPi", "pthread", "crypt", "m", "rt"]
