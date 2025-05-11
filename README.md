# Pokémon Data Fetcher

## Description

This project retrieves Pokémon data from the PokéAPI and outputs it in JSON format. It's containerized with Docker and can be deployed to Kubernetes using the provided Helm chart.

## Contents

* **`pokemon_fetcher.py`**:  Python script to fetch Pokémon data.
* **`Dockerfile`**:  Instructions to build a Docker image for the application.
* **`helm-chart`**:  [Helm chart for deploying to Kubernetes.](https://github.com/arunkumardhanabal/pokemon-helm.git)
* **Docker Image**: `arun1771/pokemon:v1`

## Prerequisites

* Docker installed
* Python installed

## Instructions

**1.  To create a new docker image using given Dockerfile**

* Clone this repository.


        git clone https://github.com/arunkumardhanabal/pokemon-project.git


  
* Build the Docker image:

        
        docker build -t pokemon-app:v1.1 .
        
        
* Run the container, providing the Pokémon name as an argument:

  
        docker run pokemon-app:v1.1 python3 pokemon_fetcher.py ditto


**2.  To create a container using existing docker image**

* create a container:

        
        docker run arun1771/pokemon:v1 python3 pokemon_fetcher.py ditto

  
