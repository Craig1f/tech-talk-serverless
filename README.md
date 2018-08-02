# serverless framework

## What Problem Do We Want to Solve?

1. Writing Lambda Functions
2. Code locally, deploy easily
    1. Maintaining our code in Git/Source Control
    2. Stay out of console (except to debug)
3. Manage any number of stages easily
4. Wire up API Gateway easily
5. Manage IAM permissions

## Enter serverless

[serverless.com](serverless.com)

1. Write in the language of your choice (we will use Python)
2. Write code locally (or in Cloud 9) and maintain in Git. Use Console for testing
3. Use an env.yml file in serverless, or some Codebuild voodoo (discussed later). Can also be combined with ssm.
4. Couldn't be simpler
5. Simple. More complicated use-cases handled easily with a plugin

