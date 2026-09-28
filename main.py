from track.track_loader import load_track
from simulation.lap_simulation import LapSimulator

track = load_track(
    "silverstone.json"
)

sim = LapSimulator()

lap = sim.run(
    track,
    drag=1200,
    downforce=4500
)

print(
    f"Lap Time = {lap:.2f}"
)