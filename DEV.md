`python -m lambdata_nsriniva.helper_functions`

`mypy -p lambdata_nsriniva`

`pylint lambdata_nsriniva/helper_functions.py`

`autopep8 lambdata_nsriniva/helper_functions.py > helper_functions.py; cp helper_functions.py lambdata_nsriniva/helper_functions.py;rm helper_functions.py`

`python lambdata_test.py `

`rm -rf dist build lambdata_nsriniva.egg-info`

`python setup.py sdist bdist_wheel`

`twine upload --repository testpypi dist/*`

`docker build Docker -t python` : Use `docker build Docker --no-cache -t python` if a new version of any package needs to be installed in the image.


`docker run -it python python lambdata_test.py`