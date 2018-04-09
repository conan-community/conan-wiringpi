from conans import ConanFile, AutoToolsBuildEnvironment, tools, CMake


class WiringpiConan(ConanFile):
    name = "wiringpi"
    version = "2.46"
    settings = "os", "compiler", "build_type", "arch"
    exports = "CMakeLists.txt"

    def source(self):
        self.run("git clone git://git.drogon.net/wiringPi")
	#with tools.chdir("wiringPi"):
         #   self.run("git checkout 2.46")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
#	with tools.chdir("wiringPi/wiringPi"):
#            atools = AutoToolsBuildEnvironment(self)
#            atools.make()

    def package(self):
	self.copy("*.h", src="wiringPi/wiringPi", dst="include", keep_path=True)
        self.copy("*.so*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["wiringPi"]
