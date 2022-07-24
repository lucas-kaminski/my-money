import os

os.system("black src")

os.system("sql-formatter *.sql")

# TODO: Format HTML, CSS and JS files

flake8_options = [
    "--ignore='E501,E402,W503'",
    "--per-file-ignores='src/main.py:F401'",
    "src",
]
flake8_command = "flake8 " + " ".join(flake8_options)
flake8_output = os.popen(flake8_command).read()
if flake8_output:
    print("PEP8 violations found, must resolve before continuing.")
    print(flake8_output)
    exit(1)
