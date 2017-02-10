# -*- coding: utf-8 -*-
import os

API_KEY=os.getenv('SHUB_APIKEY', '')
PROJECT_ID=int(os.getenv('SHUB_PROJECT', 0))
FRONTIER_NAME=os.getenv('FRONTIER_NAME', '')
