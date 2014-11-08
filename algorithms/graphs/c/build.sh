#!/bin/bash
#gyp -f ninja test/test.gyp --depth=. --generator-output=build
gyp -f ninja test.gyp --depth=.
ninja -C out/Release/ -v
#ninja -C build/out/Release/ -v
