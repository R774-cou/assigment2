import random

# a. Coin toss simulation
coin_tosses = [random.choice(['Heads', 'Tails']) for _ in range(10000)]
heads = coin_tosses.count('Heads')
tails = coin_tosses.count('Tails')

print("Heads Probability:", heads / 10000)
print("Tails Probability:", tails / 10000)

# b. Rolling two dice and checking sum = 7
dice_sum_7 = 0
for _ in range(10000):
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        dice_sum_7 += 1
print("Probability of sum = 7:", dice_sum_7 / 10000)
# question 2
def prob_at_least_one_six(trials=10000):
    success = 0
    for _ in range(trials):
        rolls = [random.randint(1, 6) for _ in range(10)]
        if 6 in rolls:
            success += 1
    return success / trials

print("Probability of at least one 6 in 10 rolls:", prob_at_least_one_six())

# question 3
colors = ['Red']*5 + ['Green']*7 + ['Blue']*8
prev_blue = 0
red_given_prev_blue = 0

for _ in range(1000):
    first = random.choice(colors)
    second = random.choice(colors)
    if first == 'Blue':
        prev_blue += 1
        if second == 'Red':
            red_given_prev_blue += 1

if prev_blue > 0:
    print("P(Red | Prev Blue):", red_given_prev_blue / prev_blue)
else:
    print("No Blue appeared in first draw.")
# question 4
import numpy as np

values = [1, 2, 3]
probs = [0.25, 0.35, 0.4]
sample = np.random.choice(values, size=1000, p=probs)

mean = np.mean(sample)
variance = np.var(sample)
std_dev = np.std(sample)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

# question 5
import matplotlib.pyplot as plt
from scipy.stats import expon

samples = np.random.exponential(scale=5, size=2000)

# Histogram
plt.hist(samples, bins=50, density=True, alpha=0.6, color='skyblue', label='Histogram')

# PDF overlay
x = np.linspace(0, max(samples), 1000)
plt.plot(x, expon.pdf(x, scale=5), 'r-', label='PDF')
plt.title("Exponential Distribution (mean=5)")
plt.legend()
plt.show()
# question 6
uniform_data = np.random.uniform(0, 1, 10000)
sample_means = []

for _ in range(1000):
    sample = np.random.choice(uniform_data, size=30)
    sample_means.append(np.mean(sample))

# Plotting both distributions
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.hist(uniform_data, bins=50, color='lightgreen', edgecolor='black')
plt.title("Original Uniform Distribution")

plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=50, color='orange', edgecolor='black')
plt.title("Distribution of Sample Means (CLT)")

plt.tight_layout()
plt.show()

