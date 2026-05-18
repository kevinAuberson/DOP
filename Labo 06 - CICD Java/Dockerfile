FROM maven:3.9.9-eclipse-temurin-17 AS build

WORKDIR /app

# Copier uniquement les fichiers nécessaires pour optimiser le cache Docker
COPY pom.xml ./
RUN mvn dependency:go-offline -B

COPY src ./src

RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jdk-noble

WORKDIR /app

# Copier le fichier JAR généré depuis l'étape de build
COPY --from=build /app/target/testing-web-complete-0.0.1-SNAPSHOT.jar /app/dop-java.jar

EXPOSE 8080

CMD ["java", "-jar", "/app/dop-java.jar"]