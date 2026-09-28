# F1 Aero Digital Twin

A modular Python framework for exploring how aerodynamic setup affects lap performance in a Formula 1-style car. It is an early-stage prototype: the lap-time pipeline runs end to end, while several components (CFD, aero maps, telemetry) are placeholders for future work.

## Overview

The project is organised as a set of small packages, each covering one part of the problem:

```
Aero twin/
├── main.py                 # Example: load a track, run a lap
├── geometry/               # Wing (aerofoil profile), car, floor
├── mesh/                   # PyVista grid generation (placeholder)
├── cfd/                    # Solver, boundary conditions, turbulence, post-processing
├── aero/                   # Force extraction, aero balance, aero maps
├── vehicle/                # Vehicle, aero, tyre, suspension, powertrain parameters
├── tires/                  # Pacejka tyre model
├── dynamics/               # Bicycle model, weight transfer, lateral/longitudinal
├── track/                  # Track loader and track definitions (JSON)
├── simulation/             # Lap simulator, telemetry
├── optimiser/              # Setup optimisation
└── dashboard/              # Streamlit app
```

## Current status

| Component | Status |
|-----------|--------|
| Aerofoil profile generation | Implemented |
| Pacejka lateral tyre force | Implemented |
| Weight transfer, corner speed | Implemented (simple analytic forms) |
| Segment-based lap simulation | Implemented (simplified, see below) |
| Track loading from JSON | Implemented |
| Differential-evolution optimiser | Implemented (generic wrapper, fixed bounds) |
| Vehicle parameter dataclasses | Implemented |
| Streamlit dashboard | Prototype (static values) |
| CFD solver, meshing, force extraction | Placeholder (returns constants or scaled sums, no flow solution) |
| Aero balance, aero maps, telemetry, floor geometry, turbulence, boundary conditions | Not yet implemented |

## Installation

```bash
pip install numpy scipy pyvista streamlit
```

## Usage

Run from the project root:

```bash
python main.py
```

This loads `track/silverstone.json`, runs the lap simulator with the given drag and downforce (in N), and prints the lap time.

Launch the dashboard with:

```bash
streamlit run dashboard/app.py
```

## How the lap simulator works

The track is a list of segments in JSON:

```json
[
  ["straight", 900],
  ["corner", 120, 50],
  ["straight", 700],
  ["corner", 180, 80]
]
```

Straights are `["straight", length_m]` and corners are `["corner", length_m, radius_m]`.

- **Straights** are driven at a fixed 80 m/s.
- **Corners** use a steady-state limit `v = sqrt((downforce + 8000) * radius / mass)`, so more downforce means a higher cornering speed.
- Lap time is the sum of segment length divided by speed.

## Limitations

- The track is a four-segment placeholder, not a real Silverstone layout.
- The `drag` input is currently unused, and straight-line speed does not depend on drag or power.
- There are no braking or acceleration zones, and no tyre model is used in the lap simulator yet.
- The CFD module returns constant fields. Aerodynamic forces are not computed from a real flow solution.
- The dashboard shows hard-coded numbers.
- Several modules are empty files reserved for future work.

## Roadmap

- [ ] Quasi-steady-state lap simulation with braking and acceleration limits
- [ ] Use drag and powertrain limits on straights
- [ ] Connect the Pacejka model and bicycle model to cornering limits
- [ ] Real track data with per-segment curvature
- [ ] Replace the CFD stub with a simple 2D solver or a surrogate model
- [ ] Aero maps (downforce and drag vs ride height and wing angle)
- [ ] Wire the optimiser to lap time
- [ ] Telemetry output and live dashboard

## Tech stack

Python, NumPy, SciPy, PyVista, Streamlit
