
# To do

## Stage 1 - local single-threaded app with a comment trigger

- _done_ `core-1`: Dispatcher class reading comments from PRAW in a single thread
- `core-2`: Dispatcher class reading both submissions and comments
- `maint-1`: github action that adds a version tag on PR merge
- `core-`: Logging setup
- `core-`: Create an example bot
- `core-`: Dispatcher sending comments over tcp to an example bot that just logs out the comment if a word is found

## Stage 2 - package up for kubernetes

- `core-`: Docker containers for dispatcher and the example bot
- `core-`: Manifests for the dispatcher+configmap and the example bot+service
- `core-`: Dispatcher can find a service endpoint for the bot
