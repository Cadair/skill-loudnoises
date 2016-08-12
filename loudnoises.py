from opsdroid.skills import match_regex
import random

@match_regex(r'^[^a-z]*$')
def loudnoises(opsdroid, message):
    message.respond("http://i.imgur.com/auk7p8z.jpg")
