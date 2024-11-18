# Reformatting code

## The original file

```python
def is_unique(
			s
			):
	s = list(s
				)
	s.sort()


	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			return 0
	else:
		return 1


if __name__ == "__main__":
	print(
		is_unique(input())
		)
```

## The ruff invocation

You can perform a dry-run to see whether the file will be reformatted


```bash
$ ruff format --check sample.py
Would reformat: sample.py
1 file would be reformatted

$ ruff format sample.py
1 file reformatted
```

### After reformatting
```python3
def is_unique(s):
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1


if __name__ == "__main__":
    print(is_unique(input()))
```

---
# Running the linter

## With default options 

```bash
$ ruff check sample.py
All checks passed!
```

## Selecting ALL of the rules
```bash
$ ruff check --select ALL sample.py
warning: `one-blank-line-before-class` (D203) and `no-blank-line-before-class` (D211) are incompatible. Ignoring `one-blank-line-before-class`.
warning: `multi-line-summary-first-line` (D212) and `multi-line-summary-second-line` (D213) are incompatible. Ignoring `multi-line-summary-second-line`.
sample.py:1:1: D100 Missing docstring in public module
sample.py:1:5: ANN201 Missing return type annotation for public function `is_unique`
  |
1 | def is_unique(s):
  |     ^^^^^^^^^ ANN201
2 |     s = list(s)
3 |     s.sort()
  |
  = help: Add return type annotation: `int`

sample.py:1:5: D103 Missing docstring in public function
  |
1 | def is_unique(s):
  |     ^^^^^^^^^ D103
2 |     s = list(s)
3 |     s.sort()
  |

sample.py:1:15: ANN001 Missing type annotation for function argument `s`
  |
1 | def is_unique(s):
  |               ^ ANN001
2 |     s = list(s)
3 |     s.sort()
  |

sample.py:8:5: PLW0120 [*] `else` clause on loop without a `break` statement; remove the `else` and dedent its contents
  |
6 |         if s[i] == s[i + 1]:
7 |             return 0
8 |     else:
  |     ^^^^ PLW0120
9 |         return 1
  |
  = help: Remove `else`

sample.py:13:5: T201 `print` found
   |
12 | if __name__ == "__main__":
13 |     print(is_unique(input()))
   |     ^^^^^ T201
   |
   = help: Remove `print`

Found 6 errors.
[*] 1 fixable with the `--fix` option (2 hidden fixes can be enabled with the `--unsafe-fixes` option).
```

## Determining the fix

```bash
$ ruff rule D103
```

# undocumented-public-function (D103)

Derived from the **pydocstyle** linter.

## What it does
Checks for undocumented public function definitions.

## Why is this bad?
Public functions should be documented via docstrings to outline their
purpose and behavior.

Generally, a function docstring should describe the function's behavior,
arguments, side effects, exceptions, return values, and any other
information that may be relevant to the user.

If the codebase adheres to a standard format for function docstrings, follow
that format for consistency.

## Example
```python
def calculate_speed(distance: float, time: float) -> float:
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```

Use instead (using the NumPy docstring format):
```python
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Parameters
    ----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.

    Returns
    -------
    float
        Speed as distance divided by time.

    Raises
    ------
    FasterThanLightError
        If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```

Or, using the Google docstring format:
```python
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.

    Raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```

## Options
- `lint.pydocstyle.ignore-decorators`

## References
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
- [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
- [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
```
