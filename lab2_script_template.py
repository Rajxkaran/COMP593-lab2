
def main():

# Define the complex data structure
    about_me = {
        'my_name': 'Rajkaran singh',
        'stu_id': '10247786',
        'pizza_toppings': [
            'ham',
            'makhani sauce',
            'cottage cheese'
        ],
        'movies': [
        {
                'title': 'John wick',
                'genre' :'Thriller' 
        
            },
            {
                'title': 'kissing booth',
                'genre' :'Romantic' 
            },
            {
                'title': 'Old navy',
                'genre': 'Thriller'
            }
        ]
    }
    # Add a new movie to the data structure
    new_movie = {'title': 'Conjuring','genere': 'Horror'}
    about_me['movies'].append (new_movie)
    
    
    # Add some more pizza toppings to the data structure
    favourite_pizza_toppings = (['bacon','bell pepper','olive','beef' ])
    add_pizza_toppings_to_data(about_me, favourite_pizza_toppings) 

    # Print information from the complex data structure
    print_my_student_id(about_me)
    print_pizza_toppings (about_me)
    print_film_list(about_me)
    
    
    pass


def print_my_name (data):
    name = f"My name is', {data[ 'my_name' ]}, but my friends call me raj"

def print_my_student_id (data):
    identity = f"My student ID is', {data['stu_id' ]}"
    print (identity)

def add_pizza_toppings_to_data(data, favourite_pizza_toppings):
    data[ 'pizza_toppings' ].extend(favourite_pizza_toppings)
    
    for i,p in enumerate(data[ 'pizza_toppings']) :
        data['pizza_toppings'][i] = p.capatalize()

        data['pizza_toppings'].sort()
        
        
def print_pizza_toppings (data):
    # Print the heading
    heading = f"{data[' my_name ']} 's preffered pizza toppings are:"
    print(heading)
    print('-' * len(heading))

    # Print dash list of all pizza toppings
    for s in data[ 'pizza_toppings']:
        print (f"- {s}")
    print ()


def print_film_list(data):
    # My favourite movies-
    print (f" Myself {data[ 'my_name '].split(' ')[1]} and i love watching ", end='')
    for x,y in enumerate (data[ 'movies' ]) :
        print (g[ 'genre'], end='') 
        if x < len(data[ 'movies' ])-1:
            print(', ', end='')
print('.', end=' \n\n')


main()


 
