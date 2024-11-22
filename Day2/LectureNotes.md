# **Privacy-Preserving AI: Notes**

## **Overview**
This lecture by Andrew Trask explores the potential and impact of privacy-preserving AI technologies. It focuses on techniques enabling secure computations on sensitive data without direct access, such as differential privacy, federated learning, and secure multi-party computation (SMPC).

---

## **Key Concepts and Questions**
1. **Core Question:**  
   *"Is it possible to answer questions using data we cannot see?"*  
   This is the foundation of privacy-preserving AI, addressing the need to use sensitive data without compromising its privacy.

2. **Challenges with Sensitive Data:**  
   - Difficulty in accessing, sharing, and using private data (e.g., healthcare, financial data).  
   - High costs and legal/ethical risks associated with handling such data.  

3. **Vision:**  
   Enabling AI systems to process sensitive datasets securely while ensuring privacy and usability.  

---

## **Techniques in Privacy-Preserving AI**

### 1️⃣ **Remote Execution**
- **Definition:** Perform computations on a remote machine (e.g., a hospital data server) without accessing the raw data.
- **How It Works:**  
  - Data remains on the remote machine.  
  - Computations are performed via pointers to data, ensuring no direct access.  
  - Example: PySyft extends PyTorch with `torch.send()` and `torch.get()` for remote tensor computations.  

- **Advantages:**  
  - Allows initial data science steps like feature engineering remotely.  

- **Limitations:**  
  - Security bottleneck: If improperly implemented, raw data can still be accessed via naive queries.

---

### 2️⃣ **Differential Privacy (DP)**
- **Definition:** Add controlled noise to data or query results to protect individual records in a dataset.
- **Key Concepts:**  
  - **Sensitivity:** Measures how much a query's output changes if a single record is added or removed.  
  - **Privacy Budget (Epsilon):** Controls the amount of allowable noise. A lower epsilon implies stricter privacy.  

- **Techniques Used:**  
  - Randomized Response: Add randomness to user responses to anonymize individual contributions while maintaining statistical trends.  
  - Noise Injection: Ensures individual-level information cannot be inferred from outputs.

- **Applications:**  
  - Census data protection, healthcare analytics, and sensitive survey analyses.  

---

### 3️⃣ **Secure Multi-Party Computation (SMPC)**
- **Definition:** Multiple parties collaboratively compute a function over their inputs without revealing them to each other.  
- **Key Features:**  
  - Data is split into "shares" distributed among participants.  
  - Computations occur on encrypted shares, and results remain encrypted until decryption is agreed upon.  

- **Use Case:**  
  - Collaborating on sensitive datasets across institutions (e.g., hospitals) without sharing raw data.  

---

### 4️⃣ **Federated Learning (FL)**
- **Definition:** Decentralized learning where data remains on local devices, and only model updates are shared.  
- **Example:** Google's implementation on smartphones for predictive text (e.g., next-word prediction).  

- **Types of FL:**  
  - **Fixed Model, Ephemeral Data:** Data (e.g., smartphone activity) trains a fixed model.  
  - **Exploratory FL:** Data is hosted across organizations, and data scientists query models for specific analyses.

- **Challenges:**  
  - Potential leakage of sensitive data through shared updates.  
  - Requires differential privacy to ensure secure parameter sharing.

---

## **End-to-End Encrypted Services**
- **Vision:** Provide AI-based services (e.g., healthcare diagnoses) without exposing data to service providers.  
- **Process:**  
  - Inputs (e.g., medical data) and model parameters are encrypted.  
  - Computations occur on encrypted data.  
  - Results are decrypted only by the end user.  

- **Example:**  
  - Skin cancer detection using an encrypted model and encrypted patient data, ensuring privacy for both parties.

---

## **Applications and Impact**
1. **Open Science:**  
   - Unlocking datasets for medical research while ensuring privacy.  
   - Example: Aggregating non-centralized data for dementia research across hospitals.  

2. **Accountability Systems:**  
   - Replace invasive monitoring systems (e.g., bag checks) with privacy-preserving alternatives (e.g., AI-based screening).  

3. **Enhanced Services:**  
   - Enabling encrypted services across industries (e.g., healthcare, finance).  

4. **Holistic Recommendation Systems:**  
   - Personalize recommendations (e.g., health suggestions) securely without compromising sensitive information.

---

## **Limitations and Future Work**
1. **Computational Complexity:**  
   - Encrypted computations are slower (e.g., 13x for deep learning predictions) but improving.  

2. **Infrastructure Challenges:**  
   - Requires better tools, faster networks, and adoption of privacy-preserving technologies.  

3. **Adoption Barriers:**  
   - Enterprises need to recognize commercial and ethical benefits.  
   - Individuals need tools to manage personal privacy budgets effectively.  

---

## **Conclusion**
Andrew Trask’s talk emphasizes that privacy-preserving AI is not just about protecting data but unlocking its potential responsibly. By leveraging techniques like differential privacy, FL, and SMPC, we can democratize access to data for critical research while ensuring trust and compliance.

---

## **Further Reading and Resources**
1. [PySyft Documentation](https://github.com/OpenMined/PySyft)  
2. *“Deep Learning with Differential Privacy”* (Abadi et al., 2016)  
3. [Federated Learning Overview (Google)](https://ai.googleblog.com/2017/04/federated-learning-collaborative.html)  
4. Andrew Trask’s Community: [OpenMined](https://www.openmined.org/)  
