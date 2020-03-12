class Jeep:
    hp = 300
    model = 'wrangler'

setattr(Jeep, 'wheels', 'winter tires')
print(getattr(Jeep, 'wheels'))

print(Jeep.__dict__)