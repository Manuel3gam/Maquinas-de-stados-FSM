libreria=[
    {
        'nombre':'La novela más larga',
        'género':'novela',
        'autor' :'Elif'
    },
    {
        'nombre':'Filosofía del electrón',
        'género':[
            {
                'ciencias':{
                    'física':'partículas'
                }
            },
            'Filosofía'
        ],
        'autor' : [
            {
                'Instituto de altas energías':[
                    'Gonzalo Rodríguez',
                    'Rodrigo González'
                ],
                'Centro Filosófico del Sur': 'Dolores de Rodríguez'
            }
        ]
    }
]

import json

with open('libreria.json', 'w') as archivo:
    json.dump(libreria,archivo)
with open('libreria.json', 'r') as archivo:
    libreria_leida=json.load(archivo)
print(libreria_leida
)
