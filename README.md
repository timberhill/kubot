# kubot
[![test](https://github.com/timberhill/kubot/actions/workflows/test.yaml/badge.svg)](https://github.com/timberhill/kubot/actions/workflows/test.yaml)
[![build](https://github.com/timberhill/kubot/actions/workflows/build.yaml/badge.svg)](https://github.com/timberhill/kubot/actions/workflows/build.yaml)

*Reddit bot fleet framework for kubernetes.*


This is early RnD, please move along.

## Kubot dispatcher

### Client credentials

Get at https://www.reddit.com/prefs/apps

## To do

### Stage 1 - local single-threaded app with a comment trigger

- `core-1`: Dispatcher class reading comments from PRAW in a single thread
- `maint-1`: github action that adds a version tag on PR merge
- `core-`: Logging setup
- `core-`: Create an example bot
- `core-`: Dispatcher sending comments over tcp to an example bot that just logs out the comment if a word is found

### Stage 2 - package up for kubernetes

- `core-`: Docker containers for dispatcher and the example bot
- `core-`: Manifests for the dispatcher+configmap and the example bot+service
- `core-`: Dispatcher can find a service endpoint for the bot
