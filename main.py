
def main():

    name = input("what is you name? ")
    options = ['Light', 'Dark']
    sides = ''
    output_message = 'Which side of the force would you like to use? \n'
    for index, item in enumerate(options):
        output_message += f'{index+1}) {item}\n'

    while sides.capitalize() not in options:
        sides = input(output_message)
    
    if (sides == 'Dark'):
        dark(name)

    # else:
    #     light(name)


def dark(name):



main()
