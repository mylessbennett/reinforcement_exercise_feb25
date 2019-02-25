def draw_shape(options):
    shape = ""

    for r in range(options['rows']):
        for c in range(options['cols']):
            shape += options['char']

        shape += "\n"

    return shape


print(draw_shape({'rows': 5, 'cols': 10, 'char': '*'}))
print(draw_shape({'rows': 10, 'cols': 2, 'char': '#'}))
