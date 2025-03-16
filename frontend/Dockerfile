# Development stage
FROM node:20-alpine as development

WORKDIR /app

# Add build dependencies
RUN apk add --no-cache python3 make g++

# Copy package files
COPY package.json ./

# Install dependencies with development packages
RUN npm install

# Set development environment
ENV NODE_ENV=development

# Expose the port
EXPOSE 3000

# Start the application in development mode
CMD ["npm", "run", "dev"]

# Build stage
FROM node:20-alpine as build

WORKDIR /app

# Add build dependencies
RUN apk add --no-cache python3 make g++

# Copy package files
COPY package.json ./

# Install dependencies
RUN npm install

# Copy source
COPY . .

# Build the app
RUN npm run build

# Production stage
FROM node:20-alpine as production

WORKDIR /app

# Copy built files from build stage
COPY --from=build /app/.output /app/.output

# Set production environment
ENV NODE_ENV=production

# Expose the port
EXPOSE 3000

# Start the application
CMD ["node", ".output/server/index.mjs"] 