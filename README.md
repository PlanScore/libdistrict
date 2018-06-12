# libdistrict

libdistrict is a free open source metrics library created to help developers, researchers, and policy-makers evaluate district plans. This library is developed with input from [PlanScore](https://www.planscore.org) and [Azavea](https://www.azavea.com).

## Contributing
Read the [contribution guidlines](CONTRIBUTIONS.md) for libdistrict. 

## Getting Started
libdistrict is a Python 3 library. The library is not currently available on PyPI.

### Prerequisites
 * [Python3](https://www.python.org/downloads/)
 * [GDAL](https://pypi.python.org/pypi/GDAL)
 * [setuptools](https://packaging.python.org/guides/installing-using-linux-tools/)

### Install libdistrict

 1. Clone the libdistrict git repository
  * git clone https://github.com/PlanScore/libdistrict.git
 1. Build Wheel
  * `python3 setup.py bdist_wheel`
 1. Install libdistrict
  * `pip install <wheel_name>.whl
 1. Use the metrics in your project

