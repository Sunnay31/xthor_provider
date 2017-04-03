from .main import xthor	

def autoload():
    return xthor()

config = [{
    'name': 'xthor',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'xthor',
            'description': 'See <a href="https://xthor.bz/">XThor</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'passkey',
                    'default': '',
                },
                {
                    'name': 'freeleech',
                    'label': 'freeleech only',
                    'default': 0,
                    'type': 'bool',
                    'description': 'Will ignore result if not in freeleech',
                },                
                {
                    'name': 'multi',
                    'label': 'ignore lang in multi',
                    'default': 0,
                    'type': 'bool',
                    'description': 'Will ignore "french" and "truefrench" if "multi" is detected',

                },
                {
                    'name': 'min_seeders',
                    'label': 'Minimum Seeders',
                    'default': 1,
                    'type': 'int',
                    'description': 'Minimum number of seeders to accept result',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                }
            ],
        },
    ],
}]
