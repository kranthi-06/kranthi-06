<div align="center">
  <picture>
    <img src="assets/hero.svg" alt="Hero Banner" width="100%" />
  </picture>
</div>

<br/>

<div align="center">
  <picture>
    <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&duration=3000&pause=1000&color=60A5FA&center=true&vCenter=true&width=700&lines=Architecting+Scalable+Software;Building+Production-Grade+AI;Crafting+Premium+User+Experiences;Turning+Complex+Problems+into+Elegant+Solutions" alt="Typing Effect" />
  </picture>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-gradient.svg" width="800" alt="Divider" />
  </picture>
</div>

<div align="center">
  <h2>Mission</h2>
  <p align="center" style="color: #94A3B8; font-size: 16px; line-height: 1.6; max-width: 700px; margin: 0 auto;">
    To build software that scales globally. As an AI Engineer and Full Stack Developer, I bridge the gap between complex machine learning models and intuitive, high-performance applications.
  </p>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-dots.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Live Engineering Dashboard</h2>

<div align="center">
  <p style="color: #64748B;"><i>Telemetry automatically updated via GitHub Actions. Last Updated: {{ date }}</i></p>
  <picture>
    <img src="assets/dashboard.svg" width="1000" alt="Engineering Dashboard" />
  </picture>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-gradient.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Deployment Status</h2>

<div align="center">
  {% for dep in deployments %}
  <p>
    <b>{{ dep.name }}</b> &nbsp;&middot;&nbsp; 
    {% if dep.status == "ONLINE" %}
    🟢 Online
    {% elif dep.status == "COMING SOON" %}
    🟡 Coming Soon
    {% else %}
    🔴 Offline
    {% endif %}
    &nbsp;&middot;&nbsp; <i>{{ dep.tech }}</i> 
    {% if dep.url %}
    &nbsp;&middot;&nbsp; <a href="{{ dep.url }}">Open</a>
    {% endif %}
  </p>
  {% endfor %}
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-dots.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Featured Products</h2>

<br/>

<!-- LakshyaTrack -->
<div align="center">
  <a href="https://lakshyatrack.vercel.app/">
    <img src="assets/project-lakshya.svg" width="900" alt="LakshyaTrack Preview" />
  </a>
  <br/><br/>
  <h3>🎯 LakshyaTrack</h3>
  <p style="color: #94A3B8;"><i>High-performance telemetry and goal-tracking architecture.</i></p>
  <p>
    <b>Stack:</b> <img src="https://img.shields.io/badge/Next.js-1E293B?style=flat-square&logo=next.js&logoColor=60A5FA" alt="Next.js"/> <img src="https://img.shields.io/badge/TypeScript-1E293B?style=flat-square&logo=typescript&logoColor=60A5FA" alt="TypeScript"/>
  </p>
  <a href="https://lakshyatrack.vercel.app/"><img src="https://img.shields.io/badge/Live_Demo-0F172A?style=for-the-badge&logo=vercel&logoColor=white&color=2563EB" alt="Live Demo" /></a>
</div>

<br/><br/>

<!-- AI Plant Disease -->
<div align="center">
  <a href="https://ai-plant-disease-analysis.vercel.app/">
    <img src="assets/project-plant.svg" width="900" alt="AI Plant Disease Analysis" />
  </a>
  <br/><br/>
  <h3>🌱 AI Plant Disease Analysis</h3>
  <p style="color: #94A3B8;"><i>Computer Vision model for real-time plant disease detection.</i></p>
  <p>
    <b>Stack:</b> <img src="https://img.shields.io/badge/PyTorch-1E293B?style=flat-square&logo=pytorch&logoColor=60A5FA" alt="PyTorch"/> <img src="https://img.shields.io/badge/OpenCV-1E293B?style=flat-square&logo=opencv&logoColor=60A5FA" alt="OpenCV"/>
  </p>
  <a href="https://ai-plant-disease-analysis.vercel.app/"><img src="https://img.shields.io/badge/Live_Demo-0F172A?style=for-the-badge&logo=vercel&logoColor=white&color=2563EB" alt="Live Demo" /></a>
</div>

<br/><br/>

