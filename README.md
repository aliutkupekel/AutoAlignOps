# AutoAlignOps_Mark_2
A Formally Constrained Multi-Agent Framework for Semantics-Preserving Prompt Optimization

Our File pipeline is like this: 

AutoAlignOps/
│
├── .gitignore                 # Git'e eklenmeyecek dosyalar (venv, __pycache__, .env vb.)
├── README.md                  # Proje dokümantasyonu (Proposal'ı buraya ekleyebiliriz)
├── requirements.txt           # Python kütüphaneleri (crewai, langchain, pydantic vb.)
├── .env.example               # API key'ler için güvenli şablon
│
├── data/                      # Veri ve Prompt Registry
│   ├── registry/              # Orijinal ve versiyonlanmış promptlar (JSON/YAML)
│   └── benchmarks/            # Sentetik davranışsal testler ve proplar
│
├── configs/                   # Statik Konfigürasyonlar
│   ├── agents_config.yaml     # Ajanların prompt, rol ve hedef (goal) tanımları
│   └── mcp_config.yaml        # MCP yetki ve sınır konfigürasyonları (Read/Write izinleri)
│
├── src/                       # Ana Kaynak Kodları (Uygulamanın Kalbi)
│   ├── __init__.py
│   ├── main.py                # Pipeline'ı (CrewAI/AutoGen) başlatan ana orkestratör
│   │
│   ├── agents/                # Ajan Sınıfları (Proposal'daki 4 ajan)
│   │   ├── __init__.py
│   │   ├── discovery.py       # Prompt Discovery Agent
│   │   ├── optimizer.py       # Prompt Optimization Agent
│   │   ├── validator.py       # Adversarial Alignment Validator Agent
│   │   └── deployer.py        # Rollback/Deploy Agent
│   │
│   ├── mcp/                   # Model Context Protocol & Araçlar (Tools)
│   │   ├── __init__.py
│   │   ├── schemas.py         # Pydantic ile Input/Output doğrulama (Typed input schemas)
│   │   ├── registry_tools.py  # Prompt okuma, versiyonlama ve snapshot araçları
│   │   └── probe_tools.py     # Sandboxed endpoint'te test çalıştıran araçlar
│   │
│   ├── core/                  # Çekirdek Mantık
│   │   ├── __init__.py
│   │   ├── embeddings.py      # Cosine similarity (ADR hesabı için)
│   │   └── math_models.py     # P(A) (Risk Modeli) ve Token Efficiency formülleri
│   │
│   └── evaluation/            # Metrik ve Değerlendirme Motoru
│       ├── __init__.py
│       └── metrics.py         # BRR, ADR ve AOR metrik hesaplamaları
│
└── tests/                     # Birim Testleri (Unit Tests)
    ├── test_mcp.py            # MCP kısıtlamalarının testleri
    └── test_metrics.py        # Metriklerin doğru hesaplandığının testleri