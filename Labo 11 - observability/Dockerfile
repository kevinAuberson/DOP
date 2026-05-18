FROM maven:3.9.9-eclipse-temurin-17-alpine AS build

WORKDIR /app

COPY pom.xml ./
RUN mvn dependency:go-offline -B

COPY src ./src

RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jdk-alpine

WORKDIR /app

COPY --from=build /app/target/demotory-0.0.1-SNAPSHOT.jar /app/demotory.jar

EXPOSE 8080

CMD ["java", "-jar", "/app/demotory.jar"]
