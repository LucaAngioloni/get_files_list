# Get Files List

Python package that provides a utility function to recursively get files that match a pattern.

## Usage

Example of this package usage in a folder with the following structure:

```txt
 ├──         LICENSE
 ├──         README.md
 ├──         deploy.sh
 └──         get_files_list/
 │  ├────         __init__.py
 │  └────         get_dir_content.py
 ├──         requirements.in
 ├──         requirements.txt
 └──         setup.py
```

The following code:

```python
from get_files_list import get_dir_content

# Print every file
print("Print every file\n")
for file in get_dir_content("./"):
    print(file)

# Print everyPython file
print("\n\nPrint every Python file\n")
for file in get_dir_content("./", pattern="*.py"):
    print(file)

# Print every Python file without the prepended folder name
print("\n\nPrint every Python file without the prepended folder name\n")
for file in get_dir_content("./", prepend_folder_name=False, pattern="*.py"):
    print(file)

# Print every file without recursion
print("\n\nPrint every file without recursion\n")
for file in get_dir_content("./", recursive=False):
    print(file)

# Print every file that is not a Python file
print("\n\nPrint every file that is not a Python file\n")
for file in get_dir_content("./", exclude_pattern="*.py"):
    print(file)
```

Would output:

```txt
Print every file

./LICENSE
./requirements.txt
./get_files_list/get_dir_content.py
./get_files_list/__init__.py
./README.md
./setup.py
./deploy.sh
./requirements.in


Print every python file

./get_files_list/get_dir_content.py
./get_files_list/__init__.py
./setup.py


Print every python file without the prepended folder name

get_files_list/get_dir_content.py
get_files_list/__init__.py
setup.py


Print every file without recursion

./LICENSE
./requirements.txt
./README.md
./setup.py
./deploy.sh
./requirements.in


Print every file that is not a Python file

./LICENSE
./requirements.txt
./README.md
./deploy.sh
./requirements.in
```

`get_dir_content` is a Python *generator* so the following code would not work:

```python
from get_files_list import get_dir_content

num_py_files = len(get_dir_content("./", pattern="*.py"))
# TypeError: object of type 'generator' has no len()

# You have to explicitely generate a list
num_py_files = len(list(get_dir_content("./", pattern="*.py")))
# This works
```

This is also valid if you want to order, shuffle or slice the list of files.

## Inspiration

This code is inspired by this StackOverflow [Question/Answer](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory).