<!-- Portfolio -->
<div align="center">
  <a href="https://kasakranthikiran.vercel.app">
    <img src="assets/project-portfolio.svg" width="900" alt="Portfolio Website" />
  </a>
  <br/><br/>
  <h3>💼 Professional Portfolio</h3>
  <p style="color: #94A3B8;"><i>Award-winning personal portfolio built with modern WebGL and Framer.</i></p>
  <p>
    <b>Stack:</b> <img src="https://img.shields.io/badge/Framer_Motion-1E293B?style=flat-square&logo=framer&logoColor=60A5FA" alt="Framer Motion"/> <img src="https://img.shields.io/badge/React-1E293B?style=flat-square&logo=react&logoColor=60A5FA" alt="React"/>
  </p>
  <a href="https://github.com/kranthi-06/Portfolio"><img src="https://img.shields.io/badge/GitHub-1E293B?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://kasakranthikiran.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-0F172A?style=for-the-badge&logo=vercel&logoColor=white&color=2563EB" alt="Live Demo" /></a>
</div>

<br/><br/>

<!-- Emergent -->
<div align="center">
  <a href="https://emergent-theta.vercel.app/dashboard">
    <img src="assets/project-emergent.svg" width="900" alt="Emergent Smart Agriculture" />
  </a>
  <br/><br/>
  <h3>🌾 Emergent</h3>
  <p style="color: #94A3B8;"><i>Smart Agriculture IoT & AI integrated crop monitoring system.</i></p>
  <p>
    <b>Stack:</b> <img src="https://img.shields.io/badge/IoT-1E293B?style=flat-square&logo=arduino&logoColor=60A5FA" alt="IoT"/> <img src="https://img.shields.io/badge/React-1E293B?style=flat-square&logo=react&logoColor=60A5FA" alt="React"/>
  </p>
  <a href="https://github.com/kranthi-06/emergent"><img src="https://img.shields.io/badge/GitHub-1E293B?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://emergent-theta.vercel.app/dashboard"><img src="https://img.shields.io/badge/Live_Demo-0F172A?style=for-the-badge&logo=vercel&logoColor=white&color=2563EB" alt="Live Demo" /></a>
</div>

<br/><br/>

<!-- Speech to Sign -->
<div align="center">
  <picture>
    <img src="assets/project-speech.svg" width="900" alt="Speech to Sign Language Converter" />
  </picture>
  <br/><br/>
  <h3>🤟 Speech to Sign Language</h3>
  <p style="color: #94A3B8;"><i>Deep learning NLP pipeline converting speech to 3D sign language.</i></p>
  <p>
    <b>Stack:</b> <img src="https://img.shields.io/badge/TensorFlow-1E293B?style=flat-square&logo=tensorflow&logoColor=60A5FA" alt="TensorFlow"/> <img src="https://img.shields.io/badge/Python-1E293B?style=flat-square&logo=python&logoColor=60A5FA" alt="Python"/>
  </p>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-dots.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Technology Architecture</h2>

<br/>

<div align="center">
  <p><b>Core Languages</b></p>
  <picture><img src="https://img.shields.io/badge/Python-1E293B?style=for-the-badge&logo=python&logoColor=60A5FA" alt="Python" /></picture>
  <picture><img src="https://img.shields.io/badge/TypeScript-1E293B?style=for-the-badge&logo=typescript&logoColor=60A5FA" alt="TypeScript" /></picture>
  <picture><img src="https://img.shields.io/badge/JavaScript-1E293B?style=for-the-badge&logo=javascript&logoColor=60A5FA" alt="JavaScript" /></picture>
  <picture><img src="https://img.shields.io/badge/C++-1E293B?style=for-the-badge&logo=c%2B%2B&logoColor=60A5FA" alt="C++" /></picture>
  <picture><img src="https://img.shields.io/badge/Go-1E293B?style=for-the-badge&logo=go&logoColor=60A5FA" alt="Go" /></picture>
</div>

