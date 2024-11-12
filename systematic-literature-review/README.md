# Getting started

## Config a virtual enviroment

First of all make sure you have a virtual enviroment configured.

```shell
pip install virtualenv
```

Create a virtual enviroment:

```shell
virtualenv .venv
```

Activate the virtual enviroment

```shell
source .venv/bin/activate
```

When you’re finished working in the project, you can deactivate the virtual environment to return to your general system Python environment by typing:

```shell
deactivate
```

## Install required libraries

First install pip-tools, then we can compile our requirements:

```shell
pip install pip-tools
```

Install the requirements:

```shell
pip-compile requirements.in
```

The next step is to install the dependencies listed in your requirements file in your virtual environment. Because the package versions are pinned, installing them is as easy as:

```shell
pip install -r requirements.txt
```

# References:

1. [Production Jupyter notebooks: A guide to managing dependencies, data, and secrets for reproducibility](https://blog.reviewnb.com/jupyter-notebook-reproducibility-managing-dependencies-data-secrets/)
2. [Scholar BibTex, Github project](https://github.com/Kildrese/scholarBibTex)
