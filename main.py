units = {}

feet = {
        'yards': 1 / 3,
        'inches': 12,
}

units.setdefault('feet', {}).update(feet)

def convert_units(amount: int | float, from_unit: str, to_unit: str) -> int | float:
    if from_unit in units and to_unit in units[from_unit]:
        return amount * units[from_unit][to_unit]
    elif to_unit in units and from_unit in units[to_unit]:
        return amount / units[to_unit][from_unit]
    else:
        raise ValueError(f'No conversion available between units: {from_unit} and {to_unit}')

def test_conversions():
    assert convert_units(12, 'feet', 'yards') == 4
    assert convert_units(12, 'feet', 'inches') == 144
    assert convert_units(12, 'inches', 'feet') == 1
    assert convert_units(12, 'yards', 'feet') == 36
    print('Tests Passed.')

def main():
    print(convert_units(12, 'feet', 'yards'))
    print(convert_units(12, 'feet', 'inches'))
    print(convert_units(12, 'inches', 'feet'))
    print(convert_units(12, 'yards', 'feet'))


if __name__ == '__main__':
    main()
