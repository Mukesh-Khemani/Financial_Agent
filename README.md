# Financial Agent Project

Welcome to the **Financial Agent Project**, a robust system leveraging **Groq AI** and **Phi Data** to analyze financial data, provide actionable insights, and interact with users via terminal or a UI. The project includes several components that work together seamlessly to achieve these goals.

---

## **Project Structure**

### **Files**

1. **`financial_agent.py`**
   - **Purpose**: Implements a terminal-based financial agent using the **Groq AI** model.
   - **Functionality**:
     - Provides stock analysis.
     - Fetches relevant news and analyst recommendations.
     - Offers actionable financial advice (e.g., Buy, Sell, Hold).
   - **Usage**: Run this script in the terminal to interact with the financial agent directly.

2. **`requirements.txt`**
   - **Purpose**: Lists all Python dependencies required for the project.
   - **Usage**: Install dependencies with:
     ```bash
     pip install -r requirements.txt
     ```

3. **`.env`**
   - **Purpose**: Stores sensitive environment variables, including the **GROQ API Key**.
   - **Setup**: Add the following to `.env`:
   - Create a .env file in the following format:
     GROQ_API_KEY='YOUR_API_KEY'
     
     ```
     GROQ_API_KEY=your_api_key_here
     ```

---

## **Getting Started**

### **Prerequisites**
- Python 3.8+
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Ensure `.env` contains a valid **GROQ_API_KEY**.

---

### **Running the Project**

1. **Run the Financial Agent (Terminal)**:
   ```bash
   python financial_agent.py
   ```

---

## **Features**

- **Real-Time Financial Insights**: Analyze stock performance, retrieve news, and access actionable recommendations.
- **Environment Validation**: Ensure setup correctness with built-in tests.
- **File Validation**: Debug and validate essential files for seamless execution.

---

## **Contributing**

We welcome contributions to improve the Financial Agent Project! To contribute:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Acknowledgments**

- [Groq AI](https://groq.com) for the AI model.
- Open-source contributors for their valuable tools and libraries.

---

For questions or support, please contact [mukeshkhemani222@gmail.com].

