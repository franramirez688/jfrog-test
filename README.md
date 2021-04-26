# jfrog-test

This a very simple web application (Flask + ReactJS) hosted by Heroku.

## Requirements

* python 3.x (if you want to run your tests locally)
* docker-compose 17.12.0+
* Heroku CLI (in case of manual deployments)

## Up&running

Simply run:

```bash
docker-compose up -d --build
```

Now, you should be able to see both in your browser:

**FRONTEND**: localhost:3001
**BACKEND**: localhost:5000

## Tests (backend)

```bash
pytest tests/backend
```

## CI/CD

It's using Github Actions to perform a correct CI/CD flow. If all the tests are passing, the app will be correctly deployed in Heroku.
See the `.github/workflows/main.yml` file.

## Missing things

* Heroku is not deploying correcly the application due to problems with Docker. It's not detecting any images to be deployed.
* The frontend is not rendering correctly the endpoint `[FLASK_API]/contacts`. See `frontend/src/App.js`.
* Zero-downtime. Indeed, I was not able to check this part. Here, I can say that given my experience with AWS, what I would try to do is:
    - Define a EBS (Elastic Load Balancer)
    - Deploy the containers into different AZ (Availability Zones)
    - For new updates, we'll have to define the mechanism to point to that region instead of the one that is being affected by the new upgrade.

