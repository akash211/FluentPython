def handle_command(message):
    match message:
        case['BEEPER', frequency, times]:
            print(times, frequency)
        case['NECK', angle]:
            print(angle)
        case['LED', ident, intensity]:
            print(ident, intensity)
        case['LED', ident, red, green, blue]:
            print(ident, red, green, blue)
        case _:
            raise ValueError(f"{message} is not a valid command")


handle_command(['BEEPER', 10, 2])
handle_command(['BEEPER', 5, 2])
handle_command(['NECK', 90])
handle_command(['LED', 10, 2])
handle_command(['LED', 10, 2, 0, 1])
# handle_command(['LED', 10, 2, 0, 1, 0, 1]) # throws error

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9} | {"coord":>20}')
    for record in metro_areas:
        match record:
            case [name, *_, (lat, lon) as coord] if lon <= 0:  # destructuring
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}', end=" |     ")
                print(coord)


main()
# Instances of str, bytes, and bytearray are not handled as sequences in the context of match/case


def phone_numbers(phone):
    match tuple(str(phone)):
        case ['1', *rest]:
            print("North America and Caribbean")
        case ['2', *rest]:
            print("Africa and some territories")
        case ['3' | '4', *rest]:
            print("Europe")
        case _:
            raise ValueError(f"{phone} is not a valid phone number")


phone_numbers(3335876)
phone_numbers(13335876)
# phone_numbers(9335876) # raise Error
