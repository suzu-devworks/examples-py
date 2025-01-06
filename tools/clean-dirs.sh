#! /usr/bin/sh
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$|/build$|/dist$|\..+_cache$)" | xargs rm -rf
find . | grep -E "(\.coverage$|coverage.(xml|json|html))" | xargs rm -rf
find . | grep -E "(/logs$)" | xargs rm -rf
