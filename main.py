from game_utils import solve_riddle, end_game, enter_room
# Define the function greeting and welcome the user
def greeting():
    print("Hello! Welcome to a new adventure")
    print("You will navigate trough different rooms where you have to solve riddles to proceed. The goal is to find the lost treasure")


def main():
    greeting()
    rooms= [
        {
            'name': 'the entrance hall',
            'description': 'A dark room with old paitings on the walls',
            'riddle':{
                'question': 'I am not alive, but I grow. I have no lungs, but I need air. What am I?',
                'answer': 'fire'
            }
        },
        {
            'name': 'the libary',
            'description': 'Shelves full of dusty books surround you.',
            'riddle':{ 
                'question': 'What words become shorter when you add letters to them?',
                'answer': 'short'
            }
        },        
        {
            'name': 'the treasure chamber',
            'description': 'A shining treasure lies before you.',
            'riddle':{
                'question': 'What breaks when you speak it?',
                'answer': 'silence'
            }
        }        
     ]


currentroom = 0
while currentroom < len(rooms):
   room=rooms[currentroom]
   enter_room(room)
   if currentroom < len(rooms) - 1:
       user_input = input("Do you want to enter the next room? (yes/no) \n")
       if user_input.strip().lower() != "yes":
           end_game()
           currentroom += 1
           print("You found the treasure. Congrats!")


main():
