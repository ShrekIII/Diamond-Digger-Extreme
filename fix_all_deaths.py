#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Finde alle gameOver = true mit nachfolgendem gameOverReason
i = 0
while i < len(lines):
    line = lines[i]
    
    # Prüfe ob diese Zeile "gameOver = true;" enthält
    if 'gameOver = true;' in line and 'if (playerLives <= 0)' not in line:
        # Schaue nächste Zeile für gameOverReason
        if i + 1 < len(lines) and 'gameOverReason' in lines[i + 1]:
            # Extrahiere Reason
            reason_match = re.search(r"gameOverReason = '([^']+)';", lines[i + 1])
            if reason_match:
                reason = reason_match.group(1)
                # Ersetze beide Zeilen durch eine playerDied() Zeile
                indent = re.match(r'^(\s*)', line).group(1)
                lines[i] = f"{indent}playerDied('{reason}');\n"
                lines[i + 1] = ""  # Lösche gameOverReason Zeile
                print(f"✅ Zeile {i+1}: {reason}")
    
    i += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("\n✅ Alle Deaths gefixt!")
