
# To do

## Stage 1 - local single-threaded app with a comment trigger

### Core functionality

- `core-1`: ~~Dispatcher class reading comments from PRAW in a single thread~~
- `core-2`: ~~Dispatcher class reading both submissions and comments~~
- `core-3`: ~~Dispatcher using the config for the subreddit list~~
- `core-4`: ~~Create an example bot, dispatcher sends comments over tcp to an example bot that just logs out the comment if a word is found~~
- `core-5`: Dispatcher sends events to multiple bots
- `core-`: Bots renamed to clients
- `core-`: Logging implemented

### Maintenance

- `maint-1`: github action that adds a version tag on PR merge

## Stage 2 - package up for kubernetes

- `core-`: Docker containers for dispatcher and the example bot
- `core-`: Manifests for the dispatcher+configmap and the example bot+service
- `core-`: Dispatcher can find a service endpoint for the bot
