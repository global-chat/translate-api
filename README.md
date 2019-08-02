# translate-api

## Introduction

This is a simple Lambda function written to translate incoming json text

It is integrated with API Gateway via a POST request:

### API

Post with the following body content:

  {
    "source": "{Source Language of Text}",
    "target: "{Desired Language for Translation}",
    "text": "{text to be translated}"
  }

## Deployment Instructions

- Upload the python script as a lambda function
- Create an API Gateway with a POST route and integrate with lambda.



