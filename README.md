# Physics Simulations

A collection of physics simulations built with Python, NumPy, and Pygame.

## Simulations

### Collisions
- **Elastic** - momentum and kinetic energy conserved
- **Inelastic** - momentum conserved, energy lost (coefficient of restitution = 0.7)
- **Perfectly Inelastic** - balls stick together, only momentum conserved

### Pendulum
- **Pendulum Motion** - numerical integration of equation of motion, displays angle, angular velocity, and period

## Requirements
pip install pygame numpy

## Run
```
python collisions/elastic.py
python collisions/inelastic.py
python collisions/perfectly_inelastic.py
python pendulum/pendulum.py
```
