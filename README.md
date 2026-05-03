# 🎯 Job Hunter

> *Built out of necessity. Because searching for a job shouldn't feel like a full-time job.*

A personal job search tool that connects to job listing APIs, filters vacancies by keyword and location, tracks applications, and provides direct links to job boards across multiple countries — all in one place.

Built with Python and HTML, deployed on Vercel.

---

## 🚀 Live App

[job-hunter-three-ochre.vercel.app](https://job-hunter-three-ochre.vercel.app)

---

## 💡 Why I Built This

As a career switcher actively job hunting, I found myself spending more time managing tabs and job boards than actually applying. So I built a tool to solve my own problem — a single interface to search, filter, save and track job vacancies across multiple platforms and countries.

---

## ✨ Features

- 🔍 **Job search** — search by keyword and location via REST API integration
- 💾 **Application tracker** — save interesting vacancies and track their status
- ➕ **Manual add** — add jobs from any source, not just API results
- 🌍 **Multi-country job boards** — direct links to job boards in the Netherlands, Germany, Spain and Portugal
- ⭐ **Dream companies** — save career pages of companies you want to work for

---

## 🗂️ Project Structure

```
job-hunter/
│
├── backend/          # Python backend — API calls and data handling
├── frontend/         # HTML/CSS frontend — user interface
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python |
| Frontend | HTML / CSS |
| APIs | REST APIs (job listing platforms) |
| Deployment | Vercel |

---

## 🔧 Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/Sarah-Jane85/job-hunter.git
cd job-hunter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables — copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

4. Run the app locally or deploy to Vercel.

---

## 👩‍💻 Author

**Sarah Jane Nede**

Career switcher from operations management to data analytics. Built this tool because the best way to learn is to solve a real problem.
