"""Analytics Python CLI.

Usage:
  analytics track <event> [--properties=<properties>] [--context=<context>] [--writeKey=<writeKey>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics screen <name> [--properties=<properties>] [--context=<context>] [--writeKey=<writeKey>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics page <name> [--properties=<properties>] [--context=<context>] [--writeKey=<writeKey>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics identify [--traits=<traits>] [--context=<context>] [--writeKey=<writeKey>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics group --groupId=<groupId> [--traits=<traits>] [--properties=<properties>] [--context=<context>] [--writeKey=<writeKey>] [--userId=<userId>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
  analytics alias --userId=<userId> --previousId=<previousId> [--traits=<traits>] [--properties=<properties>] [--context=<context>] [--writeKey=<writeKey>] [--anonymousId=<anonymousId>] [--integrations=<integrations>] [--timestamp=<timestamp>]
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

    if arguments["track"]:
        properties =  arguments["--properties"]
        if properties:
            properties = json.loads(properties)
        analytics.track(user_id = userId, anonymous_id=anonymousId, event = arguments["<event>"], properties = properties, context = context, integrations = integrations)
    elif arguments["screen"]:
        properties =  arguments["--properties"]
        if properties:
            properties = json.loads(properties)
        analytics.screen(user_id = userId, anonymous_id=anonymousId, name = arguments["<name>"], properties = properties, context = context, integrations = integrations)
    elif arguments["page"]:
        properties =  arguments["--properties"]
        if properties:
            properties = json.loads(properties)
        analytics.page(user_id = userId, anonymous_id=anonymousId, name = arguments["<name>"], properties = properties, context = context, integrations = integrations)
    elif arguments["alias"]:
        analytics.alias(user_id = userId, previousId=arguments["--previousId"])
    elif arguments["group"]:
        traits =  arguments["--traits"]
        if traits:
            traits = json.loads(traits)
        analytics.group(user_id = userId, anonymous_id=anonymousId, groupId = arguments["--groupId"], traits = traits, context = context, integrations = integrations)
    elif arguments["identify"]:
        traits =  arguments["--traits"]
        if traits:
            traits = json.loads(traits)
        analytics.group(user_id = userId, anonymous_id=anonymousId, traits = traits, context = context, integrations = integrations)
    else:
        raise Exception('Unknown argument')

    analytics.flush
