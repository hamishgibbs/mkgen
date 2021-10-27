# mkgen

![Tests](https://github.com/hamishgibbs/mkgen/actions/workflows/tests.yml/badge.svg)

`mkgen` is a tool for automatically creating an automated build pipeline for research projects.

## Overview

Conducting research requires interactive development to explore data and get things working. Once you are done with interactive development, it is helpful to be able to run all of the code in your project as an automated pipeline. `mkgen` creates and updates your build pipeline automatically, so that changes to source code are always reflected in the pipeline.

`mkgen` relies on [GNU Make](https://www.gnu.org/software/make/). Using Make means that all of the files in your project are related to each other in a "dependency tree." This makes build times faster for minor changes and means that changes to one file are propagated to any other files that depend on it.

## Usage

`mkgen` requires two files to automatically create a build pipeline:
  * `mkgen.json`: a configuration file.
  * `Makefile`: a `Makefile` with formatted comments showing `mkgen` where to write new targets.

To start using `mkgen`, create and enter a new directory and run:

```
mkgen init
```

This will create a `mkgen.json` file and a new `Makefile`. If you are starting with an existing project, `mkgen init` will update your `Makefile` with `mkgen` annotations.

*Note: you may have to alter the defaults in the `Makefile` and `mkgen.json` files depending on the configuration of your project.*

Run `mkgen` with:

```
mkgen
```

This will parse the files in your project and generate makefile targets for each file.

`mkgen` creates a default target for each file, allowing you to make targets by their file names. For a file named `src/plot.R`, you would call:

```
make plot
```

## mkgen.json

The `mkgen.json` file allows you to specify configurations for the programming languages and project structure that you would like to parse.

**languages:** *An array of programming language options.*
  * `name`: *The name of the programming language.*
  * `extensions`: *File extensions for this programming language.*
  * `interpreter`: *The name of the interpreter variable to include in Makefile targets.*

**src_paths**: *An array of file paths to parse in your project. Default: `src`.*

## Limitations

The goal of `mkgen` is to automatically construct Makefile targets while remaining flexible to different code patterns, project structures, and programming languages.

`mkgen` relies on recognising file paths using a regular expression. It cannot actually understand what your code is doing.
`mkgen` assumes that inputs are read in at the top of a file and that outputs are written at the bottom of a file. This is sufficient for a variety of coding patterns but `mkgen` will not be suitable for all development patterns.

## Contributions

Contributions are welcome. Please [open an issue](https://github.com/hamishgibbs/mkgen/issues/new).
