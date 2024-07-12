This project is a working AI snake game in which a reinforcement learning algorithm helps the snake to learn to maximize its score based on its surroundings.
This is completely coded from scratch using PyTorch, PyGame and Reinforcement learning algorithms.

Rewards (irrespective of the state):

Eating  - +10
Gameover - -10
Any other - 0

States(11 values):

[Danger straight,
Danger right,
Danger left,
Direction left,
Direction right,
Direction up,
Direction down,
Food Left,
Food Right,
Food Up,
Foor Down
]

Actions:

[1,0,0] -> Straight
[0,1,0] -> Right turn
[0,0,1] -> Left turn

Model:

Feed Forward Neural Network that uses Deep Q-Learning Algorithm for predicting an action based on the state.
