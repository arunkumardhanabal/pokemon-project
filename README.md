# Pokémon Data Fetcher

## Description

This project retrieves Pokémon data from the PokéAPI and outputs it in JSON format. It's containerized with Docker and can be deployed to Kubernetes using the provided Helm chart.

## Contents

* **`pokemon_fetcher.py`**:  Python script to fetch Pokémon data.
* **`Dockerfile`**:  Instructions to build a Docker image for the application.
* **`helm/pokemon-chart`**:  Helm chart for deploying to Kubernetes.
* **Docker Image**: `arun1771/pokemon:v1`

## Prerequisites

* Docker installed
* Helm installed (if deploying to Kubernetes)
* Kubernetes cluster (if deploying with Helm)

## Instructions

**1.  Using Docker**

* Clone this repository.
* Build the Docker image:

        
        e.g., docker build -t pokemon-app:v1.1 .
        
        
* Run the container, providing the Pokémon name as an argument:
    
  
        e.g., docker run pokemon-app:v1.1 python3 pokemon_fetcher.py ditto
