# mkgen

![Tests](https://github.com/hamishgibbs/mkgen/actions/workflows/tests.yml/badge.svg)

`mkgen` is a tool for automatically creating an automated build pipeline for research projects.

## Overview

Conducting research requires interactive development to explore data and get things working. Once you are done with interactive development, it is helpful to be able to run all of the code in your project as an automated pipeline. `mkgen` creates and updates your build pipeline automatically, so that changes to source code are always reflected in the pipeline.

`mkgen` relies on [GNU Make](https://www.gnu.org/software/make/). Using Make means that all of the files in your project are related to each other in a "dependency tree." This makes build times faster for minor changes and means that changes to one file are propagated to any other files that depend on it.

## Installation

Install `mkgen` from GitHub with `pip`:

```
pip install git+https://github.com/hamishgibbs/mkgen.git
```

## Usage

`mkgen` requires two files to automatically create a build pipeline:
  * `mkgen.json`: *a configuration file.*
  * `Makefile`: *a `Makefile` with formatted comments showing `mkgen` where to write generated targets.*

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

## mkgen.json

The `mkgen.json` file allows you to specify configurations for the programming languages and project structure that you would like to parse.

**languages:** *An array of programming language options.*
  * `name`: *The name of the programming language.*
  * `extensions`: *File extensions for this programming language. R defaults: `[".r", ".R"]`, Python defaults: `[".py"]`*
  * `interpreter`: *The name of the interpreter variable to include in Makefile targets. R default: `$(R)`, Python default: `$(PYTHON)`*

**src_paths**: *An array of directories to parse in your project. Default: `["src"]`.*

## How it works

`mkgen` detects file paths in source code and constructs Makefile targets based on the assumption that inputs tend to be at the top of a script and outputs tend to be at the bottom.

Consider a target generated from a file located at `src/plot.R`:

*src/plot.R*
```r
require(readr)
require(ggplot2)

data <- read_csv("path/to/input/data.csv")

data$y = data$y * 7

p <- data %>%
  ggplot() +
  geom_path(aes(x=x, y=y))

ggsave(p,
       "output/path/to/fig.png")  
```

`mkgen` will extract the input and output file paths from this script and construct the makefile target:

*Makefile*
```shell
plot: output/path/to/fig.png

output/path/to/fig.png: src/plot.R \
    path/to/input/data.csv
  $(R) $^ $@
```

Now, the script `src/plot.R` is connected to the `output/path/to/fig.png` and `path/to/input/data.csv` files. Run `make plot` to construct the plot.

## Limitations

The goal of `mkgen` is to automatically construct Makefile targets while remaining flexible to different code patterns, project structures, and programming languages.

1. `mkgen` relies on recognising file paths using a regular expression. It cannot extract file dependencies specified by or within functions.
2. `mkgen` assumes that inputs are read in (roughly) at the top of a file and that outputs are written around the bottom of a file. This assumption can accommodate a range of development patterns but will not be suitable for all developers or projects.

*Note: You can use the comment: `# -- mkgen ignore --` if you would like `mkgen` to ignore a specific file when parsing your project.*

## Contributions

Contributions are welcome. If you find a bug or would like to contribute, please [open an issue](https://github.com/hamishgibbs/mkgen/issues/new).
