# OpenDataHub
Projet de TER de dernière année de Master SID
TER OPENDATAHUB !

# Architecture Globale du projet proposer 

"""
data_pipeline/
│
├── README.md                           # Documentation du projet
├── requirements.txt                    # Dépendances Python
├── .env                               # Variables d'environnement (DB credentials)
├── .gitignore                         # Fichiers à ignorer
│
├── main.py                            # Point d'entrée principal
├── pipeline.py                        # Orchestrateur du pipeline ETL
│
├── config/                            # CONFIGURATION
│   ├── __init__.py
│   ├── settings.py                    # Configuration globale
│   ├── schemas.py                     # Définition des schémas de données
│   └── database.py                    # Configuration des connexions DB
│
├── extractors/                        # EXTRACTION (Extract)
│   ├── __init__.py
│   ├── base_extractor.py             # Classe abstraite de base
│   ├── csv_extractor.py              # Extracteur CSV
│   ├── json_extractor.py             # Extracteur JSON
│   ├── excel_extractor.py            # Extracteur Excel (XLSX, XLS)
│   ├── xml_extractor.py              # Extracteur XML
│   └── api_extractor.py              # Extracteur API REST (bonus)
│
├── transformers/                      # TRANSFORMATION (Transform)
│   ├── __init__.py
│   ├── base_transformer.py           # Classe de transformation de base
│   ├── cleaner.py                    # Nettoyage des données
│   ├── validator.py                  # Validation des données
│   ├── normalizer.py                 # Normalisation et standardisation
│   ├── enricher.py                   # Enrichissement (calculs, ajouts)
│   └── type_converter.py             # Conversion de types
│
├── loaders/                          # CHARGEMENT (Load)
│   ├── __init__.py
│   ├── base_loader.py                # Classe abstraite de base
│   ├── database_loader.py            # Chargement vers base de données
│   ├── multi_table_loader.py         # Chargement multi-tables
│   ├── s3_loader.py                    # donner brute dans le service
│   ├── 
│   └── 
│
├── utils/                            # UTILITAIRES
│   ├── __init__.py
│   ├── logger.py                     # Configuration des logs
│   ├── file_detector.py              # Détection de format et encodage
│   ├── helpers.py                    # Fonctions utilitaires
│   ├── validators.py                 # Validateurs réutilisables
│   └── exceptions.py                 # Exceptions personnalisées
│
│   
│   
│
├── data/                             # DONNÉES
│   ├── input/                        # Fichiers sources
│   │   ├── csv/
│   │   ├── json/
│   │   ├── excel/
│   │   └── xml/
│   ├── output/                       # Fichiers transformés
│   │   ├── csv/
│   │   ├── json/
│   │   └── excel/
│   ├── processed/                    # Fichiers déjà traités (archive)
│   └── errors/                       # Fichiers en erreur
│
├── logs/                             # LOGS SUIVI DE CHAQUE ETAPE EXECUTER 
│   ├── etl_YYYYMMDD_HHMMSS.log      # Logs par exécution
│   └── error.log                     # Logs d'erreurs uniquement ERREUR DEECTER 
│
├── tests/                            # TESTS UNITAIRES
│   ├── __init__.py
│   ├── test_extractors.py
│   ├── test_transformers.py
│   ├── test_loaders.py
│   ├── test_pipeline.py
│   └── fixtures/                     # Données de test
│       ├── sample.csv
│       ├── sample.json
│       └── sample.xlsx
│
├── scripts/                          # SCRIPTS UTILITAIRES
│   ├── setup_database.py            # Initialisation de la BD
│   ├── migrate_data.py              # Migration de données
│   └── generate_report.py           # Génération de rapports
│
└── docs/                            # DOCUMENTATION
    ├── architecture.md              # Documentation architecture
    ├── user_guide.md               # Guide utilisateur
    └── apobale du projet pr
"""


 
