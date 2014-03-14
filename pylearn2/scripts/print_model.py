#!/usr/bin/env python
__author__ = "Ian Goodfellow"
"""
Usage: print_model.py <pickle file containing a model>
Prints out a saved model.
"""
import logging
import sys

from pylearn2.utils import serial


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    _, model_path = sys.argv

    model = serial.load(model_path)

    logger.info(model)
