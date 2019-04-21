#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class WiringpiConan(ConanFile):
    name = "wiringpi"
    version = "2.50"
    license = "LGPL-3.0"
    description = "GPIO Interface library for the Raspberry Pi"
    homepage = "http://wiringpi.com/"
    author = "Conan Community <info@conan.io>"
    topics = ("conan", "wiringpi", "gpio", "raspberrypi")
    url = "https://github.com/conan-community/conan-wiringpi"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False],
               "wpiExtensions": [True, False], "withDevLib": [True, False],
               "skipHWDetectionRPIModel3": [True, False]}
    default_options = {"shared": False, "fPIC": True,
                       "wpiExtensions": False, "withDevLib": True,
                       "skipHWDetectionRPIModel3": False}
    # the library doesn't manage very well other than raspbian so the skipHWDetectionRPIModel3
    # will force using original RPI3 Model B, 1GB RAM
    exports_sources = "CMakeLists.txt", "*.patch"
    exports = "LICENSE"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

        if self.settings.os in ("Windows", "Macos"):
            raise ConanInvalidConfiguration("This library is not suitable for Windows/Macos")

    def source(self):
        git = tools.Git()
        git.clone("git://git.drogon.net/wiringPi", branch="master")
        git.checkout(self.version)
        if self.options.skipHWDetectionRPIModel3:
            tools.patch(".", "pi3_patch_detect.patch")
            self.output.warn("Patched to skip hardware detection, always RPI3 Model B")

    def _configure_cmake(self):
        cmake = CMake(self)
        if self.options.wpiExtensions:
            cmake.definitions["WITH_WPI_EXTENSIONS"] = "ON"
        if self.options.withDevLib:
            cmake.definitions["WITH_DEV_LIB"] = "ON"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("COPYING*", src="wiringPi", dst="licenses", keep_path=False)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["wiringPi"]
        if self.options.withDevLib:
            self.cpp_info.libs.append("wiringPiDevLib")
        self.cpp_info.libs.append("pthread")
        if self.options.wpiExtensions:
            self.cpp_info.libs.append("crypt")
        self.cpp_info.libs.extend(["m", "rt"])
