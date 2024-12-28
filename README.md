# Snake, Water, and Gun Game

## Description

This is a Python-based **Snake, Water, and Gun** game where you play against the computer. The game is based on the well-known **Rock, Paper, Scissors** game with a unique twist. You can choose one of three options: **Snake**, **Water**, or **Gun**, and the computer will randomly select one of the three options. The game then decides the winner based on the following rules:

1. **Snake beats Water**.
2. **Water beats Gun**.
3. **Gun beats Snake**.

The game provides voice feedback using the `pyttsx3` library for text-to-speech. It will announce game choices, results, and game instructions.

## Requirements

- **Python** 3.x
- **pyttsx3** library for text-to-speech functionality

You can install the `pyttsx3` library using pip:

```bash
pip install pyttsx3
