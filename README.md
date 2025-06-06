# 🧠 Mental Health Bridge

A Streamlit app to help simulate and improve sensitive conversations about mental health between children and their parents. This tool is designed to bridge generational gaps and enhance emotional understanding using AI.

## 🚀 Features

### 👶 Simulation (for Child)
- Write as yourself (the child) and simulate how a parent might realistically respond.
- Get a **suggested reframed version** of your message to better reach a sensitive or reactive parent.

### 👵 Simulation (for Parent)
- Write as your parent and simulate how a child might respond emotionally.
- See a **rephrased version** of the parent's message in a more emotionally safe way for children.

### 💡 Understand What's Happening
- Ask general questions about mental health, family dynamics, or communication.
- Receive clear, compassionate explanations tailored for emotional sensitivity.

## 🛠️ How It Works

- Uses [Ollama](https://ollama.com/) to run the **Mistral model** locally.
- Real-time responses powered by a prompt-based interaction with the model.
- Sidebar configuration lets you fine-tune the simulated behavior using:
    - **Sensitivity level** (1–10)
    - **Common reactions** (e.g., shuts down, gets anxious)
    - **Preferred tone** (e.g., Calm, Direct, Empathetic)

## 📦 Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io)
- [Ollama](https://ollama.com) running locally with Mistral model installed

## 🔧 Setup Instructions

1. **Clone the repo**
     ```bash
     git clone https://github.com/yourusername/mental-health-bridge.git
     cd mental-health-bridge
     ```

2. **Install dependencies**

     ```bash
     pip install streamlit requests
     ```

3. **Install & run Mistral model locally**
     Make sure [Ollama](https://ollama.com) is installed:

     ```bash
     ollama run mistral
     ```

4. **Run the app**

     ```bash
     streamlit run app.py
     ```

## 🧬 Example Use Case

> You want to tell your parent you're feeling burned out but worry they’ll dismiss it. Use this app to simulate how they might react and get a gentler way to phrase it.

---

## 💙 Why This Matters

Many parents and children struggle to talk about mental health due to generational gaps, emotional barriers, and different communication styles. This tool helps you practice, prepare, and improve those difficult conversations with empathy and realism.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Let’s make mental health conversations more accessible for everyone.

## 📄 License

MIT License

---

Let me know if you want to include screenshots, a logo, or a short demo video link!