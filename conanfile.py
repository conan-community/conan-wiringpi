#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class WiringpiConan(ConanFile):
    name = "wiringpi"
    version = "2.46"
    license = "LGPL-3.0"
    description = "GPIO Interface library for the Raspberry Pi"
    homepage = "http://wiringpi.com/"
    author = "Conan Community <info@conan.io>"
    topics = ("conan", "wiringpi", "gpio", "raspberrypi")
    url = "https://github.com/conan-community/conan-wiringpi"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "CMakeLists.txt"
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

    def _configure_cmake(self):
        cmake = CMake(self)
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
        self.cpp_info.libs = ["wiringPi", "pthread", "crypt", "m", "rt"]
