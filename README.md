# Fintech Hiring Trends in the US

Due to the changing business models of the financial organizations in the United States, a new breed of products colloquially known as Fintech have risen. This case study revolves around the growing trends in the recruitment in the technology domain in financial organizations. Financial organizations are using emerging technologies in the domain of Artificial Intelligence, Machine Learning and Data Science to gain new insights. These technologies have also given birth to evolving business models.

## Getting Started

The steps required to install and deploy the project in live system are as follows:

### Prerequisites

To begin with we need to install python 2.x/3.x in our local system and add it to our classpath.Some python packages are also needed for deployment

```
Python packages:

pandas
numpy
selenium
pdfminer
re
xlrd
openpyxl
collections
operator
csv
urllib
nltk
luigi

```

```
Docker

Before attempting to install Docker from binaries, be sure your host machine meets the prerequisites:

A 64-bit installation
Version 3.10 or higher of the Linux kernel. The latest version of the kernel available for your platform is recommended.
iptables version 1.4 or higher
git version 1.7 or higher
A ps executable, usually provided by procps or a similar package.
XZ Utils 4.9 or higher
A properly mounted cgroupfs hierarchy; a single, all-encompassing cgroup mount point is not sufficient


```

### Installing

Following steps are required to install necessary packages

Install python packages mentioned above using pip command

```
pip install <package_name>
```

Install docker for different categories of operating systems

```
Docker installation for Mac
•	https://docs.docker.com/docker-for-mac/
•	https://docs.docker.com/docker-for-mac/install/



Docker installation for Ubuntu
•	https://docs.docker.com/install/linux/docker-ce/ubuntu/


Docker installation for Windows
•	https://docs.docker.com/docker-for-windows/
•	https://docs.docker.com/docker-for-windows/install/

```

## Executing  Docker File

```
docker run heminjoshi/fintech_hiring_us
```


## Built With

* [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) - Code editor used for python
* [Docker](https://docs.docker.com/) - Used for packaging application  with its dependencies and libraries
* [Luigi](https://luigi.readthedocs.io/en/stable/) - Python module used to generate complex pipelines for batch processing of jobs.

## Authors

* **Ami Vora** 
* **Juhi Pareek** 
* **Aditya Soni** 
* **Hemin Joshi** 
