#!/bin/sh

swift package init --name {{ cookiecutter.name }} --type library

make bootstrap
make fmt

git init
git add .
git commit -m "Initial commit"