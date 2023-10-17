import yaml
import logging

conf = None

try:
    with open('./config/config.yaml', 'r') as f:
        conf = yaml.load(f.read(), Loader=yaml.FullLoader)
except Exception as e:
    logging.error(str(e))
