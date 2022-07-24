python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal

# Alternative
# python -m build --sdist --wheel --outdir dist/ .

# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*