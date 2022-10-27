import dataset

db = dataset.connect('sqlite:///Phones_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Apple' },
        { "description": 'Samsung' },
        { "description": 'Nokia' },
        { "description": 'Motorola' },
        { "description": 'Google Pixel' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()