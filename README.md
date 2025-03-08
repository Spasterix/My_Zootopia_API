# 🦁 My_Zootopia_API

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![API Ninjas](https://img.shields.io/badge/API-Ninjas-orange.svg)](https://api-ninjas.com/api/animals)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A dynamic web-based animal information system that fetches and displays detailed data about various animals using the API Ninjas Animals API. Perfect for educational purposes, wildlife enthusiasts, and anyone interested in learning about different animal species.

## ✨ Features

- 🔍 Search for any animal species
- 🌍 View detailed information including:
  - Diet
  - Natural habitat
  - Animal type
  - Skin type
  - Lifespan
- 📊 Filter results by multiple criteria
- 💻 Clean and responsive web interface
- 🛡️ Secure API key management
- ❌ Helpful error handling

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Spasterix/My_Zootopia_API.git
cd My_Zootopia_API
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your API Ninjas key:
```
API_KEY=2qYo05vUXwQ7kIzQsLXiPQ==CyTuRDBQJ0ybXNUT
```

## 🎮 Usage

1. Run the program:
```bash
python animals_web_generator.py
```

2. Follow the interactive prompts:
   - Enter an animal name to search
   - Choose filtering options if desired
   - View the generated HTML file in your browser

## 🛠️ Project Structure

```
My_Zootopia_API/
├── animals_web_generator.py  # Main application file
├── data_fetcher.py          # API interaction module
├── animals_template.html    # HTML template
├── requirements.txt        # Project dependencies
├── .env                   # API key configuration
└── .gitignore            # Git ignore rules
```

## 🔑 Environment Variables

The project uses the following environment variables:
- `API_KEY`: Your API Ninjas API key (required)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [API Ninjas](https://api-ninjas.com/) for providing the Animals API
- All contributors and users of this project

## 📞 Contact

If you have any questions or suggestions, feel free to open an issue or contact the maintainers.

---
Made with ❤️ by Alexander Krause 