<div align="center">
  <p><b>AI & Machine Learning</b></p>
  <picture><img src="https://img.shields.io/badge/PyTorch-1E293B?style=for-the-badge&logo=pytorch&logoColor=2563EB" alt="PyTorch" /></picture>
  <picture><img src="https://img.shields.io/badge/TensorFlow-1E293B?style=for-the-badge&logo=tensorflow&logoColor=2563EB" alt="TensorFlow" /></picture>
  <picture><img src="https://img.shields.io/badge/OpenAI-1E293B?style=for-the-badge&logo=openai&logoColor=2563EB" alt="OpenAI" /></picture>
  <picture><img src="https://img.shields.io/badge/HuggingFace-1E293B?style=for-the-badge&logo=huggingface&logoColor=2563EB" alt="HuggingFace" /></picture>
  <picture><img src="https://img.shields.io/badge/OpenCV-1E293B?style=for-the-badge&logo=opencv&logoColor=2563EB" alt="OpenCV" /></picture>
</div>

<div align="center">
  <p><b>Frontend & Infrastructure</b></p>
  <picture><img src="https://img.shields.io/badge/Next.js-1E293B?style=for-the-badge&logo=next.js&logoColor=60A5FA" alt="Next.js" /></picture>
  <picture><img src="https://img.shields.io/badge/React-1E293B?style=for-the-badge&logo=react&logoColor=60A5FA" alt="React" /></picture>
  <picture><img src="https://img.shields.io/badge/Node.js-1E293B?style=for-the-badge&logo=nodedotjs&logoColor=2563EB" alt="Node.js" /></picture>
  <picture><img src="https://img.shields.io/badge/PostgreSQL-1E293B?style=for-the-badge&logo=postgresql&logoColor=2563EB" alt="PostgreSQL" /></picture>
  <picture><img src="https://img.shields.io/badge/Docker-1E293B?style=for-the-badge&logo=docker&logoColor=2563EB" alt="Docker" /></picture>
  <picture><img src="https://img.shields.io/badge/AWS-1E293B?style=for-the-badge&logo=amazonaws&logoColor=2563EB" alt="AWS" /></picture>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-gradient.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Coding Profiles</h2>

<div align="center">
  <p>
    <b>LeetCode:</b> <picture><img src="https://img.shields.io/badge/Solved-{{ lc.solved }}-FFA116?style=flat-square&logo=leetcode&logoColor=white" /></picture> <i>(Rank: {{ lc.ranking }})</i>
    <br/><br/>
    <b>HackerRank:</b> <a href="https://www.hackerrank.com/profile/kasakk2006"><img src="https://img.shields.io/badge/Profile-Active-00EA64?style=flat-square&logo=hackerrank&logoColor=white" /></a> <i>(Top Rated)</i>
    <br/><br/>
    <b>Kaggle:</b> <a href="https://www.kaggle.com/kasakranthi"><img src="https://img.shields.io/badge/Profile-Active-20BEFF?style=flat-square&logo=kaggle&logoColor=white" /></a> <i>(Datasets & Notebooks)</i>
  </p>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-dots.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Contribution Graph</h2>

<div align="center">
  <picture>
    <img src="assets/snake.svg" alt="Contribution Graph" width="100%" />
  </picture>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/divider-gradient.svg" width="800" alt="Divider" />
  </picture>
</div>

<h2 align="center">Connect</h2>

<div align="center">
  <a href="https://github.com/kranthi-06">
    <img src="https://img.shields.io/badge/GitHub-1E293B?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://www.linkedin.com/in/kasakranthikiran06/">
    <img src="https://img.shields.io/badge/LinkedIn-1E293B?style=for-the-badge&logo=linkedin&logoColor=60A5FA" alt="LinkedIn" />
  </a>
  <a href="mailto:kasakk2006@gmail.com">
    <img src="https://img.shields.io/badge/Email-1E293B?style=for-the-badge&logo=gmail&logoColor=EA4335" alt="Email" />
  </a>
  <a href="https://kasakranthikiran.vercel.app">
    <img src="https://img.shields.io/badge/Portfolio-1E293B?style=for-the-badge&logo=globe&logoColor=60A5FA" alt="Portfolio" />
  </a>
</div>

<br/>

<div align="center">
  <picture>
    <img src="assets/footer-wave.svg" width="100%" alt="Footer" />
  </picture>
</div>
