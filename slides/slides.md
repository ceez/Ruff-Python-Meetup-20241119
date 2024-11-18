### Ruff: A Modern Python Linter

Chris Cowan - Nov 19, 2024



#### What is Ruff?
- A fast, extensible Python linter and code formatter.
- Written in Rust for maximum performance.
- Designed to enforce Python coding standards and find errors in your code.
- Supports linting, formatting, and autofixes in one tool.



#### Key Features
- Up to 100x faster than traditional linters like Flake8 or pylint.
- Integrates functionality of tools like Flake8, isort, pyupgrade, and more.
- Highly customizable with fine-grained rule configuration.
- Automatically fixes many issues (e.g., formatting, imports).


#### Key Features (cont.)
- Supports over 800 lint rules, including best practices, style, and security.
- Runs standalone and does not rely on Python for execution.



#### Installation and Setup
#### Install
```bash
$ pip install ruff

$ brew install ruff # On MacOS without python preinstalled
```


#### Usage
```bash
$ ruff --help
```
```text
Ruff: An extremely fast Python linter and code formatter.

Usage: ruff [OPTIONS] <COMMAND>

Commands:
  check    Run Ruff on the given files or directories
  rule     Explain a rule (or all rules)
  config   List or describe the available configuration options
  linter   List all supported upstream linters
  clean    Clear any caches in the current directory and any subdirectories
  format   Run the Ruff formatter on the given files or directories
  server   Run the language server
  analyze  Run analysis over Python source code
  version  Display Ruff's version
  help     Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version

Log levels:
  -v, --verbose  Enable verbose logging
  -q, --quiet    Print diagnostics, but nothing else
  -s, --silent   Disable all logging (but still exit with status code "1" upon detecting
                 diagnostics)

Global options:
      --config <CONFIG_OPTION>  Either a path to a TOML configuration file
                                (`pyproject.toml` or `ruff.toml`), or a TOML `<KEY> =
                                <VALUE>` pair (such as you might find in a `ruff.toml`
                                configuration file) overriding a specific configuration
                                option. Overrides of individual settings using this option
                                always take precedence over all configuration files,
                                including configuration files that were also specified
                                using `--config`
      --isolated                Ignore all configuration files

For help with a specific command, see: `ruff help <command>`.
```


#### Configuration

- Config in 'pyproject.toml' or 'ruff.toml'
  - https://docs.astral.sh/ruff/configuration/

- Sample pyproject.toml file:

```toml
[tool.ruff]
line-length = 88
select = ["E", "F"]
exclude = ["migrations"]
```


#### Integrations
- Editors and IDEs
  - https://docs.astral.sh/ruff/editors/setup/
- CI/CD
  - https://docs.astral.sh/ruff/integrations/



#### Challenges with Ruff
- Less flexible for highly customized linting needs.
- Requires Rust for local builds, which may be unfamiliar to some Python developers.
- Fast-evolving tool; staying current may be a challenge for large teams.



#### Looking into the Crystal Ball
- Continued expansion of supported rules and integrations.
- More autofix capabilities.
- Community-driven features and contributions. Request new features from the GitHub repository



#### Resources
- Home Pages and Docs::
  - [https://astral.sh](https://astral.sh)
  - [https://ruff.rs](https://ruff.rs)
  - [https://docs.astral.sh/ruff/](https://docs.astral.sh/ruff/)
- GitHub Repo:
  - [https://github.com/astral-sh/ruff](https://github.com/astral-sh/ruff)
- Playground:
  - [https://play.ruff.rs/](https://play.ruff.rs)
- Test Cases:
  - [https://github.com/pylint-dev/pylint/tree/main/tests](https://github.com/pylint-dev/pylint/tree/main/tests)
