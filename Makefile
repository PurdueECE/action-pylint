ACT = act

test_empty:
	$(ACT) -W test_integration/test_empty.yml

test_valid:
	$(ACT) -W test_integration/test_valid.yml

test_invalid:
	$(ACT) -W test_integration/test_invalid.yml

test: test_empty test_valid test_invalid