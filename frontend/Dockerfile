# Build stage
FROM node:20-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Development stage
FROM node:20-alpine as development

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

# Production stage
FROM node:20-alpine as production

WORKDIR /app

COPY --from=build /app/.output /app/.output

EXPOSE 3000

ENV NODE_ENV=production

CMD ["node", ".output/server/index.mjs"] 