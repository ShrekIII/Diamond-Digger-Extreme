#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Ersetze alle gameOver = true durch playerDied() mit passendem Grund
replacements = [
    # Monster Kollisionen
    (r"gameOver = true;\s*gameOverReason = '💀 Killed by Monster';", "playerDied('💀 Killed by Monster');"),
    # Explosion
    (r"gameOver = true;\s*gameOverReason = '💥 Explosion';", "playerDied('💥 Explosion');"),
    # Zeit abgelaufen
    (r"gameOver = true;\s*gameOverReason = '⏱️ Time Over';", "playerDied('⏱️ Time Over');"),
    # Stein-Tod
    (r"gameOver = true;\s*gameOverReason = '🪨 Crushed by Stone';", "playerDied('🪨 Crushed by Stone');"),
    # Suicide
    (r"gameOver = true;\s*gameOverReason = '🚪 Suicide';", "playerDied('🚪 Suicide');"),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Death logic replaced")
