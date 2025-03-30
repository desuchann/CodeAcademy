class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
right_stack = Stack('Right')
middle_stack = Stack('Middle')
stacks += [left_stack, middle_stack, right_stack]
#Set up the Game
num_disks = int(input('\nHow many disks do you want to play with?\n'))
while num_disks < 3:
  num_disks = int(input('\nAt least 3 disks pls.\n'))
for num_disk in reversed(range(num_disks)):
  left_stack.push(num_disk)
num_optimal_moves = 2**(num_disks)-1
print(f'\nThe fastest you can solve this game is in {num_optimal_moves} moves!')
#Get User Input
def get_input():
  choices = [s.get_name()[0] for s in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f'Enter {letter} for {name}')
    user_input = input(": ")
    if user_input.upper() in choices:
      user_input = user_input.upper()
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n...Current Stacks...")
    for s in stacks: s.print_items()
    print('\nWhich stack do you want to move from?\n')
    from_stack = get_input()
    print('\nWhich stack do you want to move to?\n')
    to_stack = get_input()
    if from_stack.is_empty():
      print("\nInvalid Move, try again...\n")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
    else:
      print("\nInvalid move, try again...\n")
for s in stacks: s.print_items()
print(f"\nYou completed the game in {num_user_moves} moves where the optimal amount is {num_optimal_moves}. Great job!\n")
