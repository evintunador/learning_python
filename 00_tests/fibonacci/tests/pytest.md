`pytest tests`
or for a specific file
`pytest tests/test_fibonacci.py`
or a specific test to run
`pytest tests/test_fibonacci.py::test_fibonacci_values`
if one test failing results in a long list of tests failing, then rather than have all that annoying stuff print you can make pytest stop after the first test fail
`pytest -x tests`
it's normal to write your tests in increasing order of sophistication so that earlier tests are more likely to catch basic errors in the code