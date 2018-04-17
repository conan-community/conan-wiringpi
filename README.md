# conan-wiringpi

![conan-wiringpi image](/images/conan-wiringpi.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/wiringpi%3Aconan/images/download.svg?version=2.46%3Astable)](https://bintray.com/conan-community/conan/wiringpi%3Aconan/2.46%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-wiringpi.svg?branch=stable%2F2.46)](https://travis-ci.org/conan-community/conan-wiringpi)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/2.46?svg=true)](https://ci.appveyor.com/project/<appveyor_user>/conan-wiringpi/branch/stable/2.46)

[Conan.io](https://conan.io) package for [wiringpi](http://wiringpi.com/) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/wiringpi%3Aconan).

## Basic setup

    $ conan install wiringpi/2.46@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    wiringpi/2.46@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)