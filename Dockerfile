# Use a base image with Node.js installed
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies listed in package.json
RUN npm install

# Copy all the source code files to the container
COPY . .

# Expose port 3000 to access the application
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
