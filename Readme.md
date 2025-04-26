# 📜 NPC Generator

**_"Where Every Character Has a Story."_**

---

**NPC Generator** is a web-based application that allows users to randomly create NPC (Non-Player Character) profiles for different gaming systems.  
It is designed to support both **universal systems** (global) and **user-specific custom systems**.

This project uses:

- **Frontend:** React / Next.js
- **Backend:** Python / Django
- **Database:** MySQL or PostgreSQL (depending on deployment)

---

## 🎭 Project Philosophy

Unlike traditional "stat block" generators that focus heavily on combat stats, numbers, and game mechanics,  
**NPC Generator** is opinionated toward a **storytelling-first** approach.

The goal is to **enrich world-building** and **deepen character immersion** by focusing on elements like:

- Characteristic traits (personality, quirks)
- Deep wants, needs, and motivations
- Physical appearance (hair, eyes, scars, height, build)
- Gender, age categories, and race/species
- Professions and vocations
- Hometowns, regions, and locations
- Social groupings and cultural classifications

In short:  
> **_"More about who they are, rather than just what they can do."_**

---

## ✨ Features

- Create and browse **Global Systems** (available to all users).
- Create **Custom Systems** visible only to you.
- Automatically generate rich, story-driven NPCs.
- Future expansions: user-created templates, profession generators, relationship webs, and more!

---

## 🗂️ Current Backend Model: `System`

The `System` model represents the different RPG/game systems users can generate NPCs for.

| Field | Purpose |
|:------|:--------|
| `system_name` | Name of the system (e.g., "D&D 5e", "Starfinder", "Custom Homebrew"). |
| `description` | Short description of the system. |
| `is_global` | Boolean flag — true if this system is available to everyone. |
| `owner` | The user who created a private/custom system (null for global systems). |
| `created_at` | When it was created. |
| `updated_at` | When it was last modified. |

---

## ⚙️ Quick Tech Overview

- **Django REST Framework** for API endpoints
- **Next.js (React)** frontend for dynamic and interactive page experiences
- **MySQL or PostgreSQL** for database management
- **Authentication** using Django's built-in auth system (expandable to JWT or OAuth if needed)

---

## 🔮 Future Vision

- Expand NPC generation with **modular templates**.
- Allow **user-driven system sharing** (private group visibility).
- Add **AI-assisted character traits** and plot hooks.
- Include **visual avatars** and **symbolic descriptions** using AI imagery or custom uploads.
- Enable **"community systems"** where multiple users collaborate on a custom world.

---

## 🤝 Contributing

This is an early-stage project!  
Feature requests, ideas, and creative brainstorming are welcome.  
Pull Requests will be reviewed thoughtfully — storytelling-first designs are prioritized!

---

> **Remember:** In every world, characters are the heart of the story.  
> Stats may tell you how strong they are.  
> But stories tell you **why** they fight.

---
