import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Car:
    def __init__(self, x=0, v=1, gif=None):
        '''
        gif is guy in front, for those wondering
        '''
        self.x = x
        self.v = v
        self.gif = gif

    def step(self):
        if self.gif:
            self.x = min((self.gif.x + self.x)/2,
                         self.x + self.v)

        else: self.x += self.v

global_v=10
epochs = 1000
p_spawn = 0.5
p_entering = 0.1
x_entering = 500


cars = []
cars.append(Car(v=global_v))


positions = []

for _ in range(epochs):
    # Move the cars
    for car in cars:
        car.step()

    # Spawn new cars
    if np.random.rand() < p_spawn:
        new_car = Car(v=global_v, gif=cars[-1])
        cars.append(new_car)

    # Spawn entering cars
    if np.random.rand() < p_entering:
        gif = None
        for car in cars[::-1]:
            if car.x > x_entering: gif = car

        new_car = Car(x=500, v=global_v, gif=gif)
        cars.append(new_car)

    # Record new positions
    positions.append([car.x for car in cars])


fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    scat = ax.scatter(positions[i], np.ones_like(positions[i]))
    ax.set_xlim(0,1000)
    return scat

ani = animation.FuncAnimation(fig, animate, frames=len(positions)-1,
                                interval=50)
plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots()
# ax.set_xlim([0, 10])
#
# scat = ax.scatter(1, 0)
# x = np.linspace(0, 10)
#
#
# def animate(i):
#     scat.set_offsets((x[i], 0))
#     return scat,
#
# ani = animation.FuncAnimation(fig, animate, repeat=True,
#                                     frames=len(x) - 1, interval=50)
#
# # To save the animation using Pillow as a gif
# # writer = animation.PillowWriter(fps=15,
# #                                 metadata=dict(artist='Me'),
# #                                 bitrate=1800)
# # ani.save('scatter.gif', writer=writer)
#
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# #     scat.set_offsets((positions[i], np.ones_like(positions[i])))
# plt.show()
