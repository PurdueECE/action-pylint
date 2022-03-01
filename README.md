# pylint Action

This action will run pylint in the specified directory.

# Usage
```yaml
- uses: PurdueECE/action-pylint@main
  with:
    # Path to be linted
    # Default: .
    path: ''
```

# Testing
To run the action locally, you must install the [`act`](https://github.com/nektos/act) command line tool.
## Local Testing
To test a local version of the action, run the following command:
`act -W .github/workflows/test-local.yml`
## Integration Testing
To test the latest version pushed to `main`, run the following:
`act -W .github/workflows/test-integration.yml`