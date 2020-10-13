# node-addon-api Conan package
# Dmitriy Vetutnev, Odant, 2020


from conans import ConanFile


class CImgConan(ConanFile):
    name = "node-addon-api"
    version = "3.0.2"
    license = "MIT https://raw.githubusercontent.com/nodejs/node-addon-api/master/LICENSE.md"
    description = "This module contains header-only C++ wrapper classes which simplify the use of the C based N-API provided by Node.js when using C++. It provides a C++ object model and exception handling semantics with low overhead."
    url = "https://github.com/odant/conan-node-addon-api"
    exports_sources = "src/napi.h", "src/napi-inl.h", "src/napi-inl.deprecated.h"
    no_copy_source = True

    def package(self):
        self.copy("napi.h", src="src", dst="include")
        self.copy("napi-inl.h", src="src", dst="include")
        self.copy("napi-inl.deprecated.h", src="src", dst="include")

    def package_id(self):
        self.info.header_only()

