/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/dashboard.html',
    './templates/*/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@themesberg/flowbite/plugin'),
  ],
}
