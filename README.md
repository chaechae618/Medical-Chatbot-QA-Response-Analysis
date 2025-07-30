## 🏥 Medical Chatbot QA Response Analysis & Accuracy Quantification  
📅 Mar. 2024 – Jun. 2024  
🎯 *Evaluating and improving LLM-based chatbot performance for healthcare-specific queries*

---

### 🧩 Overview  
- 약 4,000건의 **LLM 기반 의료 QA 기록**을 분석하여 챗봇 응답 품질 향상 방향 제시  
- **사용자군별 적합성 분석**, **질문 유형별 오류 패턴 파악**, **모델별 응답 구조 비교**를 통해 실무 인사이트 도출  
- ChatGPT, Claude, LLaMA2, Clova 등의 **LLM 모델 성능을 정량적으로 비교**하고 개선 전략 제시  

---

### 📊 Data Summary

- **Data Type**:  
  - 실제 LLM 기반 의료 챗봇 응답 기록 (비정형 텍스트)  
  - 전문가 정답 레퍼런스 (정형 텍스트)  
- **Data Volume**:  
  - 약 4,000건  
- **Content**:  
  - 복용법, 상호작용, 효능효과 관련 사용자 질의  
  - 임산부, 어린이, 고령자 등 **특수 사용자군 질의**  
  - LLM(Claude, ChatGPT, LLaMA2 등)의 응답과 전문가 정답 비교

---

### 📌 Key Findings

- **❶ 질문 유형별 분석**  
  - 복용법 관련 질문이 가장 많아 **우선 개선 영역**으로 식별  
  - 핵심 정보: 복용법 > 상호작용 > 효능효과

- **❷ LLM 모델별 응답 구조 분석**  
  - LLaMA2: 높은 응답 완성도  
  - ChatGPT: 깊이·적정성에서 강점  
  - **결합 전략** 필요 (LLaMA2 + ChatGPT 스타일)

- **❸ 연령대별 적합성 분석**  
  - 고령자 질의: LLaMA2 33%  
  - 소아 질의: ChatGPT 33%  
  - 청소년: 모든 모델 적합도 0% → 개선 필요성 제기

---

### 🧠 Project Outcomes

- ✅ 4,000+건 QA 데이터 기반 정량 평가 체계 수립  
- ✅ 오류 발생 질문 유형 및 패턴 도출  
- ✅ 모델별 응답 품질 영향 요인 도출  
- ✅ 의료 특화 챗봇 개발을 위한 구조적 개선 방향 제시  
- ✅ 전체 파이프라인 경험 확보 (전처리 → 분석 → 시각화 → 개선 제안)

---

### ⚙️ Tech Stack

- **Data Handling**: `Python`, `Pandas`, `NumPy`, `Scikit-learn`  
- **AI & Evaluation**: `OpenAI API (GPT-4 Turbo)`, `Prompt Engineering`, `LLM Response Evaluation Metrics`  

---

### 🧪 System Workflow (Step-by-Step)

1. **데이터 전처리 및 기준 설계**  
   - 4,000건 의료 QA 데이터 로딩 및 전처리 (토큰화, 정규화 등)  
   - 응답 품질 평가를 위한 정량적 기준 수립 (정확성, 완성도, 구조화 정도 등)

2. **LLM 응답 품질 수치화 분석**  
   - ChatGPT, Claude, LLaMA2 등 주요 LLM의 답변을 GPT-4 Turbo로 평가  
   - 다층 기준(완성도, 명확성, 깊이
