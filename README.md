This project is an internal reporting tool which takes log data of a database and calculates statistics from it. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Install

First of all, you have to install the following programms: 
1. [Python3](https://www.python.org/downloads)
2. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. [Vagrant](https://www.vagrantup.com/downloads.html)

### Setup the project
1. Download/Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
2. Download and unzip the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside ist called *newsdata.sql*.
3. Download/clone this repository and copy it with the *newsdata.sql* into Vagrant sub-directory in the *fullstack-nanodegree-vm* 

### Launching the Virtual Machine:
  1. Use your terminal and change the directory to the Vagrant sub-directory and use command `vagrant up` to set up vagrant
  2. Use `vagrant ssh` to log into Vagrant VM

### Run

1. Laod the data into localdatabase with the command: `psql -d news -f newsdata.sql`
2. Run the program with: `python log.py`

### Output

If the programm runs correctly, you will the the following output: 
```
THE 3 MOST POPULAR ARTICLE:
1 . Candidate is jerk, alleges rival - 338647 views
2 . Bears love berries, alleges bear - 253801 views
3 . Bad things gone, say good people - 170098 views

THE MOST POPULAR AUTHORS:
1 . Ursula La Multa - 507594 views
2 . Rudolf von Treppenwitz - 423457 views
3 . Anonymous Contributor - 170098 views
4 . Markoff Chaney - 84557 views

DAYS ON WHICH MORE THAN 1% OF REQUESTS LEAD TO ERROR:
1 . 2016-07-17 - 2.26 %
```

## Acknowledge

This project was built as part of the Udacity course "Fullstack Web Developer Nanodegree". 