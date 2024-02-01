# example-python
An example repository to demonstrate Python support in Pants.

See [pantsbuild.org](https://www.pantsbuild.org/docs) for much more detailed documentation.

This is only one possible way of laying out your project with Pants. See 
[pantsbuild.org/docs/source-roots#examples](https://www.pantsbuild.org/docs/source-roots#examples) for some other
example layouts.

# Running Pants

You run Pants goals using the `pants` launcher binary, which will bootstrap the
version of Pants configured for this repo if necessary.

See [here](https://www.pantsbuild.org/docs/installation) for how to install the `pants` binary.

> :question: Running with Apple Silicon and/or macOS? You will want to make changes to the `search_path` and
`interpreter_constraints` values in `pants.toml` before running `pants` - there is guidance in `pants.toml`
for those settings.

Use `pants --version` to see the version of Pants configured for the repo (which you can also find
in `pants.toml`).

# Goals

Pants commands are called _goals_. You can get a list of goals with

```
pants help goals
```

# Targets

Targets are a way of setting metadata for some part of your code, such as timeouts for tests and 
entry points for binaries. Targets have types like `python_source`, `resources`, and 
`pex_binary`. They are defined in `BUILD` files.

Pants goals can be invoked on targets or directly on source files (which is often more intuitive and convenient).
In the latter case, Pants locates target metadata for the source files as needed.

## File specifications

Invoking goals on files is straightforward, e.g.,

```
pants test helloworld/greet/greeting_test.py
```

You can use globs:

```
pants lint helloworld/greet/*.py
```

But note that these will be expanded by your shell, so this is equivalent to having used

```
pants lint helloworld/greet/__init__.py helloworld/greet/greeting.py helloworld/greet/greeting_test.py
```

If you want Pants itself to expand the globs (which is sometimes necessary), you must quote them in the shell:

```
pants lint 'helloworld/greet/*.py'
```

You can run on all changed files:

```
pants --changed-since=HEAD lint
```

You can run on all changed files, and any of their "dependees":

```
pants --changed-since=HEAD --changed-dependees=transitive test
```

## Target specifications

Targets are referenced on the command line using their address, of the form `path/to/dir:name`, e.g.,

```
pants lint helloworld/greet:lib
```

You can glob over all targets in a directory with a single trailing `:`, or over all targets in a directory
and all its subdirectories with a double trailing `::`, e.g.,

```
pants lint helloworld::
```
