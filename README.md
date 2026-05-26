Machine Learning Image Captioning System

<img width="1763" height="844" alt="image" src="https://github.com/user-attachments/assets/0d6df4cb-012a-4192-881f-72f79390854e" />


Image captioning is a challenging task in the fields of computer vision and natural language processing that involves automatically generating descriptive captions for images. This project implements an intelligent image captioning system using deep learning techniques with the BLIP (Bootstrapping Language-Image Pre-training) model.

The system generates meaningful textual descriptions for uploaded images and allows users to customize caption generation settings such as caption length and beam search quality. A user-friendly web interface is developed using the Python library Streamlit, enabling users to upload images, generate captions, download results, and save captions for dataset creation.

This project demonstrates the practical application of transformer-based AI models in connecting visual understanding with natural language generation. Such systems have real-world applications in accessibility tools for visually impaired users, automated image tagging, content management systems, and media description automation.

Requirements
Operating System: Windows 10/11, Linux, macOS
Programming Language: Python 3.8 or above
Required Libraries: streamlit, PIL (Pillow), torch, transformers, io, matplotlib, pandas, collections.Counter
Models Used:
  -Salesforce/blip-image-captioning-base
  -Salesforce/blip-image-captioning-large

Steps to Build and Run the Project
Step 1: Create Python File

Copy and paste the provided code into a Python file.

Example: app.py

Step 2: Install Required Libraries

Open terminal or command prompt and run: pip install streamlit pillow torch transformers matplotlib pandas

Step 3: Run the Project

Open terminal in the project folder and run:

python -m streamlit run app.py

 this path will locate in browser using local URL:
 
 <img width="1005" height="566" alt="image" src="https://github.com/user-attachments/assets/f649aa8d-0681-4ed8-badb-1ef4cef3ff37" />

<img width="1005" height="566" alt="image" src="https://github.com/user-attachments/assets/82ecce63-473a-4b21-bbcc-a33ee6940277" />

<img width="1005" height="566" alt="image" src="https://github.com/user-attachments/assets/b35e69b2-e559-47c1-b08f-69642a3ca7fe" />



Features of the System
-Upload images (jpg, jpeg, png)
-Generate AI-based image captions
-Select different BLIP models
-Customize beam search and caption length
-Download generated captions
-Save captions into CSV dataset

Applications
-Accessibility tools for visually impaired users
-Automatic image annotation
-Social media content generation
-Smart photo organization systems
-AI-powered media management

Conclusion

The Image Captioning System successfully combines computer vision and natural language processing techniques to generate descriptive captions from images. Using transformer-based BLIP models improves caption quality and contextual understanding. The Streamlit interface makes the system interactive, simple to use, and suitable for practical real-world applications.
