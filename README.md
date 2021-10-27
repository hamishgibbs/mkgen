# mkgen

![Tests](https://github.com/hamishgibbs/mkgen/actions/workflows/tests.yml/badge.svg)

*Automated research automation.*

Generate makefile targets from source code files.

## Overview

`mkgen` is a tool for automatically creating an automated build pipeline while supporting a variety of coding patterns, project structures, and programming languages.

**Research Automation**

`mkgen` simplifies the creation of an automated build pipeline for research projects by linking individual code files with their input and output dependencies.

Why an automated build pipeline? Conducting a research project requires interactive development to explore data and make sure that things are working properly. Once you are done with interactive development, it is helpful to have a single `entrypoint` where you can run all of the code in your project as a pipeline.

The problem with defining this `entrypoint` manually is that your code can evolve - meaning you need to keep track of your code itself and the code you have used to create your pipeline.

**Dependency Tracking**

`mkgen` relies on GNU Make to generate an automated build pipeline. Using Make means that all of the files in your project are managed in a "dependency tree". Make can identify which files depend on which other files and update dependencies accordingly.  

## Limitations

## Project Structure

## Usage

**Higher Level Targets**

## How it works

## Contributions
