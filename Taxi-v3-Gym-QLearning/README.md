This folder is part of the Project course in Data Camp for the Taxi Route Optimization using Reinforcement Learning.
Project Instructions
Train an agent over 2,000 episodes, allowing for a maximum of 100 actions per episode (max_actions), utilizing Q-learning. Record the total rewards achieved in each episode and save these in a list named episode_returns.
What are the learned Q-values? Save these in a numpy array named q_table.
What is the learned policy? Save it in a dictionary named policy.
Test the agent's learned policy for one episode, starting with a seed of 42. Save the encountered states from env.render() as frames in a list named frames, and the sum of collected rewards in a variable named episode_total_reward. Make sure your agent does not execute more than 16 actions to solve the episode. If your learning process is efficient, the episode_total_reward should be at least 4.
Execute the last provided cell to visualize your agent's performance in navigating the environment effectively. Please note that it might take up to one minute to render.

