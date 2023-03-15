
# Breezy Briefs

Breezy Briefs is a webapp to get Brief Summary of a  YouTube Video based on its captions/subtitles.
The URL of the youtube video or the video Id is required to get the breif summary.


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Features (WIP)

- Get Brief summary of the youtube video.
- Default language is English but other languages are possible if subtitles are available. 


## Run Locally

Clone the project

```bash
  git clone https://github.com/shivamnaik39/breezy_briefs
```

Go to the project directory

```bash
  cd breezy_briefs
```

Install dependencies (using pipenv)

```bash
  pipenv install

  # for development
  pipenv install --dev
```

Install dependencies using pip  (pipenv recommended )

```bash
 pip install -r ./requirements.txt
```

Activate the Virtual Environment 

```bash
 pipenv shell
```

Run the program

```bash
pipenv run start

# for development
pipenv run dev
```

## API Documentation

```bash
# Swagger
http://localhost:8000/docs


# Redoc
http://localhost:8000/redoc

```



## Roadmap

- Add a GUI frontend



## Authors

- [@shivamnaik39](https://www.github.com/shivamnaik39)
- [@grishmakadam](https://github.com/grishmakadam)
