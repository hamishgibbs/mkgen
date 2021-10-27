# mkgen

![Tests](https://github.com/hamishgibbs/mkgen/actions/workflows/tests.yml/badge.svg)

*Automated research automation.*

## Overview

`mkgen` is a tool for automatically creating an automated build pipeline while supporting a variety of coding patterns, project structures, and programming languages.

**Research Automation**

`mkgen` simplifies the creation of an automated build pipeline for research projects by linking individual code files with their input and output dependencies.

Why an automated build pipeline? Conducting research requires interactive development to explore data and make sure that things are working properly. Once you are done with interactive development, it is helpful to have a single `entrypoint` where you can run all of the code in your project as an automated pipeline.

The problem with defining this pipeline manually is that your code can evolve - meaning you need to keep track of your code itself and the code that you have used to create your pipeline.

`mkgen` makes creating and updating your build pipeline automatic, so that changes to source code are always reflected in the build pipeline.

**Dependency Tracking**

`mkgen` relies on GNU Make to generate an automated build pipeline. Using Make means that all of the files in your project are managed in a "dependency tree".

## Limitations

`mkgen` relies on parsing files and cannot actually understand what your code is doing.
`mkgen` assumes a flexible coding pattern with inputs defined at the top of a script and outputs defined at the bottom of a script.

## Project Structure

## Usage

`# -- mkgen ignore --`

## How it works

## Contributions
