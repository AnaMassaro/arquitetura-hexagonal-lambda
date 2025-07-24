```plaintext
📦 lambda_function.py        ← ponto de entrada da Lambda

📁 application/              ← lógica de negócio (casos de uso)
│   └── validate_lambda_config.py  ← orquestra as validações

📁 domain/                   ← contratos (ports)
│   └── ports/
│       └── input_event_port.py   ← interface para entrada dos dados
│       └── lambda_data_port.py   ← interface para busca de dados da Lambda

📁 adapters/
│   ├── inbound/             ← adapters de entrada (formato do evento)
│   │   ├── sqs_event_parser.py
│   │   └── api_event_parser.py
│   └── outbound/            ← adapters de saída (serviços externos)
│       ├── boto3_lambda_fetcher.py
│       └── config_lambda_fetcher.py
```
