def get_class_repr(class_entity, class_name):
    if not class_entity or not class_name:
        raise Exception('Invalid arguments')

    # gets values for all class members
    values_str = ', '.join(list(map(
        lambda prop: f'{class_entity.__dict__[prop]}',
        list(class_entity.__dict__)
    )))
    return f'{class_name}({values_str})'
