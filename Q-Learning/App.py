import gymnasium as gym
import numpy as np
import time

# Inisialisasi environment dan Q-table
env = gym.make("FrozenLake-v1", is_slippery=False)
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Parameter Q-learning
alpha = 0.8         # Learning rate
gamma = 0.95        # Discount factor
epsilon = 1.0       # Epsilon awal (untuk eksplorasi)
min_epsilon = 0.1   # Nilai minimum epsilon
decay_rate = 0.995  # Laju penurunan epsilon

# Jumlah episode pelatihan
num_episodes = 5000

# Proses pelatihan Q-Learning
for episode in range(num_episodes):
    state, _ = env.reset()
    done = False
    total_reward = 0

    while not done:
        # Pilih aksi dengan epsilon-greedy
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        # Eksekusi aksi di environment
        next_state, reward, terminated, truncated, _ = env.step(action)

        # Update Q-table dengan rumus Q-learning
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        new_value = old_value + alpha * (reward + gamma * next_max - old_value)
        q_table[state, action] = new_value

        # Perbarui state dan akumulasi reward
        state = next_state
        total_reward += reward
        done = terminated or truncated

    # Kurangi epsilon setiap episode
    epsilon = max(min_epsilon, epsilon * decay_rate)

    # Cetak hasil setiap 100 episode
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

# Uji hasil belajar di GUI setelah pelatihan
print("\nMenjalankan demo menggunakan GUI...")

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")
state, _ = env.reset()
done = False
reward = 0

time.sleep(1)

while not done:
    action = np.argmax(q_table[state])
    next_state, reward, terminated, truncated, _ = env.step(action)
    state = next_state
    done = terminated or truncated
    time.sleep(0.5)

print(f"\nDemo selesai. Reward akhir: {reward}")
env.close()
