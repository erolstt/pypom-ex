# A basic example to show how to use PYPOM

### Installing dependencies
You need to install the Python packages that are needed to run tests using pip. In a
terminal, from the the project root, execute the following command:

```bash
$ pip install -Ur requirements.txt
```

### Running the tests
To run all of the tests against the default environment:

```bash
$ py.test --driver Firefox
```

If you would like to generate HTML report for the test result, run the following command

```bash
$ py.test --driver Firefox --html=report.html
```
