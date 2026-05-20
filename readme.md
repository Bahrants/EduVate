# EduVate 🌍

so basically i built a language learning website that focuses on Ethiopian languages but also has some major world languages too. started it as a personal project because i wanted something that actually makes learning Ethiopian languages easier and more accessible

live site: [edu-vate.netlify.app](https://edu-vate.netlify.app)

<br>

## why i built this

i entered this in a government organized tech competition held by one of the Addis Ababa sub-city administrations. the idea was to build something that actually solves a real problem, and for me that was making Ethiopian languages easier to learn and helping preserve them through technology

<br>

## what it does

- **Ethiopian Languages** - Amharic, Oromo, Tigrinya (still working on Somali, Afar, Sidamo)
- **Foreign Languages** - Spanish, Japanese, Korean, German, Russian, English and more
- **AI Assistant** - supposed to help with questions and teach basic phrases in Amharic, Tigrinya, Oromo, English etc. *(still fixing this part)*
- **User accounts** - you can register and login to track progress, streaks, points
- **Resources page** - extra stuff to help with learning
- works on mobile too

<br>

## pages

| route | whats there |
|---|---|
| `/` | landing page + login/register |
| `/start` | Ethiopian language courses |
| `/language` | foreign language courses |
| `/ai` | AI tutor chat |
| `/resources` | study resources |
| `/about` | about the project |
| `/profile` | your profile and progress |

<br>

## tech stack

- just HTML, CSS and JavaScript, no frameworks or anything
- [Vanta.js](https://www.vantajs.com/) for the globe animation on the homepage
- [Three.js](https://threejs.org/) (vanta needs it)
- Font Awesome for icons
- Google Fonts - Inter and Abyssinica SIL
- `localStorage` to save user data and progress
- deployed on [Netlify](https://netlify.com)

<br>

## known issues / stuff im still working on

- AI chat doesnt fully work yet, needs an API key hooked up
- some language courses arent done yet (Somali, Afar, Sidamo)
- planning to build a mobile app eventually
- want to add community features later on

<br>

## project structure

```
/
├── index.html        # landing page
├── start.html        # Ethiopian languages
├── language.html     # foreign languages
├── ai.html           # AI assistant
├── resource.html     # resources
├── about.html        # about page
├── profile.html      # user profile
└── favicon.ico
```

<br>

## running it locally

no setup needed, just open `index.html` in your browser or run a local server:

```bash
npx serve .
# or
python -m http.server 8000
```

<br>

## about

made by me, **Bahran Tsegay**. i built this because i wanted to help preserve Ethiopian languages and make them easier to learn through technology. still a work in progress but getting there

> "Building bridges between cultures through technology-driven language education"
