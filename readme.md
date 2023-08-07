# Introduction
This project is built to visulize the forest fire occurence across jurisdiction since 1990. The datasets are obtained from Canadian Council of Forest Ministers - Conseil canadien des ministres des forêts [DOI](http://doi.org/10.5281/zenodo.3690046).

## Access online
You can access the app from [here](https://github.com/ChengguiSun/Canada_wildfire/blob/main/stApp/mul_pages/burned_area.py)

# Setup
The sample commands is based on Windows. Please update the commands accordingly for other OS.

## prequirement
Python 3.9+

## Setup project
1. clone the project `git clone https://github.com/ChengguiSun/Canada_wildfire.git`
2. cd project folder `cd Canada_wildfire`
3. setup python virtual env `python -m venv .venv`
4. activate virtual env `env/Scripts/activate`
5. install required package `pip install -r requirements.txt`
6. Start web server `streamlit run stApp/mul_pages/app.py`
7. open browser and access [http://localhost:8080/](http://localhost:8080/)
