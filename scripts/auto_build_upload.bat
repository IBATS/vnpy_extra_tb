rd /s /Q dist
python setup.py bdist_wheel
rd /s /Q build
twine upload -u mmmaaaggg dist/*