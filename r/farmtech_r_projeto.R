# install.packages("jsonlite")

library(jsonlite)

areas <- c(120, 150, 180)
insumos <- c(300, 350, 400)

cat("---- ESTATÍSTICAS ----\n")

cat("Média das áreas:", mean(areas), "\n")
cat("Desvio padrão das áreas:", sd(areas), "\n")

cat("Média dos insumos:", mean(insumos), "\n")
cat("Desvio padrão dos insumos:", sd(insumos), "\n")

cat("\n---- CLIMA ----\n")

# Coordenadas de Goiânia
url <- "https://api.open-meteo.com/v1/forecast?latitude=-16.6869&longitude=-49.2648&current=temperature_2m,wind_speed_10m"

dados <- fromJSON(url)

cat("Temperatura:", dados$current$temperature_2m, "\n")
cat("Vento:", dados$current$wind_speed_10m, "\n")