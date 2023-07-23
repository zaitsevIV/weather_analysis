from file_analysis import received_data
from scatters import max_of_TMax_index, min_of_TMax_index, max_of_TMin_index, min_of_TMin_index
from matplotlib import pyplot as plt

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(16, 9))

ax.plot(received_data['date'], received_data['TMax'], c='red', alpha=0.5)
for scatter in max_of_TMax_index:
    ax.scatter(received_data['date'][scatter], received_data['TMax'][scatter], c='#A60000', edgecolor='none', s=30)
for scatter in min_of_TMax_index:
    ax.scatter(received_data['date'][scatter], received_data['TMax'][scatter], c='#FF7400', edgecolor='none', s=30)

ax.plot(received_data['date'], received_data['TMin'], c='blue', alpha=0.5)
for scatter in max_of_TMin_index:
    ax.scatter(received_data['date'][scatter], received_data['TMin'][scatter], c='#25567B', edgecolor='none', s=30)
for scatter in min_of_TMin_index:
    ax.scatter(received_data['date'][scatter], received_data['TMin'][scatter], c='#002137', edgecolor='none', s=30)

plt.fill_between(received_data['date'], received_data['TMax'], received_data['TMin'], facecolor='#464196', alpha=0.1)

ax.plot(received_data['date'], received_data['TAver'], c='#B53AD4', alpha=0.5)

title = "Daily high and low tempertures - 2022\nSheremetyevo, Moscow"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('weather_Moscow_Sheremetyevo_2022.png')

plt.show()
