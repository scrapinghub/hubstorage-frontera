# -*- coding: utf-8 -*-
import config
from hcf_backend import HCFStates
from frontera.core.models import Request
from random import randint, choice
from sys import maxsize
import logging

from unittest import skipIf


def generate_fprint():
    return ''.join(map(lambda x:choice('0123456789abcdef'), range(40)))


def check_states(states, fprints, objs):
    states.fetch(fprints)
    objs_fresh = [Request(o.url, meta={b'fingerprint': o.meta[b'fingerprint']}) for o in objs]
    states.set_states(objs_fresh)
    i1 = iter(objs)
    i2 = iter(objs_fresh)

    while True:
        try:
            o1 = next(i1)
            o2 = next(i2)
            assert o1.meta[b'fingerprint'] == o2.meta[b'fingerprint']
            assert o1.meta[b'state'] == o2.meta[b'state']
        except StopIteration:
            break

@skipIf(not config.API_KEY, "missing config API_KEY")
@skipIf(not config.PROJECT_ID, "missing config PROJECT_ID")
@skipIf(not config.FRONTIER_NAME, "missing config FRONTIER_NAME")
def test_states():
    logging.basicConfig(level=logging.DEBUG)
    states = HCFStates(config.API_KEY, config.PROJECT_ID, config.FRONTIER_NAME, 256, True)
    states.frontier_start()
    objs = []
    fprints = []
    for i in range(0, 128):
        o = Request('http://website.com/%d' % randint(0, maxsize))
        o.meta[b'fingerprint'] = generate_fprint()
        o.meta[b'state'] = choice([HCFStates.NOT_CRAWLED, HCFStates.QUEUED, HCFStates.CRAWLED, HCFStates.ERROR])
        objs.append(o)
        fprints.append(o.meta[b'fingerprint'])

    states.update_cache(objs)
    states.flush()

    # cache is warm
    check_states(states, fprints, objs)

    # clearing tha cache, and testing fetching
    states.flush(force_clear=True)
    check_states(states, fprints, objs)





