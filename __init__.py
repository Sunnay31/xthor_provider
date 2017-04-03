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
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAD20lEQVR42k2TbVATdBzH/zBj9Sbo6IUwVGw57rg4UJo4wDGPJWSINPYEI2BjOh62tt3YGBCPEdsAh04UG4wxQXzsItQVDuKu1LpMw5K6rri8q+uud5ETbbDfr//2qhe/+7/43+/h+73vh3R3d5Ourq5IbXG5XKRCLidJSUn6/Pz8lcqqqqCoXLzO4+X+nJiY2D46OkrW1tZIIBDYYjQaSV9fH4k2d3Z2xthsNsLn87MzM7MWGpt0wePDJ+DM2Q/h/Q/6QafTh0XlknUud++tnp6eA8FgkExPT8dYLJboAIbdbifp6emlOft4jzs6u9FoNOGQ0wke7ySOe7zoGBgCmbwCysrKkcXaFhJLJOrZ2VliMBhiSeRsiUS8JzNzd1BvNEFhofDfSoUC+m12dI974NoNP8wHFtA1MgJUSqiAL9hkxjHDRUVFQrfbTYhSWRvLYrGWFFXVKHzjYKi+oREOvVUCh0uPwHX/p/jZzQB+t/wAWtvaQSqTY17e/lAKKwWZTOZDv99PSEL8iwZRpeJpmUgcVtDNdCuOUu0Hi4rRdWoEH/3+B166fAWVyjrw+qagudkMe7g5m5zXMjArK6ue7GSzV9SNWng5MZFqHQxPTPrg8tWP8Kx7DEsOl+LMzAVUqepw+KQLp87PoJf+v7qLE1ao1EAI+ZPsy8t/Ui6VQUJ8PI5PeOHjT+bw0pWreH/5AXZ19+AuDgdtjoFo80V6SWDxc0xLSwNJpQKStiatk5zcvCeSigqIpwPOX7gYNez2V1/j4tIS1qmPolKloq8a567fQGpo9I9DByiqayA1dec6Sdm2/SfNu3pIeCkhsiV89959+P7hClpaWtDuGMQxzwRKpFK0DwziDys/4s3AArzCZocNLa0QFxf3F3nheaZFWqN8dkQkhmazGVZ/e4RmiwXaOzojZuLkuSl0j41joVCI/vl5cDgcIJbKwzVH65H7eraJyGSy55KTk7+oqVWh4EBhqLqmFtTHjsHImVGYpgbOzl1D39Q0Dp84CZqGBiwufnNDpzdCQUHBL6urvzLI4NAQ4fF4e7lc7tMmrT6cl78/1KTVQcQ0mgH48vYd+Obbe+A7NwVSqWyj2dyyQXOC/bb+txGRkN7eXgYtwmazZfwCwTNr23tYUanYtLa2hanrQC8AJ+Wi6p3qzbb2DhRRqRqNxhAMPiaLi4uMCEiEAhJLiwgEgtzs7Ow7Wp0ebfYBPHX6dDQPkQyYLS0oFouXdVrtoUiEvV5vDGWBkP/hzHA6nSSCKfWkZPuOHbcyMjL+pnT+w+Fw7qampsp8Ph/xeDzEZDIxrFZrFOf/AFu5FJcUjneiAAAAAElFTkSuQmCC',
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
