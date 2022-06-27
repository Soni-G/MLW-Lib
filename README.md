# MLWLIB


[![codecov](https://codecov.io/gh/SoftwareAG/nyoka/branch/master/graph/badge.svg)](https://codecov.io/gh/SoftwareAG/nyoka)
[![license](https://img.shields.io/github/license/softwareag/nyoka.svg)](https://github.com/softwareag/nyoka/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://pypi.org/project/nyoka/)


## Overview

Mlwlib is a python library which acts a connector between Machine Learning Workbench(MLW) and Jupyter Enteprise Gateway(JEG). Using Mlwlib, users can list all the projects in a MLW tenant, list all resources in a project, upload and download resources from & to a project etc.

The main purpose of this library is to allow users to do file transfer between MLW & JEG.

Wheel file for Mlwlib is available at **[Mlwlib Wheel](https://github.com/SoftwareAG/c8y-docs/tree/develop/static/files/zementis)**.


  

## Prerequisites

* Python >= 3.6

## Dependencies

mlwlib requires:

* pandas
 
## Installation

You can install mlwlib using: 

```python
pip install git+https://github.com/Soni-G/MLW-Lib.git#egg=mlwlib
```
## Usage

The main module of __Mlwlib__ is `mlwlib`. To use it you need to first import MLWClient, and create a MLWclient object. Creating a MLWClient objet will prompt for mlw userId & password. Eg:

```python
# import MLWClient class from mlw
from mlwlib.mlw import MLWClient

# create a mlw client object to get all projects in a mlw 
# tenant, pass mlw tenant url as parameter

client_obj = MLWClient("https://mlw.tenant.url")
```

MLWClient class contains below functions:


| Function | description |
|--|--|
| **list_projects** | _lists all projects in a mlw tenant_ |
| **project** | _creates a project class object_ |

### list_projects
To list all projects in a mlw tenant, create a _MLWClient_ class object with the tenant url as parameter. Then, use this object to call list_projects function.
This function supports two parameters:
- **show_all_attributes=True/False**  _# shows all attributes of existing projects if True. Else, shows only project name & id by default or if False._
- **show_json=True/False** _# shows list of projects in json format if True. Else, shows in dataframe format by default or if False._

Eg: 

```python
from mlwlib.mlw import MLWClient

client_obj = MLWClient("https://mlw.tenant.url")

# get list of projects in a mlw tenant
# optional parameters:
# show_json=True/False
# show_all_attributes = True/False
client_obj.list_projects(show_all_attributes=False, show_json=False)
```
### project object
To do any file operation in a mlw project, you need to first create a project class object, by calling _project_ function from _MLWClient_ class object with project name as a parameter.
The function expect one parameter:
- **project_name="name_of_mlw_project"**  _# name of project existing in mlw tenant._


Eg: 

```python
from mlwlib.mlw import MLWClient

client_obj = MLWClient("https://mlw.tenant.url")

# create a project object to list, upload or download files from/to a mlw project
# pass project name as a parameter to create object for each project
proj_obj = client_obj.project('MLW Project Name')
```

Project class object contains below functions:

| Function | description |
|--|--|
| **list_resources** | _lists all resources in a mlw project_ |
| **download_resource** | _downloads a resource from project_ |
| **upload_resource** | _uploads a resource to a project_ |

### list_resources
To list all resources in a mlw project, create a _project_ class object with the project name as parameter. Then, use this object to call list_resources function.
This function supports two parameters:
- **show_all_attributes=True/False**  _# shows all attributes of existing resources if True. Else, shows only resource id, name, size, type & extension by default or if False._
- **show_json=True/False** _# shows list of resources in json format if True. Else, shows in dataframe format by default or if False._

Eg: 

```python
from mlwlib.mlw import MLWClient

client_obj = MLWClient("https://mlw.tenant.url")
resourcesproj_obj = client_obj.project('MLW Project Name')

# fetch all resources in a project
# optional parameters:
# show_json=True/False
# show_all_attributes = True/False
proj_obj.list_resources(show_json=False, show_all_attributes=False)
```

### download_resource
To download a resource from a mlw project, create a _project_ class object with the project name as parameter. Then, use this object to call download_resource function.
This function expects one parameter:
- **resource_name="name of resource"**  _# name of resource which needs to be downloaded from mlw project._


Eg: 

```python
from mlwlib.mlw import MLWClient

client_obj = MLWClient("https://mlw.tenant.url")
proj_obj = client_obj.project('MLW Project Name')

# Download a resource from a mlw project
# use method download_resource() from Project class object
# pass resource_name as a parameter which is to be downloaded
proj_obj.download_resource("samplefile.csv")
```

### upload_resource
To upload a resource to a mlw project, create a _project_ class object with the project name as parameter. Then, use this object to call upload_resource function.
This function expects one parameters:
- **resource_path="path of resource"**  _# path of resource which needs to be uploaded to mlw project._


Eg: 

```python
from mlwlib.mlw import MLWClient

client_obj = MLWClient("https://mlw.tenant.url")
proj_obj = client_obj.project('MLW Project Name')

# Upload a resource to a mlw project
# use method upload_resource() from Project class object
# pass resource_path as a parameter
proj_obj.upload_resource("path/to/the/file/filename.csv")
```

## Uninstallation

```
pip uninstall mlwlib
```

## Support

You can get email support at:

*  ai-dev@softwareag.com by sending your queries

-----
