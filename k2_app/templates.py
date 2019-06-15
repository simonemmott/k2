from k2.settings import BASE_DIR, MAIN_DIR
import os
import logging

logger = logging.getLogger(__name__)

def index(domain, path):
    search_path = '/'.join([BASE_DIR, domain, 'jinja2', path])
    if os.path.isdir(search_path):
        idx={}
        logger.debug('Indexing directory: {path}'.format(path=path))
        for file in os.listdir(search_path):
            idx[file] = '{path}'.format(domain=domain, path='/'.join([path, file]))
        return idx
    else:
        raise ValueError("The path '{path} is not a directory".format(path=search_path))
    