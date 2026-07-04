# Build
FROM node:24-slim AS build

# Set the working directory
WORKDIR /app

# Retrieve project files & dependencies
COPY ./ ./

# Install
RUN npm install

# Build
RUN npm run build

# Expose Port
EXPOSE 4173

# Start Server
CMD [ "npm", "version" ]

# Deploy
FROM nginx:alpine AS deploy

# Copy build output to Nginx's html directory
COPY --from=build /app/build /usr/share/nginx/html

# Optionally, copy a custom nginx.conf if you have one
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port Nginx runs on
EXPOSE 80

# Start Nginx (default CMD is fine, so this line is optional)
CMD ["nginx", "-g", "daemon off;"]
