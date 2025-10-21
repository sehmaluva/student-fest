# React Lottery Game

Difficulty: Beginner–Intermediate  
Topics: React, Hooks, State, Randomness, UI Components, CSS

## Project description
A modular React app that generates a lottery ticket of n numbers, evaluates a pluggable winning condition, and renders the ticket and the win/lose result through presentational components and scoped CSS. The container manages stateful ticket generation via helper utilities and renders numbers and outcome with a clean separation of concerns.

## Core features
- Configurable ticket size via the `n` prop on `Lottery`.
- Ticket generation using `genTicket(n)` on mount and on user action.
- Winning logic passed as a function prop `winningCondition(ticket)` returning a boolean.
- Presentational components: `Ticket`, `TicketNum`, and `Result` with component-scoped styles.
- Reset-to-zero action `initiallyzeroes` sets ticket to deterministic zeros.
- Styling via `Lottery.css`, `Ticket.css`, and global `index.css`.

## Bonus features (optional)
- Pass custom `winningCondition` implementations to explore game mechanics.
- Modify `genTicket` to change ranges, uniqueness rules, or distributions.
- Introduce reusable button components (e.g., `Btn2`) for consistent actions.
- Side-effect demos (logging/analytics) using `useEffect` similar to the Counter example.

## Tech stack
- React (with `react-dom`, `createRoot`, and `StrictMode`)
- Component-scoped CSS (Lottery.css, Ticket.css) + global `index.css`

## Project structure
```
.
├─ main.jsx
├─ index.css
├─ Lottery.jsx
├─ Lottery.css
├─ Ticket.jsx
├─ Ticket.css
├─ TicketNum.jsx
├─ Result.jsx
├─ Btn2.jsx
├─ Counter.jsx
└─ helper.js
```

## Files and responsibilities
- `Lottery.jsx` — container: state, ticket generation, rule evaluation, handlers for regenerate and zero-initialize.
- `helper.js` — utilities: `genTicket`, `sum`, etc.
- `Ticket.jsx` — presentational: renders the ticket using `TicketNum`.
- `TicketNum.jsx` — displays a single number.
- `Result.jsx` — displays win/lose state.
- `Lottery.css`, `Ticket.css`, `index.css` — component and global styles.
- `Btn2.jsx` — button abstraction (replace or add `Btn1` if referenced).
- `Counter.jsx` — example showing `useState`/`useEffect`.

## Getting started
1. Ensure `App.jsx` exists and renders `Lottery` with `n` and `winningCondition`.
2. Install dependencies and start dev server (example for Vite):
    ```
    npm install
    npm run dev
    ```
3. The container generates an initial ticket with `genTicket(n)` and computes `isWinning` using `winningCondition`.

## Example: App.jsx usage
```jsx
// App.jsx
import Lottery from "./Lottery";

// Example: win if all numbers are identical
const allEqual = (arr) => arr.length > 0 && arr.every((v) => v === arr[0]);

export default function App() {
  return (
     <div>
        <h1>Lottery</h1>
        <Lottery n={3} winningCondition={allEqual} />
     </div>
  );
}
```

## Example winning conditions
```jsx
// 1) Sum equals target
const sumEquals = (target) => (arr) =>
  arr.reduce((a, b) => a + b, 0) === target;

// 2) Contains a specific number
const containsNumber = (x) => (arr) => arr.includes(x);

// 3) Strictly increasing sequence
const strictlyIncreasing = (arr) =>
  arr.every((v, i) => i === 0 || v > arr[i - 1]);
```

## Helper utilities (helper.js)
- `genTicket(n)`: returns an array of length `n` (randomized by default).
- `sum(arr)`: returns sum of numbers in an array.

Example additions:
```js
// helper.js additions
function genTicketInRange(n, min = 0, max = 9) {
  const arr = Array.from({ length: n }, () =>
     Math.floor(Math.random() * (max - min + 1)) + min
  );
  return arr;
}

function hasDuplicates(arr) {
  return new Set(arr).size !== arr.length;
}

export { genTicketInRange, hasDuplicates };
```

## Styling notes
- `Ticket.css`: large font-size for numbers, centered layout, spacing for readability.
- `Lottery.css`: margins and button hover/transform effects.
- `index.css`: global typography, color scheme handling, and consistent button focus/hover states.

## Usage tips
- Swap `winningCondition` functions to test rules without changing the container.
- Use `initiallyzeroes` to set the ticket to `Array(n).fill(0)` for demos, then trigger "buy" to randomize.

## Known gaps / integration notes
- `Lottery.jsx` references `Btn1` but only `Btn2.jsx` is provided — either add `Btn1.jsx` or replace usage with `Btn2` or native buttons.
- `App.jsx` must exist (main.jsx mounts it).
- `Result.jsx` and `TicketNum.jsx` are minimal — ensure they render UI as intended.

## How to contribute
- Extend helpers to adjust number ranges or uniqueness rules.
- Improve ticket visuals and responsive layout.
- Add animations, accessibility improvements, and tests for helpers and container logic.

## Roadmap ideas
- Difficulty modes that change `genTicket` rules and `winningCondition` presets.
- Animations on ticket changes.
- Accessibility enhancements (ARIA, focus order).
- Unit tests for helper functions and container logic.
