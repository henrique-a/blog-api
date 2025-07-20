# Posigliere coding challenge

A RESTful API for managing a simple blogging platform, using a containerized Django application with PostgreSQL database and Docker setup.

## How to run it

### Prerequisites
- Docker & Docker Compose installed
- Git

```bash
git clone <your-repo-url>
cd api
```

### 3. Run the Application

```bash
docker compose --env-file .env up --build
```
Access at: http://localhost:80

### Test

**Create Post**
```bash 
curl --location 'localhost:80/api/posts/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Test post",
    "content": "Lorem Ipsum"
}'
```

**Get Post**
```bash 
curl --location 'localhost:80/api/posts/a2fb4545-86a1-4616-bfce-233878df2f6d' \
--data ''
```

**List Posts**
```bash 
curl --location 'localhost:80/api/posts/' \
--data ''
```

**Create Comment**
```bash 
curl --location 'localhost:80/api/posts/8f1baabc-8815-4145-b030-0c95751c2010/comments' \
--header 'Content-Type: application/json' \
--data '{
    "content": "Lorem Ipsum"
}'
```

## Next Steps
- Set up HTTPS with certbot.
- Add authentication and authorization (e.g., JWT or session-based) to secure the API.
- Add unit tests for posts, comments, and user flows.
- Switch to asynchronous views and asynchronous database connections.
