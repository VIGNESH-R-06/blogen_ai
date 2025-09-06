# BLOGEN_AI

BLOGEN_AI is a simple Python library that allows you to generate unique, plagiarism-free blog posts from any topic in seconds.  
It’s designed for content creators, bloggers, and social media managers who want high-quality content without spending hours writing.

---

## 🚀 Features

- Generate blogs from any topic with a single function call.
- Unique and plagiarism-free content.
- Quick and easy to use with minimal setup.
- Supports environment variable configuration for secure API keys.

---

## 💻 Installation

Install the library via pip:

```bash
pip install blogen_ai

```

---
⚙️ Setup & 📖 Usage

Before using, make sure you have a Mistral API key.

Option 1: Using environment variable

Create a .env file in your project root:
```bash
MISTRAL_API_KEY=your_api_key_here

```
Use the library:
```bash
from blogen_ai import genblog

result = genblog("AI in healthcare")
print(result)
```
Option 2: Passing API key directly
```bash
from blogen_ai import genblog

result = genblog("AI in healthcare", api_key="your_api_key_here")
print(result)

```
---


📝 License

This project is licensed under the MIT License. See the LICENSE
 file for details.


---

✅ **Why this README works:**

1. **Simple & professional** – clean headings and minimal text.  
2. **Highlights key features** – easy, unique, plagiarism-free blogs.  
3. **Includes installation & setup instructions** – so users can start quickly.  
4. **Usage example** – shows one simple Python snippet.  
5. **License section** – standard practice for open-source projects.  

---
