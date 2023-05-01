# Choose a base image
FROM node:18.13.0

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the .next folder
COPY .next .next

# # Build the app
# RUN npm run build

# Set the command to run when the container starts
CMD ["npm", "start"]