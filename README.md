# CodigoSecreto-

Generador simple de tarjetas de 5x5 inspiradas en el juego Código Secreto.

## Reglas implementadas
- 6 rombos (♦)
- 5 círculos (O)
- 1 infiltrado (X)
- Los 13 espacios restantes como guiones (-)

## Uso
```bash
python generator.py
```

Para resultados reproducibles, usa una semilla:
```python
import random
from generator import generate_card, format_card

rng = random.Random(42)
card = generate_card(rng)
print(format_card(card))
```
