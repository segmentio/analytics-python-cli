#!/usr/bin/env python
"""Analytics Python CLI.

Usage:
  analytics --writeKey=<writeKey> --type=track --event=<event> [--properties=<properties>] [--context=<context>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics --writeKey=<writeKey> --type=screen --name=<name> [--properties=<properties>] [--context=<context>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics --writeKey=<writeKey> --type=page --name=<name> [--properties=<properties>] [--userId=<userId>] [--context=<context>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics --writeKey=<writeKey> --type=identify [--traits=<traits>] [--context=<context>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics --writeKey=<writeKey> --type=group --groupId=<groupId> [--traits=<traits>] [--properties=<properties>] [--context=<context>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics --writeKey=<writeKey> --type=alias --userId=<userId> --previousId=<previousId> [--context=<context>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics -h | --help
  analytics --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt
import analytics
import os
import json
import sys

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')

    writeKey = arguments["--writeKey"]
    if not writeKey:
        analytics.write_key = os.getenv('SEGMENT_WRITE_KEY')
    else:
        analytics.write_key = writeKey

    userId = arguments["--userId"]
    anonymousId = arguments["--anonymousId"]
    timestamp = arguments["--timestamp"]
    context = arguments["--context"]
    if context:
        context = json.loads(context)
    integrations = arguments["--integrations"]
    if integrations:
        integrations = json.loads(integrations)

    msgType = arguments["--type"]

    if msgType == "track":
        properties =  arguments["--properties"]
        if properties:
            properties = json.loads(properties)
        analytics.track(user_id = userId, anonymous_id=anonymousId, event = arguments["--event"], properties = properties, context = context, integrations = integrations)
    elif msgType == "screen":
        properties =  arguments["--properties"]
        if properties:
            properties = json.loads(properties)
        analytics.screen(user_id = userId, anonymous_id=anonymousId, name = arguments["--name"], properties = properties, context = context, integrations = integrations)
    elif msgType == "page":
        properties =  arguments["--properties"]
        if properties:
            properties = json.loads(properties)
        analytics.page(user_id = userId, anonymous_id=anonymousId, name = arguments["--name"], properties = properties, context = context, integrations = integrations)
    elif msgType == "alias":
        analytics.alias(user_id = userId, previousId=arguments["--previousId"])
    elif msgType == "group":
        traits =  arguments["--traits"]
        if traits:
            traits = json.loads(traits)
        analytics.group(user_id = userId, anonymous_id=anonymousId, group_id = arguments["--groupId"], traits = traits, context = context, integrations = integrations)
    elif msgType == "identify":
        traits =  arguments["--traits"]
        if traits:
            traits = json.loads(traits)
        analytics.identify(user_id = userId, anonymous_id=anonymousId, traits = traits, context = context, integrations = integrations)
    else:
        raise Exception('Unknown argument')

    analytics.flush
