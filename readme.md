# blappy-fird 🐦

[🇬🇧 English](#english) | [🇵🇱 Polski](#polski) | [🇷🇺 Русский](#русский)

---

<a name="english"></a>
## 🇬🇧 blappy-fird - A Student Project (English)

A simple implementation of the Flappy Bird game in Python using the Pygame library. This project is being created for educational purposes by a team of four.

The code that inspired us: [russs123/flappy_bird](https://github.com/russs123/flappy_bird).

### 🗺️ Development Plan

The work is divided into 4 parts.

#### 🎮 Task 1: Game Core and Bird (Responsible: Pavel Kravtsov)

*   **Tasks:**
    1.  🎯 Create the basic project structure and the main game loop.
    2.  🎯 Implement the `Bird` class.
    3.  🎯 Implement bird physics: gravity (constant falling) and jumping (on key press).
    4.  🎯 Implement bird rotation animation based on its vertical velocity.
    5.  🎯 Implement collision detection logic with screen boundaries (ground and ceiling).
    6.  🎯 Integrate and merge the code from other team members.

#### 🧱 Task 2: Pipes and Collisions (Responsible: Anastasiya Trafimovich)

*   **Tasks:**
    1.  🎯 Create the `Pipe` class.
    2.  🎯 Implement the movement of pipes and their generation with a random gap.
    3.  🎯 Implement the collision detection logic between the bird and the pipes.
    4.  🎯 Implement the scoring system (one point for passing a pipe).

#### 🖥️ Task 3: UI and Game States (Responsible: Minich Nazar)

*   **Tasks:**
    1.  🎯 Create a "Get Ready" start screen.
    2.  🎯 Create a "Game Over" screen.
    3.  🎯 Display the current score during the game and the final score on the "Game Over" screen.
    4.  🎯 Implement a system for saving and displaying the high score.
    5.  🎯 Add a pause/resume functionality to the game.

#### 🖼️ Task 4: Environment and Assets (Responsible: Leschenko Konstantin)

*   **Tasks:**
    1.  🎯 Set up loading for all necessary assets: images and sounds.
    2.  🎯 Implement the rendering and "movement" of the background and ground.
    3.  🎯 Integrate sound effects: jump, score, and collision.
    4.  🎯 Implement a feature to randomly change the background (e.g., day/night) at the start of each game.
    5.  🎯 Add the ability to select different bird skins on the start screen.

---

<a name="polski"></a>
## 🇵🇱 blappy-fird - Projekt studencki (Polski)

Prosta implementacja gry Flappy Bird w Pythonie przy użyciu biblioteki Pygame. Projekt ten jest tworzony w celach edukacyjnych przez czteroosobowy zespół.

Kod, który nas zainspirował: [russs123/flappy_bird](https://github.com/russs123/flappy_bird).

### 🗺️ Plan rozwoju

Praca jest podzielona na 4 części.

#### 🎮 Zadanie 1: Rdzeń gry i Ptak (Odpowiedzialny: Pavel Kravtsov)

*   **Zadania:**
    1.  🎯 Stworzenie podstawowej struktury projektu i głównej pętli gry.
    2.  🎯 Implementacja klasy `Bird` (ptak).
    3.  🎯 Implementacja fizyki ptaka: grawitacja (ciągłe opadanie) i skok (po naciśnięciu klawisza).
    4.  🎯 Implementacja animacji obrotu ptaka w zależności od jego prędkości pionowej.
    5.  🎯 Implementacja logiki wykrywania kolizji z granicami ekranu (ziemia i sufit).
    6.  🎯 Integracja i połączenie kodu od pozostałych członków zespołu.

#### 🧱 Zadanie 2: Rury i Kolizje (Odpowiedzialny: Anastasiya Trafimovich)

*   **Zadania:**
    1.  🎯 Stworzenie klasy `Pipe` (rura).
    2.  🎯 Implementacja ruchu rur i ich generowania z losową przerwą.
    3.  🎯 Implementacja logiki wykrywania kolizji między ptakiem a rurami.
    4.  🎯 Implementacja systemu punktacji (jeden punkt za przelecenie przez rurę).

#### 🖥️ Zadanie 3: Interfejs i Stany gry (Odpowiedzialny: Minich Nazar)

*   **Zadania:**
    1.  🎯 Stworzenie ekranu startowego ("Get Ready").
    2.  🎯 Stworzenie ekranu "Game Over".
    3.  🎯 Wyświetlanie aktualnego wyniku podczas gry oraz końcowego wyniku na ekranie "Game Over".
    4.  🎯 Implementacja systemu zapisywania i wyświetlania najlepszego wyniku.
    5.  🎯 Dodanie funkcji pauzy/wznowienia gry.

#### 🖼️ Zadanie 4: Otoczenie i Zasoby (Odpowiedzialny: Leschenko Konstantin)

*   **Zadania:**
    1.  🎯 Konfiguracja ładowania wszystkich niezbędnych zasobów: obrazów i dźwięków.
    2.  🎯 Implementacja renderowania i "ruchu" tła oraz ziemi.
    3.  🎯 Integracja efektów dźwiękowych: skok, zdobycie punktu i kolizja.
    4.  🎯 Implementacja funkcji losowej zmiany tła (np. dzień/noc) na początku każdej gry.
    5.  🎯 Dodanie możliwości wyboru różnych skórek ptaka na ekranie startowym.

---

<a name="русский"></a>
## 🇷🇺 blappy-fird - Учебный проект (Русский)

Простая реализация игры Flappy Bird на Python с использованием библиотеки Pygame. Этот проект создается в учебных целях командой из четырех человек.

Код, который нас вдохновил: [russs123/flappy_bird](https://github.com/russs123/flappy_bird).

### 🗺️ План разработки

Работа разделена на 4 части.

#### 🎮 Задача 1: Ядро игры и Птица (Ответственный: Pavel Kravtsov)

*   **Задачи:**
    1.  🎯 Создать базовую структуру проекта и основной игровой цикл.
    2.  🎯 Реализовать класс для птицы (`Bird`).
    3.  🎯 Реализовать физику птицы: гравитация (постоянное падение) и прыжок (по нажатию клавиши).
    4.  🎯 Реализовать анимацию вращения птицы в зависимости от ее вертикальной скорости.
    5.  🎯 Реализовать логику обнаружения столкновений с границами экрана (земля и потолок).
    6.  🎯 Интегрировать и свести воедино код от других участников.

#### 🧱 Задача 2: Трубы и Столкновения (Ответственный: Anastasiya Trafimovich)

*   **Задачи:**
    1.  🎯 Создать класс для труб (`Pipe`).
    2.  🎯 Реализовать движение труб и их генерацию со случайным просветом.
    3.  🎯 Реализовать логику обнаружения столкновений птицы с трубами.
    4.  🎯 Реализовать систему подсчета очков (очко за пролет трубы).

#### 🖥️ Задача 3: Интерфейс и Состояния игры (Ответственный: Minich Nazar)

*   **Задачи:**
    1.  🎯 Создать стартовый экран ("Get Ready").
    2.  🎯 Создать экран "Game Over".
    3.  🎯 Отображать текущий счет во время игры и финальный счет на экране "Game Over".
    4.  🎯 Реализовать систему сохранения и отображения лучшего результата.
    5.  🎯 Добавить в игру функционал паузы/возобновления.

#### 🖼️ Задача 4: Окружение и Ассеты (Ответственный: Leschenko Konstantin)

*   **Задачи:**
    1.  🎯 Настроить загрузку всех необходимых ассетов: изображений и звуков.
    2.  🎯 Реализовать отрисовку и "движение" фона и земли.
    3.  🎯 Интегрировать звуковые эффекты: прыжок, получение очка и столкновение.
    4.  🎯 Реализовать функцию случайной смены фона (например, день/ночь) в начале каждой игры.
    5.  🎯 Добавить возможность выбора разных скинов птицы на стартовом экране.