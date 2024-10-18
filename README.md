Repo to support https://github.com/astral-sh/uv/issues/8302#issue-2595521584

## Overview

- [x]  tests for each app/lib
- [x]  ability to run tests in a "synced" environment for each particular app/lib
- [ ] add coverage for each app/lib
- [x] support testing interface in vscode
- [ ] support devcontainer in vscode
- [ ] support docker containerization for the apps
- [x] maybe exploit vscode workspaces


### How to

Run commands in `Makefile`, e.g. `make test` which will run all tests in isolated environments and return with error if at least one fails.

### Current issues

Tests in `http-backend` fails since the fastapi application can't be imported in the test for some reason