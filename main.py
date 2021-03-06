# coding: utf8
from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback
import urllib2
import json
import sys
import urllib

log = CPLog(__name__)

import ast
import operator

_binOps = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.div,
    ast.Mod: operator.mod
}

class xthor(TorrentProvider, MovieProvider):

    urls = {
        'index' : 'https://xthor.bz',
        'api' : 'https://api.xthor.bz?passkey=%s&search=%s',
        'permalink' : 'https://xthor.bz/details.php?id=%s',
    }

    http_time_between_calls = 1 #seconds
    cat_backup_id = None

    def _searchOnTitle(self, title, movie, quality, results):
        request = ''
        if isinstance(title, str):
            title = title.decode('utf8')
        
        request = title.replace(':', '')
        request = urllib2.quote(request.encode('iso-8859-1'))

        log.debug('Looking on Xthor for movie named %s' % (title))
        url = self.urls['api'] % (self.conf('passkey'), request)
        #log.debug('Request to Xthor: %s' % (url))
        xthorresponse = self.getHTMLData(url)

        if xthorresponse:
            log.debug('Data received from Xthor')
            data = json.loads(xthorresponse)
            try:
                torrents = data['torrents']
                for torrent in torrents:
                    log.info('Xthor found ' + torrent['name'])
                    valid = True
                    # Testing seeders
                    if int(torrent['seeders']) < int(self.conf('min_seeders')):
                        valid = False
                        log.debug('Skipping torrent, not enough seeders (%s)' % (torrent['seeders']))
                    # Testing freeleech
                    if self.conf('freeleech') and torrent['freeleech'] == '0':
                        valid = False
                        log.debug('Skipping torrent, not freeleech.')
                    if valid:
                        results.append({
                            'leechers': torrent['leechers'],
                            'seeders': torrent['seeders'],
                            'name': torrent['name'],
                            'url': torrent['download_link'],
                            'detail_url': self.urls['permalink'] % (torrent['id']),
                            'id': torrent['id'],
                            'size': str(int(torrent['size']) / 1048576),
                    })
            except:
                log.error('Failed getting results from %s: %s', (self.getName(), traceback.format_exc()))
