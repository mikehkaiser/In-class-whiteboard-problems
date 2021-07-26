street_1 = ['T', 't', 'T', 'f', 'T']


def outages(l_street):
    counter = 0
    for light in l_street:
        if light.lower() == 'f':
            counter += 1
            if counter >= 2:
                return 'Outage'
    return 'Power'


outages(street_1)
