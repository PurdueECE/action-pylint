# pylint Action

This action will run pylint in the specified directory.

# Usage
```yaml
- uses: PurdueECE/action-pylint@v1.2
  with:
    # Args to send to pylint command
    args: -v test_data/empty
```

# Testing
Test cases are contained in the `test/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.