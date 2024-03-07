
# Stori-QA-Automation-Challenge

This is a project to answer the challenge by the vacancy to QA Automation

The purpose is to demonstrate the capabilities to automate browsers on mobile devices applied to testing, using selenium and gherking language

## Table of Contents
- [Installation](##installation)
- [Run](##Run)

## Installation

We will need to install: 

- node
- appium
- python
- java
- Andorid Studio (*for emulator devices*)

To install node we access the official page https://nodejs.org/en
We select the environment in which we are working and install

To install appium:

```bash
  npm install -g appium
```
And nedd install the driver 
- UiAutomator2 
```bash
  appium device install uiautomator2
```
- Geckodriver
```bash
  appium device install gecko
```
    
To install python from the website https://www.python.org/ and download the latest version

The same way with java, access the oficial page https://www.java.com/en/download/

If we'll use emulator Android there is that install Andorid Studio from the oficial site https://developer.android.com/studio?hl=es-419


## Environment Variables

To run this project, you will need to add the following environment variables

`JAVA_HOME` -> **PATH/install/java**

`ANDROID_HOME` -> **PATH/intall/android_SDK**

`GECKO_DRIVER` -> **PATH/gecko_driver/in/the/system**


## Run

By run this project we need
1. locate us into the project folder with the next command

```bash
  cd path/the/project 
```
Example
```bash
  cd D:\Stori-QA-Automation-Challenge
```

2. Next create a new virtual environment 
```bash
  python -m venv env
```
And execute:
- Windows
```
  powerhell -> <env_folder>\Scripts\activate.ps1
  cmd - > <env_folder>\Scripts\activate.bat
```
- Linux y Mac OS
```
  source <env_folder>/Scripts/bin/activate
```
3. download the dependencies, to do we'll run the next command

```bash
  pip install -r requirements.txt
```
4. Finish the download we can execute the project with 
```bash
  path/the/project python .\run-py.py --browsername="<browsername>"
```
Example:
```bash
  D:\Stori-QA-Automation-Challenge python .\run-py.py --browsername="chome"

  D:\Stori-QA-Automation-Challenge python .\run-py.py --browsername="firefox"
```
If we omit the argument _**--browsername**_ the project will use the **Chrome Driver** by default

