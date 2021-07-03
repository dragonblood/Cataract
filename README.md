# Under Construction
# Cataract [![Build and deploy Python app to Azure Web App - cataract](https://github.com/dragonblood/Cataract/actions/workflows/master_cataract.yml/badge.svg)](https://github.com/dragonblood/Cataract/actions/workflows/master_cataract.yml)
## 1. About:

A Neumorphic WebApp which allows users to analysis an upload image hosted on azure.

## 2. Steps To Follow:

### Conda
```
git clone https://github.com/dragonblood/Cataract.git
cd Cataract
conda env create --file cataract.yml
conda activate cataract
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### ~~~~~~~ OR ~~~~~~~

### PIP
```
git clone https://github.com/dragonblood/Cataract.git
cd Cataract
pipenv shell
pipenv install
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 3. Screenshots
| Screens |
|----------------|
|Initial|
|<img src="https://github.com/dragonblood/Cataract/blob/master/screenshots/initial.png"/>|
|Upload|
|<img src="https://github.com/dragonblood/Cataract/blob/master/screenshots/upload.png"/>|
|Results|
|<img src="https://github.com/dragonblood/Cataract/blob/master/screenshots/results.png"/>|

## 4. TODO
- [x] Put user uploaded images to bucket
- [ ] Auto Delete some stuff after use
- [x] Modify and display results to user
- [x] Upload Screenshots
- [x] create cataract.yml and requirements.txt
- [ ] Add automatic magic code .vscode folder

### Please Feel Free to raise an issue.
### Take Permission Before using it in your work.

