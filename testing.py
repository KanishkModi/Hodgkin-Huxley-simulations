from models import HHModel
from simulations_num_int import Simulation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# customize a neuron model if desired
model = HHModel()
# model.gNa = 100  # typically 120
# model.gK = 5  # typically 36
# model.EK = -35  # typically -12

# customize a stimulus waveform
stim = np.zeros(20000)
stim[7000:13000] = 50  # add a square pulse

#two pulses and a resting potential
# stim[7000:7500] = 50
# stim[13000:13500] = 50
# stim[19000:20000] = 0

# add an absolute sine wave
stim = (np.sin(np.arange(20000) * 0.002)) * 25+50

# add a single pulse
# stim[7000:7100] = 50
# stim[7300:7400] = 50

# simulate the model cell using the custom waveform
sim = Simulation(model)
sim.Run(stimulusWaveform=stim, stepSizeMs=0.01)


# plot the results with MatPlotLib
plt.figure(figsize=(10, 8))

ax1 = plt.subplot(411)
ax1.plot(sim.times, sim.Vm - 70, color='b')
ax1.set_ylabel("Potential (mV)")
ax1.set_title("Hodgkin-Huxley Spiking Neuron Model")

ax2 = plt.subplot(412)
ax2.plot(sim.times, stim, color='r')
ax2.set_ylabel("Stimulation (µA/cm²)")

ax3 = plt.subplot(413, sharex=ax1)
ax3.plot(sim.times, sim.StateH, label='h')
ax3.plot(sim.times, sim.StateM, label='m')
ax3.plot(sim.times, sim.StateN, label='n')
ax3.set_ylabel("Activation (frac)")
ax3.legend()

ax4 = plt.subplot(414, sharex=ax1)
ax4.plot(sim.times, sim.INa, label='VGSC')
ax4.plot(sim.times, sim.IK, label='VGKC')
ax4.plot(sim.times, sim.IKleak, label='KLeak')
ax4.set_ylabel("Current (µA/cm²)")
ax4.set_xlabel("Simulation Time (milliseconds)")
ax4.legend()

# plt.figure(figsize=(15, 5))

# # m vs. Vm
# ax1 = plt.subplot(131)
# ax1.plot(sim.Vm - 70, sim.StateM, color='b')
# ax1.set_xlabel("Potential (mV)")
# ax1.set_ylabel("m Activation")
# ax1.set_title("m vs. Vm Phase Plane Plot")

# # n vs. Vm
# ax2 = plt.subplot(132)
# ax2.plot(sim.Vm - 70, sim.StateN, color='g')
# ax2.set_xlabel("Potential (mV)")
# ax2.set_ylabel("n Activation")
# ax2.set_title("n vs. Vm Phase Plane Plot")

# # h vs. Vm
# ax3 = plt.subplot(133)
# ax3.plot(sim.Vm - 70, sim.StateH, color='r')
# ax3.set_xlabel("Potential (mV)")
# ax3.set_ylabel("h Inactivation")
# ax3.set_title("h vs. Vm Phase Plane Plot")




plt.tight_layout()
plt.show()
