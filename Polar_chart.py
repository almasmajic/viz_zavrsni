# In[15]:
import matplotlib.pyplot as plt

# In[16]:
import numpy as np

# In[17]:
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday"]

# In[18]:
actual_calories = [2347, 2587, 2411, 2401, 2464]

# In[19]:
expected_calories = [2500, 2500, 2500, 2500, 2500]

# In[20]:
plt.figure(figsize=(10, 6))
plt.subplot(polar=True)

theta = np.linspace(0, 2 * np.pi, len(actual_calories))

lines, labels = plt.thetagrids(
    range(0, 360, int(360/len(days_of_week))), (days_of_week))

plt.plot(theta, actual_calories)
plt.fill(theta, actual_calories, 'b', alpha=0.1)

plt.plot(theta, expected_calories)

plt.legend(labels=('Actual', 'Expected'), loc=1)
plt.title("Actual VS Expected Calorie Intake")

plt.show()
