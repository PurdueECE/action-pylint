test_valid:
	act -W test/valid/.github/workflows

test_invalid:
	act -W test/invalid/.github/workflows

test: test_valid test_invalid