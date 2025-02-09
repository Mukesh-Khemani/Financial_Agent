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

2. **`playground.py`**
   - **Purpose**: Creates a user interface (UI) for the financial agent using **Phi Data**.
   - **Functionality**:
     - Enables users to interact with the agent through a graphical interface.
     - Displays stock performance, news, and recommendations in an easy-to-read format.
   - **Usage**: Execute this script to launch the UI.

3. **`testing.py`**
   - **Purpose**: Verifies the presence of the API key (`GROQ_API_KEY`) in the `.env` file.
   - **Functionality**:
     - Ensures the environment is set up correctly before running the project.
     - Prompts for the key if it's missing.
   - **Usage**: Run this script to validate your environment configuration.

4. **`file.py`**
   - **Purpose**: Checks if a specific file exists in the project directory.
   - **Functionality**:
     - Confirms the existence of essential files required for the project.
     - Outputs results for debugging or setup validation.
   - **Usage**: Use this script during project setup or troubleshooting.

5. **`requirements.txt`**
   - **Purpose**: Lists all Python dependencies required for the project.
   - **Usage**: Install dependencies with:
     ```bash
     pip install -r requirements.txt
     ```

6. **`.env`**
   - **Purpose**: Stores sensitive environment variables, including the **GROQ API Key**.
   - **Setup**: Add the following to `.env`:
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

2. **Launch the UI**:
   ```bash
   python playground.py
   ```

3. **Test Environment Setup**:
   ```bash
   python testing.py
   ```

4. **Verify File Presence**:
   ```bash
   python file.py
   ```

---

## **Features**

- **Real-Time Financial Insights**: Analyze stock performance, retrieve news, and access actionable recommendations.
- **Interactive UI**: Engage with the financial agent using a user-friendly graphical interface.
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
- [Phi Data](https://phidata.io) for the user interface framework.
- Open-source contributors for their valuable tools and libraries.

---

For questions or support, please contact [your email/contact info].

