# serverless framework

## Intro

### What Problem Do We Want to Solve

- [ ] Writing Lambda Functions
  - Arbitrary code
- [ ] Code locally, deploy easily
  - [ ] Maintaining our code in Git/Source Control
  - [ ] Stay out of console (except to debug)
- [ ] Manage any number of stages easily
- [ ] Wire up API Gateway easily
- [ ] Manage IAM permissions

### Enter serverless

- [x] Writing Lambda Functions
  - Write in the language of your choice (we will use Python)
- [x] Code locally, deploy easily
  - [x] Maintaining our code in Git/Source Control
  - [x] Stay out of console (except to debug)
  - Write code locally (or in Cloud9) and maintain in Git. Use Console for testing
- [x] Manage any number of stages easily
  - Maintain environments in serverless or, preferably, use SSM Param Store
- [x] Wire up API Gateway easily
  - Couldn't be simpler
- [x] Manage IAM permissions
  - Simple. More complicated use-cases handled easily with a plugin
- [ ] A plugin for IAM you say? Go on ...

## Getting Started

Disclaimers: I'm on a Mac. Mileage may vary

[serverless.com](serverless.com)

Visit serverless for comprehensive steps. I'm going to assume some basic pre-requisites, such as nodejs for this demo.

1. Install serverless
    ```bash
    npm install -g serverless
    ```
2. Create a project
    ```bash
    serverless create --template aws-python --path my-service
    ```
3. Deploy
    ```bash
    sls deploy -v
    ```
4. Local Test
    ```bash
    sls invoke local -f hello
    ```

Quick Review of the serverless.yml file

## Advanced Examples: Plugins

    Run through the second deployment

## Takeaways/Review/Cheat Sheet

1. A typical stack will use:
    - EC2->SSM->Param Store
    - API Gateway
    - Lambda (Python, Node, etc)
    - Backend (RDS, Dynamo, etc)
    - IAM
2. "I have complicated IAMs that need to be adjusted on a per-function basis":
    - [serverless-iam-roles-per-function](https://www.npmjs.com/package/serverless-iam-roles-per-function)
3. "I hit the 200 resource limit with CloudFormation because I have over 30 functions, using 6 resources each!"
    - [serverless-plugin-split-stacks](https://www.npmjs.com/package/serverless-plugin-split-stacks)
    - [Additional Information](https://serverless.com/blog/serverless-workaround-cloudformation-200-resource-limit/)
4. "I have a requirements.txt file with my python. I might also want a different one per python. Also, I might be hitting the 10mb limit on my lambdas, preventing me from viewing my code in the console when I want to debug."
    - [serverless-python-requirements](https://www.npmjs.com/package/serverless-python-requirements)

5. `Serverless Error ---------------------------------------` shows up with no additional information! What gives?
    `SLS_DEBUG=true` and run again

6. "My functions are timing out!"
    - One-line adjustment to add a timeout by seconds. 6 is default

7. Authorizer
    - Controls access to routes
    - Caches for 5 minutes
    - Allows you to pass values through to your lambda

## Questions