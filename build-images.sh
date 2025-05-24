#!/bin/bash

# Construir imagen de suma
docker build -t suma:latest ./suma

# Construir imagen de resta
docker build -t resta:latest ./resta

# Construir imagen de ecuación
docker build -t ecuacion:latest ./ecuacion

# Construir imagen de storage
docker build -t storage:latest ./storage 