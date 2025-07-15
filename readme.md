# 🐦🎮 Blappy Fird - Pygame Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple, yet feature-rich implementation of the Flappy Bird game, created for educational purposes by a team of four developers. This project demonstrates core game development concepts using the Pygame library.

The code that inspired us: [russs123/flappy_bird](https://github.com/russs123/flappy_bird).

---

### 📜 Table of Contents

*   [✨ Features](#-features)
*   [🔧 Getting Started](#-getting-started)
    *   [Requirements](#requirements)
    *   [Installation](#installation)
*   [🚀 How to Play](#-how-to-play)
*   [🗺️ Development Plan](#-development-plan)
    *   [🇬🇧 English](#english)
    *   [🇵🇱 Polski](#polski)
    *   [🇷🇺 Русский](#русский)
*   [🤝 Contributing](#-contributing)
*   [📝 License](#-license)

> **Note:** This document reflects the project's state upon completion and may be updated with new information.

---

<a name="-features"></a>
### ✨ Key Features

- 🐦 **Classic Gameplay:** Simple and addictive "one-button" mechanics.
- 🎨 **Dynamic Themes:** Automatically switches between day and night themes on each restart.
- 💰 **Coin System:** Collect coins for a bonus score displayed separately during gameplay.
- ⏸️ **Pause Functionality:** Pause the game at any moment by pressing 'P'.
- 🏆 **High Score Tracking:** Your best score is always saved.
- 😂 **Random Death Messages:** A unique, humorous message appears every time you lose.
- 🔊 **Sound Effects:** Immersive sounds for jumping, scoring, collecting coins, and collisions.

---

<a name="-getting-started"></a>
### 🔧 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

#### Requirements

*   🐍 Python 3.8+
*   📦 pip (Python package installer)

#### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/P-Kravtsov/blappy-fird.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd blappy-fird
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

<a name="-how-to-play"></a>
### 🚀 How to Play

1.  Run the game:
    ```bash
    python main.py
    ```
2.  Press `SPACE` to start the game and to make the bird jump.
3.  Press `P` to pause or resume the game.
4.  The game ends when the bird collides with a pipe or the screen boundaries.

---

<a name="-development-plan"></a>
### 🗺️ Development Plan

The project was divided into tasks, with each team member responsible for specific features. Below is the final breakdown of planned and implemented tasks.

[🇬🇧 English](#english) | [🇵🇱 Polski](#polski) | [🇷🇺 Русский](#русский)

<a name="english"></a>
#### 🇬🇧 English

*   **Task 1: Game Core and Bird (Responsible: Pavel Kravtsov)**
    *   ✅ Create the basic project structure and the main game loop.
    *   ✅ Implement the `Bird` class with physics (gravity and jumping).
    *   ✅ Implement bird rotation animation based on its vertical velocity.
    *   ✅ Implement collision detection with screen boundaries.
    *   ✅ Integrate and merge code from all team members.

*   **Task 2: Pipes, Coins, and Collisions (Responsible: Anastasiya Trafimovich)**
    *   ✅ Create the `Pipe` class and implement its movement.
    *   ✅ Implement collision detection between the bird and pipes.
    *   ✅ Implement the scoring system for passing pipes.
    *   ✨ **Implemented:** Added a `Coin` class for a bonus score.
    *   ✨ **Implemented:** Decoupled coin spawning from pipes to make it more random and fair.

*   **Task 3: UI and Game States (Responsible: Nazar Minich)**
    *   ✅ Create "Get Ready" and "Game Over" screens.
    *   ✅ Display the current, final, and bonus coin scores.
    *   ✅ Implement a system for saving and displaying the high score.
    *   ✅ Add pause/resume functionality.
    *   ✨ **Implemented:** Added a variety of random messages on the "Game Over" screen.
    *   ✨ **Implemented:** Created a text-wrapping function to properly display long messages.

*   **Task 4: Environment and Assets (Responsible: Konstantin Leschenko)**
    *   ✅ Set up loading for all images and sounds.
    *   ✅ Implement the scrolling background and ground.
    *   ✅ Integrate sound effects for game events.
    *   ✅ Implement a feature to randomly change themes (day/night) on restart.
    *   ❌ **Not Implemented:** The ability to select different bird skins was postponed.

<a name="polski"></a>
#### 🇵🇱 Polski

*   **Zadanie 1: Rdzeń gry i Ptak (Odpowiedzialny: Pavel Kravtsov)**
    *   ✅ Stworzenie podstawowej struktury projektu i głównej pętli gry.
    *   ✅ Implementacja klasy `Bird` z fizyką (grawitacja i skakanie).
    *   ✅ Implementacja animacji obrotu ptaka w zależności od jego prędkości pionowej.
    *   ✅ Implementacja wykrywania kolizji z granicami ekranu.
    *   ✅ Integracja i połączenie kodu od pozostałych członków zespołu.

*   **Zadanie 2: Rury, Monety i Kolizje (Odpowiedzialny: Anastasiya Trafimovich)**
    *   ✅ Stworzenie klasy `Pipe` i implementacja jej ruchu.
    *   ✅ Implementacja wykrywania kolizji między ptakiem a rurami.
    *   ✅ Implementacja systemu punktacji za przelatywanie przez rury.
    *   ✨ **Zaimplementowano:** Dodano klasę `Coin` dla dodatkowych punktów.
    *   ✨ **Zaimplementowano:** Oddzielono pojawianie się monet od rur, aby było bardziej losowe i sprawiedliwe.

*   **Zadanie 3: Interfejs i Stany gry (Odpowiedzialny: Nazar Minich)**
    *   ✅ Stworzenie ekranów "Get Ready" i "Game Over".
    *   ✅ Wyświetlanie aktualnego, końcowego oraz bonusowego wyniku za monety.
    *   ✅ Implementacja systemu zapisywania i wyświetlania najlepszego wyniku.
    *   ✅ Dodanie funkcji pauzy/wznowienia gry.
    *   ✨ **Zaimplementowano:** Dodano różnorodne losowe komunikaty na ekranie "Game Over".
    *   ✨ **Zaimplementowano:** Stworzono funkcję zawijania tekstu, aby poprawnie wyświetlać długie komunikaty.

*   **Zadanie 4: Otoczenie i Zasoby (Odpowiedzialny: Konstantin Leschenko)**
    *   ✅ Konfiguracja ładowania wszystkich obrazów i dźwięków.
    *   ✅ Implementacja przewijanego tła i ziemi.
    *   ✅ Integracja efektów dźwiękowych dla zdarzeń w grze.
    *   ✅ Implementacja funkcji losowej zmiany motywów (dzień/noc) przy restarcie.
    *   ❌ **Niezrealizowane:** Możliwość wyboru różnych skórek ptaka została odłożona.

<a name="русский"></a>
#### 🇷🇺 Русский

*   **Задача 1: Ядро игры и Птица (Ответственный: Pavel Kravtsov)**
    *   ✅ Создать базовую структуру проекта и основной игровой цикл.
    *   ✅ Реализовать класс `Bird` с физикой (гравитация и прыжок).
    *   ✅ Реализовать анимацию вращения птицы в зависимости от ее вертикальной скорости.
    *   ✅ Реализовать обнаружение столкновений с границами экрана.
    *   ✅ Интегрировать и свести воедино код от всех участников.

*   **Задача 2: Трубы, Монеты и Столкновения (Ответственный: Anastasiya Trafimovich)**
    *   ✅ Создать класс `Pipe` и реализовать его движение.
    *   ✅ Реализовать обнаружение столкновений птицы с трубами.
    *   ✅ Реализовать систему подсчета очков за пролет труб.
    *   ✨ **Реализовано:** Добавлен класс `Coin` для получения бонусных очков.
    *   ✨ **Реализовано:** Появление монет отделено от появления труб, чтобы сделать его более случайным и справедливым.

*   **Задача 3: Интерфейс и Состояния игры (Ответственный: Nazar Minich)**
    *   ✅ Создать экраны "Get Ready" и "Game Over".
    *   ✅ Отображать текущий, финальный и бонусный счет за монеты.
    *   ✅ Реализовать систему сохранения и отображения лучшего результата.
    *   ✅ Добавить функционал паузы/возобновления.
    *   ✨ **Реализовано:** Добавлены разнообразные случайные сообщения на экране "Game Over".
    *   ✨ **Реализовано:** Создана функция переноса текста для корректного отображения длинных сообщений.

*   **Задача 4: Окружение и Ассеты (Ответственный: Konstantin Leschenko)**
    *   ✅ Настроить загрузку всех изображений и звуков.
    *   ✅ Реализовать прокрутку фона и земли.
    *   ✅ Интегрировать звуковые эффекты для игровых событий.
    *   ✅ Реализовать функцию случайной смены тем (день/ночь) при рестарте.
    *   ❌ **Не реализовано:** Возможность выбора разных скинов для птицы была отложена.

---

<a name="-our-team"></a>
### 🧑‍💻 Our Team

This project was brought to life by a team of four developers, simulating a real-world collaborative workflow.

| Name                                                                         | Role                              | Responsibilities                                                                               |
| :--------------------------------------------------------------------------- | :-------------------------------- | :--------------------------------------------------------------------------------------------- |
| **Pavel Kravtsov** ([P-Kravtsov](https://github.com/P-Kravtsov))               | **Team Lead**                     | Core game architecture, bird physics, version control management, and final code integration.  |
| **Anastasiya Trafimovich** ([Nastya-42](https://github.com/Nastya-42)) | **Developer**            | Pipe and coin mechanics, collision systems, and scoring logic.                                 |
| **Nazar Minich** ([Lodems](https://github.com/Lodems))             | **Developer**               | Game state management (start/game over screens), UI elements, and the dynamic message system.  |
| **Konstantin Leschenko** ([Xecuc](https://github.com/Xecuc)) | **Developer** | Asset integration (images, sounds), dynamic theming, and environment animations.               |

---

<a name="-contributing"></a>
### 🤝 Contributing

This project was created for educational purposes and is not currently seeking active contributions. However, you are welcome to fork the repository and explore the code for your own learning.

---

<a name="-license"></a>
### 📝 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.