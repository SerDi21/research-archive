# Research Archive

Research Archive is a full-stack web application designed to store, manage, and search scientific publications.
It provides a simple interface to create, update, delete, and search research entries with a powerful search engine.

The project demonstrates how to build and deploy a modern application using containerized services.

---

## Tech Stack

**Frontend**

* React

**Backend**

* Flask

**Databases**

* PostgreSQL (primary data storage)
* Elasticsearch (full-text search)

**Infrastructure**

* Docker
* Docker Compose

---

## Features

* Create new research publications
* Update existing publications
* Delete publications
* Search publications using full-text search
* Basic filtering and search bar
* Containerized environment for easy deployment

---

## Getting Started

### Requirements

* Docker
* Docker Compose
* Git

---

### Clone the repository

```bash
git clone https://github.com/your-username/research-archive.git
cd research-archive
```

---

### Copy the environment file

```bash
cp .env.example .env
```

---

### Run the application

```bash
docker compose up --build
```

Docker will automatically:

* Build the backend and frontend images
* Start PostgreSQL
* Start Elasticsearch
* Load sample data into the database
* Start the web application

---

## Access the Application

Frontend:

```
http://localhost:5173
```

Backend API:

```
http://localhost:5000
```

Elasticsearch (optional):

```
http://localhost:9200
```

---

## Search Functionality

Search requests are processed using **Elasticsearch**, allowing full-text search across:

* Title
* Abstract
* Authors
* Keywords

The search engine returns matching publications which are displayed in the frontend interface.

---

## Sample Data

The project includes a small dataset automatically loaded at startup for testing purposes.

**Important:**
The publications included in the database are **synthetic example data generated for demonstration purposes only**.
They do **not correspond to real research papers, authors, or institutions.**

---

## Development

To rebuild containers after code changes:

```bash
docker compose up --build
```

To stop the application:

```bash
docker compose down
```

---

## Possible Improvements

Future improvements could include:

* Advanced search filters
* Authentication and user accounts
* Pagination
* Sorting by relevance or date
* Autocomplete search
* Highlighting search matches
* API documentation

---

## License

This project is provided for educational and demonstration purposes.
