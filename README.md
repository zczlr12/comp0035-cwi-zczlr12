[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12237636&assignment_repo_type=AssignmentRepo)
# COMP0035 2023-24 Coursework

Use this README.md to explain to the markers how to set up your project for COMP0035 coursework 1 and coursework 2.

The project structure follows
the ['Tests as part of the application code'](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#tests-as-part-of-application-code)
structure. This is to make it easier for you to submit a single folder for the coursework.

Do not delete, move or rename the following files and folders:

- `LICENSE`
- `README.md`
- `.gitignore`
- `pyproject.toml`
- `requirements.txt`
- `src/__init__.py`
- `src/coursework1` and the files within it: `__init__.py`,`data_prep.py`
- `src/coursework2` and the files within it: `__init__.py`,`employee.py`
- `src/coursework2/tests` and the files within it: `__init__.py`,`test_code.py`, `test_employee.py`

## Coursework 1

I cloned the project from GitHub to VS Code after accepting the GitHub classroom assignment.

With the opened project in VS Code, I entered `py -m venv .venv` in the terminal to create a virtual environment and used `.\.venv\Scripts\activate` to activate that virtual environment.

As coursework 1 requires matplotlib for data exploration, I added this library to the original `requirement.txt` file before installing the dependencies using `pip install -r requirements.txt`.

As the `.gitignore` file originally includes VS Code and virtual environments, there is no need to further modify it.

More information of this project is shown in `./src/coursework1/coursework1.md`
