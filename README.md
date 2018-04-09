# libdistrict

libdistrict is a free open source metrics library created to help developers, researchers, and policy-makers evaluate district plans. This library is developed with input from [PlanScore](https://www.planscore.org) and [Azavea](https://www.azavea.com).

## Build and Run

### Install
 * [Python3](https://www.python.org/downloads/)
 * [GDAL](https://pypi.python.org/pypi/GDAL)
 * [setuptools](https://packaging.python.org/guides/installing-using-linux-tools/)

### Run tests
 * Locally: `python3 setup.py test`

### Build Wheel
 * Locally: `python3 setup.py bdist_wheel`

### Install libdistrict
 * Add .whl file to directory where you would like to use libdistrict
 * Activate virtual environment
 * Install libdistrict in virtual environment: `pip install <wheel_name>.whl`

### Uninstall libdistrict before installing new version of libdistrict
 * Activate virtual environment
 * Uninstall libdistrict from virtual environment: `pip uninstall libdistrict`

### Virtual environment setup, activation, and deactivation
 * Setup: `virtualenv -p /usr/bin/python3 env`
 * Activate: `. env/bin/activate`
 * Deactivate: `deactivate`


## Contributing

### Setup
 * GitHub: Fork a copy of this repository
 * Locally: `git clone <clone_url_for_fork>`
 * Locally: Add the canonical copy as a remote repo `git remote add canonical https://github.com/PlanScore/libdistrict.git` 

### Contributing Your Changes
 * Locally: Push your changes to your fork `git push origin <your_branch_name>`
 * GitHub: Create a pull request from the forked repository to the canonical master branch
 * GitHub: The pull request will be reviewed prior to merging

### Getting Others' Contributions
 * Locally: `git pull canonical master`
 
### Resources
 * Open source forking workflow: [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
 * More details on feature branching: [Scott's Weblog](https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/)
