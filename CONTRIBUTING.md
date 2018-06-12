# Contributing to libdistrict

## Install
 * [Python3](https://www.python.org/downloads/)
 * [GDAL](https://pypi.python.org/pypi/GDAL)
 * [setuptools](https://packaging.python.org/guides/installing-using-linux-tools/) 

## Setup
 * GitHub: Fork a copy of this repository
 * Locally: `git clone <clone_url_for_fork>`
 * Locally: Add the canonical copy as a remote repo `git remote add canonical https://github.com/PlanScore/libdistrict.git` 

## Contributing Your Changes
 * Locally: Push your changes to your fork `git push origin <your_branch_name>`
 * GitHub: Create a pull request from the forked repository to the canonical master branch
 * GitHub: The pull request will be reviewed prior to merging

## Getting Others' Contributions
 * Locally: `git pull canonical master`

## Run Tests
 * Locally: `python3 setup.py test`
 
## Resources
 * Open source forking workflow: [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
 * More details on feature branching: [Scott's Weblog](https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/)
