# SignLanguage
# 🤟 Real-Time Sign Language Translator  

An AI-powered real-time hand gesture recognition system that translates Indian Sign Language into text using deep learning and computer vision.

---

## 🎯 Project Objective  

To bridge the communication gap between hearing-impaired individuals and others by building a system that recognizes sign language gestures in real time and converts them into text.

---

## 🛠️ Technologies & Tools Used  

- **Deep Learning:**  
  - 🧩 **Convolutional Neural Network (CNN):** For spatial feature extraction from gesture images  
  - 🧩 **Recurrent Neural Network (RNN):** For sequence learning of dynamic hand movements  

- **Computer Vision & Hand Tracking:**  
  - 📹 **MediaPipe:** Hand landmark detection (21 key points)  
  - 📷 **OpenCV:** Real-time video capture and frame processing  

- **Natural Language Processing (NLP):**  
  - For context interpretation of recognized gestures  

- **Development Language:** Python  

- **Frameworks/Libraries:** TensorFlow, Keras, OpenCV, MediaPipe  

---

## 📈 Model Architecture & Workflow  

- **CNN:** Extracts spatial hand features  
- **RNN:** Analyzes temporal gesture sequences  
- **MediaPipe + OpenCV:** Handles real-time detection & video capture

  <img width="1108" height="532" alt="image" src="https://github.com/user-attachments/assets/e4055275-1003-408f-97c3-7bb5f90260c0" />


---

## 🗂️ Dataset & Model Training  

- 📊 Trained on **5000+ samples** of Indian Sign Language gestures (ISL dataset & ISL Translate)  
- 🧠 Used CNN for image recognition and RNN for sequential data learning  
- 📈 Achieved **90%+ accuracy** under testing conditions

  <img width="582" height="801" alt="image" src="https://github.com/user-attachments/assets/9f31e7ce-dc95-4ecd-bbbf-c0deb01a642c" />


### Results

<p align="center">
  <img src="https://github.com/user-attachments/assets/3eef3367-418c-45db-ac91-4eef647fc0c6" width="45%" alt="Result 1" />
  <img src="https://github.com/user-attachments/assets/add985a0-c437-43bb-ac32-4e1f0af1003e" width="45%" alt="Result 2" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/8c79049d-e392-4271-975d-5fbc21c06224" width="45%" alt="Result 3" />
  <img src="https://github.com/user-attachments/assets/a1553350-2320-4623-a4f3-7de77fce8b18" width="45%" alt="Result 4" />
</p>



### Challenges Tackled:
- Variability in lighting and backgrounds  
- Real-time gesture recognition accuracy  
- Efficient processing for dynamic hand movements  

---

## 🚀 Features  

- Real-time hand gesture detection and tracking  
- High-precision gesture-to-text conversion  
- Robust against lighting, background changes, and hand positions  
- Privacy-friendly (Processes data locally)  

---

## 🔍 Problem Solved  

Overcomes traditional sign language barriers by providing a technological bridge for real-time communication.  
Addresses limitations in gesture recognition under dynamic, real-world conditions.  

---

## ❓ Sample Questions & Answers  

**Q: Why did you use both CNN and RNN?**  
> CNN is effective for static image feature extraction, while RNN captures the sequence of gestures over time — combining both enables accurate dynamic gesture recognition.

**Q: What role does MediaPipe play in your system?**  
> MediaPipe detects hand landmarks with high precision, which serve as inputs for gesture recognition.

**Q: What challenges did you face during development?**  
> Handling variations in gestures, ensuring real-time processing, and achieving high accuracy under varying conditions.

**Q: How does your system ensure privacy?**  
> All video data is processed locally; nothing is stored or transferred externally.

**Q: Future improvements?**  
> Adding text-to-speech conversion, supporting multiple sign languages, and deploying as a web/mobile application.

---

## 📝 System Requirements  

### Functional Requirements  
- Real-time hand gesture detection using a webcam  
- Spatial feature extraction with CNN  
- Sequential gesture analysis with RNN  

### Non-Functional Requirements  
- High-speed, real-time performance  
- Scalable for multiple sign languages  
- Privacy and data security assurance  
- Reliable operation under varied lighting and background conditions  

---

## 📊 Architecture Diagram  

*(Insert your system architecture diagram here)*  

---

## 📄 References  

- IEEE Conference Papers on Sign Language Recognition  
- MediaPipe, OpenCV, TensorFlow official documentation  

---

**Boya Vijayalakshmi** — [GitHub](https://github.com/Vijayalakshmiboya) | [LinkedIn](https://www.linkedin.com/in/vijayalakshmi-boya)  
---

*“Combining AI with vision technology to create inclusive solutions for communication accessibility.”*  

