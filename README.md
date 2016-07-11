# A basic example to show how to use PYPOM

### Install dependencies
Install the Python packages that are needed to run tests using pip. In a
terminal, from the the project root, issue the following command:

```bash
$ pip install -Ur requirements.txt
```

### Run the tests
Tests are run using the command line. Below are a couple of examples of running
the tests:

To run all of the tests against the default environment:

```bash
$ py.test --driver Firefox
```

If you would like to generate HTML report for the test result:

```bash
$ py.test --driver Firefox --html=report.html
```
