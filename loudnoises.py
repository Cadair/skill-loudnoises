from opsdroid.skills import match_regex
import random

@match_regex(r'(\b([A-Z]{2,}\s+)([A-Z]{2,})\b)|(\b[A-Z]{5,}\b)')
def loudnoises(opsdroid, message):
    message.respond("http://i.imgur.com/auk7p8z.jpg")
