"""
Lambda example with external dependency
"""

import os
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    """
    Lambda handler
    """
    logger.info("%s - %s", event, context)
    logger.info("ENV: %s", os.environ)

    url = "https://api.ipify.org?format=json"

    raw = requests.get(url)
    logger.info("%s", raw)
    result = raw.json()

    logger.info("Lambda IP: %s", result['ip'])
