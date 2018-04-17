from conans import ConanFile, AutoToolsBuildEnvironment, tools, CMake


class WiringpiConan(ConanFile):
    name = "wiringpi"
    version = "2.46"
    description = "GPIO Interface library for the Raspberry Pi"
    homepage = "http://wiringpi.com/"
    url = "https://github.com/conan-community/conan-wiringpi"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False, fPIC=False"
    exports = "CMakeLists.txt"
    generators = "cmake"

    def configure(self):
        del self.settings.libcxx

        if self.settings.os in ("Windows", "Macos"):
            raise Exception("This library is not suitable for Windows/Macos")

    def source(self):
        self.run("git clone git://git.drogon.net/wiringPi")
        with tools.chdir("wiringPi"):
            self.run("git checkout %s" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", src="wiringPi/wiringPi", dst="include", keep_path=True)
        self.copy("*.a*", dst="lib", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["wiringPi", "pthread", "crypt", "m", "rt"]
