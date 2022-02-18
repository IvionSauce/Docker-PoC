#!/usr/bin/env python

import cherrypy
import random


phrases = (
    # Make the bulk humorous/witty.. or at least attempt to.
    "Assumption is the mother of all fuck-ups.",
    "It compiles; ship it.",
    "When I wrote this code, only God and I understood what I did. Now only God knows.",
    "Always code as if the person who ends up maintaining your code will be a violent psychopath who knows where you live.",
    "There are only two kinds of programming languages out there: the ones people complain about and the ones no one uses.",
    "UNIX is user friendly. It's just very particular about who its friends are.",
    "The trouble with programmers is that you can never tell what a programmer is doing until it's too late.",
    "A user interface is like a joke. If you have to explain it, it's not that good.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "The generation of random numbers is too important to be left to chance.",
    "Any fool can use a computer. Many do.",
    "That's the thing about people who think they hate computers.  What they really hate is lousy programmers.",
    "To iterate is human, to recurse divine.",
    "The use of COBOL cripples the mind; its teaching should therefore be regarded as a criminal offense.",
    "Fifty years of programming language research, and we end up with C++?",
    "You can't have great software without a great team, and most software teams behave like dysfunctional families.",
    "A computer lets you make more mistakes faster than any invention in human history.. with the possible exceptions of handguns and tequila.",
    "If debugging is the process of removing bugs, then programming must be the process of putting them in.",
    "Optimism is an occupational hazard of programming; feedback is the treatment.",
    "The test of the machine is the satisfaction it gives you. There isn't any other test. If the machine produces tranquility it's right. If it disturbs you it's wrong until either the machine or your mind is changed.",
    "Humans are the reproductive organs of technology.",
    "Any sufficiently advanced technology is indistinguishable from magic.",
    "Explanations exist; they have existed for all time; there is always a well-known solution to every human problem - neat, plausible, and wrong.",

        # But also mix in some serious phrases/quotes.
    "Debugging is twice as hard as writing the code in the first place.  Therefore, if you write the code as cleverly as possible, you are – by definition – not smart enough to debug it.",
    "Controlling complexity is the essence of computer programming.",
    "Computer science education cannot make anybody an expert programmer any more than studying brushes and pigment can make somebody an expert painter.",
    "Technology is a useful servant but a dangerous master.",
    "When I am working on a problem I never think about beauty, but when I have finished, if the solution is not beautiful, I know it is wrong.",
)

class RandomSaying (object):
    def __init__(self):
        self.saying = Saying()

    @cherrypy.expose
    def index(self):
        index = random.randrange(0, len(phrases))
        return {
            "saying" : phrases[index],
            "index" : index,
            "description" :
            "Provides a (witty) saying, randomly picked from {} options!".format(len(phrases)),

            "links" : {
                "all-sayings" : "/sayings",
                "this-saying" : "/saying/{}".format(index),
                "wat" : "/wat"
            }
        }

    @cherrypy.expose
    def sayings(self):
        return {
            "sayings" : phrases,
            "description" : "The entire collection of sayings we randomly pick from.",
            "links" : {
                "random-saying" : "/"
            }
        }

    @cherrypy.expose
    def wat(self):
        return {
            "wat" : "https://www.destroyallsoftware.com/talks/wat",
            "description" : "Recommended watching for anyone involved in this sordid affair called programming."
        }

@cherrypy.popargs("indexStr")
class Saying (object):
    @cherrypy.expose
    def index(self, indexStr):
        try:
            index = int(indexStr)
        except ValueError:
            index = -1

        if index >= 0 and index < len(phrases):
            return {
                "saying" : phrases[index],
                "index" : index,

                "links" : {
                    "random-saying" : "/",
                    "all-sayings" : "/sayings"
                }
            }
        else:
            return {"error" : "Invalid index."}


if __name__ == "__main__":
    cherrypy.config.update(
        {"server.socket_host" : "0.0.0.0"}
    )

    cherrypy.quickstart(
        RandomSaying(), "/",
        {"/" : {"tools.json_out.on" : True,
                "tools.trailing_slash.on" : False,}}
    )
