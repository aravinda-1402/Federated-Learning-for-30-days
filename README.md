# Federated Learning for 30 Days

Welcome to my 30-day journey into **Federated Learning (FL)**! This repository documents my daily learnings, experiments, and insights as I dive into this exciting domain at the intersection of AI and privacy. 🚀

## 🔍 Why Federated Learning?

Federated Learning is a method for training models on decentralized data while ensuring privacy by keeping the data localized on devices. As data privacy becomes increasingly important, technologies like FL offer a promising way to enable powerful AI without compromising user privacy.

This 30-day plan aims to strengthen my understanding of FL through implementation, experimentation, and research.

---

## 📅 30-Day Plan

### Week 1: Foundations and Basics
- **Day 1 (Nov 21):** 
  - Implement FedAvg with SimpleNN and CNN.  
  - Experiment with client participation levels (25%, 50%, 75%, 100%) and observe accuracy trends.  
  - Study "Communication-Efficient Learning of Deep Networks from Decentralized Data" (McMahan et al., 2017).  

- **Day 2:** 
  - Explore metrics for FL: communication efficiency, convergence rate, and accuracy trade-offs.  
  - Add tracking for these metrics (e.g., rounds vs. accuracy) and visualize trends.  
  - Experiment with varying **local epochs** (e.g., 1, 5, 10) to analyze their impact on convergence and accuracy.  

- **Day 3:** 
  - Simulate **non-IID datasets**:  
    - Create skewed MNIST distributions (e.g., each client has data for specific digits).  
    - Train FedAvg on non-IID data and analyze performance compared to IID datasets.  

- **Day 4:** 
  - Study and implement FedProx ("Federated Optimization in Heterogeneous Networks," Li et al., 2020).  
  - Compare FedProx’s performance with FedAvg on non-IID datasets.  

- **Day 5:** 
  - Study Differential Privacy (DP) in FL:  
    - Read "Deep Learning with Differential Privacy" (Abadi et al., 2016).  
    - Implement DP in your FedAvg setup by adding noise to gradients.  

- **Day 6:** 
  - Experiment with privacy-preserving FL:  
    - Combine Differential Privacy and FedProx for non-IID datasets.  
    - Compare their performance and privacy trade-offs.  

- **Day 7:** 
  - Implement dynamic client participation:  
    - Simulate clients randomly dropping out in each round.  
    - Observe the combined effects of non-IID data and client dropouts on convergence.  

---

### Week 2: Privacy Vulnerabilities and Defenses
- **Day 8:** 
  - Study privacy attacks in FL, focusing on "Deep Leakage from Gradients" (Zhu et al., 2019).  
  - Understand how gradients can leak sensitive client data.  

- **Day 9:** 
  - Implement a gradient inversion attack to reconstruct client-side data from gradients.  

- **Day 10:** 
  - Implement defenses: Differential Privacy and gradient clipping.  
  - Evaluate their effectiveness against gradient inversion attacks.  

- **Day 11:** 
  - Study Secure Aggregation:  
    - Read "Practical Secure Aggregation for Privacy-Preserving Machine Learning" (Bonawitz et al., 2017).  
    - Simulate Secure Aggregation in your FL setup.  

- **Day 12:** 
  - Explore and implement Scaffold (Stochastic Controlled Averaging) to address gradient variance in non-IID settings.  
  - Compare Scaffold’s performance with FedAvg and FedProx.  

- **Day 13:** 
  - Implement client-specific personalization:  
    - Fine-tune the global model on each client’s local dataset and measure the performance boost.  

- **Day 14:** 
  - Experiment with varying data distribution across clients (e.g., highly imbalanced datasets).  
  - Train FL models (FedAvg, FedProx) and compare their performance.  

---

### Week 3: Applications and Advanced Optimization
- **Day 15:** 
  - Study FL applications in healthcare by reading "Federated Learning for Medical Imaging" (Sheller et al., 2020).  
  - Prepare CIFAR-10 or FashionMNIST datasets for a classification task.  

- **Day 16:** 
  - Implement FL for image classification using CNNs on CIFAR-10.  

- **Day 17:** 
  - Study model compression techniques (e.g., quantization and sparsification) in FL:  
    - Read "Federated Learning with Compression" (Konecny et al., 2016).  
    - Implement quantization to reduce communication costs.  

- **Day 18:** 
  - Apply quantization to your FedAvg implementation and analyze the trade-offs between communication efficiency and accuracy.  

- **Day 19:** 
  - Simulate real-world FL challenges:  
    - Introduce stragglers (slower clients) and random client dropouts.  
    - Observe their impact on global model convergence.  

- **Day 20:** 
  - Study FL in edge computing and IoT scenarios:  
    - Summarize challenges like device constraints, latency, and scalability.  
    - Experiment with lightweight models for resource-constrained devices.  

---

### Week 4: SOTA Algorithms and Final Project
- **Day 21:** 
  - Study advanced FL algorithms for non-IID data, such as FedNova (Wang et al., 2020).  
  - Implement FedNova and compare its performance with FedAvg, FedProx, and Scaffold.  

- **Day 22:** 
  - Study adversarial attacks and backdoors in FL:  
    - Read "Backdoor Attacks on Federated Learning" (Bagdasaryan et al., 2020).  

- **Day 23:** 
  - Simulate a backdoor attack on my FL model.  
  - Measure its impact on the global model and client accuracy.  

- **Day 24:** 
  - Implement defenses against backdoor attacks, such as anomaly detection in client updates.  

- **Day 25:** 
  - Explore cross-silo vs. cross-device FL:  
    - Compare their challenges and optimization strategies.  
    - Begin planning my final project.  

- **Day 26:** 
  - Begin --- final project:  
    - Choose a specific FL scenario (e.g., non-IID, privacy enhancement, or adversarial robustness).  
    - Define objectives and design experiments.  

- **Day 27:** 
  - Develop my final project:  
    - Implement the core FL setup and begin running experiments.  

- **Day 28:** 
  - Test and refine my project:  
    - Collect results, visualize performance metrics, and iterate as needed.  

- **Day 29:** 
  - Finalize my project:  
    - Prepare a detailed report with insights, challenges, and outcomes.  

- **Day 30 (Dec 20):** 
  - Share my project:  
 

---

## 🎯 Potential Final Project Ideas

Choose a solid AI/ML-focused FL project that showcases your understanding:
1. **Adversarial Robustness in FL**:  
   - Simulate and defend against gradient inversion or backdoor attacks.  
2. **Personalized FL for Non-IID Data**:  
   - Build a model that adapts to diverse client data distributions.  
3. **Federated Image Classification**:  
   - Train FL models on CIFAR-10 or FashionMNIST for cross-silo settings.  
4. **FL for IoT Devices**:  
   - Create a lightweight FL setup for resource-constrained devices with quantization.  



