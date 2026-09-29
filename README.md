# Extração de Texto com Amazon Textract

Para explorar o funcionamento do serviço de forma objetiva e sem dependência de execução na nuvem AWS, o projeto foi estruturado com base na criação de uma imagem de teste personalizada, elaboração de script de integração em Python e documentação visual do fluxo de processamento no console.

## Tecnologias e Ferramentas

- **Amazon Textract**: Serviço de IA/ML para extração de texto em documentos.
- **Python & Boto3**: Script de chamada elaborado para integração com a API da AWS.
- **Paint**: Criação da imagem de entrada (lista de material escolar).

## Escopo e Etapas do Desafio

- Foi realizado o teste do Amazon Textract utilizando um documento contendo uma lista de material escolar.
- Foram exploradas as opções de análise documental e reconhecimento óptico de caracteres (OCR), observando o fluxo de processamento de documentos no serviço.

1. **Elaboração do Dataset**: Criação manual de uma imagem em formato `.png` contendo uma lista de material escolar para teste de OCR.
2. **Desenvolvimento do Script**: Elaboração de código Python utilizando a biblioteca `boto3` para realizar a chamada do serviço `detect_document_text`.
3. **Simulação e Validação no Console**:
   - Acesso ao Amazon Textract.
   - Upload da imagem `.png` gerada.
   - Execução do fluxo de extração de texto e análise dos resultados obtidos.

## Estrutura do Repositório

- `inputs/`: Imagem criada para o teste.
- `src/`: Script Python (`main.py`) com a estrutura de chamada via Boto3.
- `screenshots/`: Evidências do acesso ao console, upload e extração no Amazon Textract.

## Aprendizados

- Conceitos fundamentais do serviço **Amazon Textract**.
- Estruturação de chamadas via SDK oficial (`boto3`) em Python.
- Fluxo de processamento de documentos e extração de texto por OCR.
