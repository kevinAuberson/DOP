# Étape 1 : Build de l'application Vue.js
FROM node:20 AS build

WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install 

# Copier le reste du code source
COPY . .

# Construire l'application
RUN npm run build 

# Étape 2 : Serveur Nginx pour servir l'application
FROM nginx:1.27-alpine-slim

# Copier les fichiers buildés de Vite dans Nginx
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
