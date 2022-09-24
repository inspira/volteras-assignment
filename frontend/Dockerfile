# See: https://dev.to/aws-builders/containerize-react-app-with-docker-for-production-572b


# stage1 - build react app first
FROM node:16.17 as builder

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV NODE_ENV=production

ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app/

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --production

COPY ["src/", "./src/"]
COPY ["public/", "./public/"]

RUN npm run build


# stage 2 - build the final image and copy the react build files
FROM nginxinc/nginx-unprivileged:1.23 as server

COPY --from=builder /app/build /usr/share/nginx/html
