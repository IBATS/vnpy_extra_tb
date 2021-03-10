#!/bin/bash
rm -rf dist
python setup.py bdist_wheel
rm -rf build
twine upload -u mmmaaaggg dist/*
