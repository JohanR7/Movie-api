# MOVIE API BACKEND USING DJANGO

## Project Overview
This is a Django-based API project that integrates **TMDb (The Movie Database)** API to fetch movie data such as popular, top-rated, upcoming movies, and allows search, comparisons, and filtering based on user input. The application provides endpoints for these functionalities.

---

## How to Run the Application Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/movie-api-project.git
cd movie-api-project
```

### Step 2: Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure API Key
Create a `.env` file in the root directory and add your **TMDB API key**:
```env
my_api_key=your_tmdb_api_key_here
```

### Step 5: Set Up the Database
```bash
python manage.py migrate
```

### Step 6: Run the Application Locally
```bash
python manage.py runserver
```

---

## API Endpoints

### 1. **GET /popular/**
**Function:** Fetches a list of popular movies.
- **Parameters:**
  - `page` *(Optional)*: Page number to fetch. Default is 1.
- **Example Request:**
```bash
GET /popular/?page=1
```
- **Example Response:**
```json
{
  "page": 1,
  "total_results": 1000,
  "total_pages": 50,
  "results": [
    {
      "id": 12345,
      "title": "Movie Title",
      "release_date": "2024-01-01",
      "vote_average": 8.5
    }
  ]
}
```

### 2. **GET /top-rated/**
**Function:** Fetches a list of top-rated movies.
- **Parameters:** None.
- **Example Request:**
```bash
GET /top-rated/
```
- **Example Response:**
```json
{
  "top_movies": [
    {
      "id": 12345,
      "title": "Top Movie Title",
      "release_date": "2023-12-15",
      "vote_average": 9.5
    }
  ]
}
```

### 3. **GET /search/**
**Function:** Searches for movies based on the query provided.
- **Parameters:**
  - `query` *(Required)*: Search keyword or movie title.
  - `page` *(Optional)*: Page number. Default is 1.
- **Example Request:**
```bash
GET /search/?query=inception&page=1
```
- **Example Response:**
```json
{
  "page": 1,
  "total_results": 100,
  "total_pages": 5,
  "results": [
    {
      "id": 12345,
      "title": "Inception",
      "release_date": "2010-07-16",
      "vote_average": 8.8
    }
  ]
}
```

### 4. **GET /now-playing/**
**Function:** Fetches movies currently playing in theaters.
- **Parameters:**
  - `page` *(Optional)*: Page number. Default is 1.
- **Example Request:**
```bash
GET /now-playing/?page=1
```
- **Example Response:**
```json
{
  "page": 1,
  "total_results": 100,
  "total_pages": 5,
  "results": [
    {
      "id": 67890,
      "title": "Now Playing Movie",
      "release_date": "2024-01-01",
      "vote_average": 7.5
    }
  ]
}
```

### 5. **GET /upcoming/**
**Function:** Fetches upcoming movies.
- **Parameters:**
  - `page` *(Optional)*: Page number. Default is 1.
- **Example Request:**
```bash
GET /upcoming/?page=1
```
- **Example Response:**
```json
{
  "page": 1,
  "total_results": 50,
  "total_pages": 3,
  "results": [
    {
      "id": 54321,
      "title": "Upcoming Movie Title",
      "release_date": "2024-02-01",
      "vote_average": 8.0
    }
  ]
}
```

### 6. **GET /filter/**
**Function:** Fetches movies based on filters (genre, release year).
- **Parameters:**
  - `genre` *(Optional)*: Genre (e.g., Action, Drama).
  - `release_year` *(Optional)*: Release year.
  - `page` *(Optional)*: Page number.
- **Example Request:**
```bash
GET /filter/?genre=Action&release_year=2023&page=1
```
- **Example Response:**
```json
{
  "page": 1,
  "total_results": 10,
  "total_pages": 1,
  "results": [
    {
      "id": 98765,
      "title": "Action Movie",
      "release_date": "2023-05-15",
      "vote_average": 7.8
    }
  ]
}
```

### 7. **GET /compare/**
**Function:** Compares two movies.
- **Parameters:**
  - `movie1` *(Required)*: ID or title of the first movie.
  - `movie2` *(Required)*: ID or title of the second movie.
- **Example Request:**
```bash
GET /compare/?movie1=12345&movie2=67890
```
- **Example Response:**
```json
{
  "movie1": {
    "title": "Inception",
    "release_date": "2010-07-16",
    "vote_average": 8.8
  },
  "movie2": {
    "title": "Interstellar",
    "release_date": "2014-11-07",
    "vote_average": 8.6
  },
  "higher_vote_average": "Inception"
}
```

---

## How to Generate an API Key
1. Sign up on [TMDb](https://www.themoviedb.org/).
2. Generate an API key under the **API** section.
3. Add your key to the `.env` file:
```env
my_api_key=your_tmdb_api_key_here
