/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //templates at the project level
    "./**/*.py", //templates at the project level
    "./**/templates/**/*.html", //templates at the app level
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

