import gym
import numpy as np

from dueling_q_model import Agent

#from utils import plot_learning_curve



if __name__ == '__main__':
	env = gym.make('LunarLander-v2')
	num_games = 500

	load_checkpoint = False 

	agent = Agent(gamma = 0.99 , epsilon = 1.0 , lr = 5e-4, input_dims = [8]
		,n_actions = 4, mem_size = 1000000, eps_min = 0.01, batch_size = 64, 
		eps_dec= 1e-3 , replace= 100 )

	#load a check point 

	if load_checkpoint():
		agent.load_models()


	#to save the plot 

	filename = "graph.png"

	scores, eps_history  = [] , []

	for i in range(num_games):
		done = False 
		observation = env.reset()
		score = 0

		#plating the game 
		while not done:
			action = agent.choose_action(observation)
			observation_, reward, done, info = env.step(action)
			score += reward
			agent.score_transition(observation, action,reward,observation_, int(done))

			agent.learn()

			observation = observation_

		#appending the score 
		scores.append(score)
		avg_score = np.mean([scores[-100:]])

		print("episode",'score %.if' % score , 'average score %.if' % agent.epsilon)

		if i > 10 and i %10 == 0:
			agent.save_models()

		eps_history.append(agent.epsilon)

	x = [i+1 for i in range(num_games)]

	#plot_learning_curve(x, scores,eps_history,filename)
	







