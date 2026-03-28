# CodigoSecreto-

Generador simple de tarjetas de 5x5 inspiradas en el juego Código Secreto.

## Reglas implementadas
- Tablero 5x5.
- Equipo que inicia: 6 gemas (rombos azules `◆` si empieza azul o cuadrados rojos `■` si empieza rojo).
- Equipo rival: 5 gemas del color contrario.
- 1 infiltrado (`X`).
- Los 13 espacios restantes como guiones (`-`).

## Uso
```bash
python generator.py
```

Para resultados reproducibles, usa una semilla y, si quieres, fija qué equipo empieza:
```python
import random
from generator import generate_card, format_card

rng = random.Random(42)
card = generate_card(rng, active_team="blue")  # \"blue\" o \"red\"
print(format_card(card))
```
