# 🔍 Atividade Prática: The Human Linter

Este repositório foi criado para a atividade prática de **Revisão de Código (Code Review)**, simulando o papel de um "Linter Humano". O objetivo é praticar a identificação de erros de lógica e de estilo (PEP8) em Python através do fluxo de Pull Requests no GitHub.

## 👥 Dupla Responsável
* **Wellington Paiva** (Desenvolvedor/Autor)
* **Juliana Bertoldo** (Revisora/Linter)

---

## 🎯 Objetivo da Missão
Criar funções propositadamente erradas para que o parceiro de dupla identifique os problemas apenas através da revisão visual na interface do GitHub, sem a execução do código ou auxílio de ferramentas automatizadas.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Versionamento:** Git & GitHub
* **Padrão de Estilo:** PEP 8 (Python Enhancement Proposal)

---

## 📂 Estrutura do Projeto

* `calculo.py`: Contém uma função de cálculo de impostos com erros de nomenclatura (PascalCase em variáveis) e erro de lógica na soma da taxa.
* `verificacao.py`: Contém uma função de maioridade com erro de padrão de nome de função (PascalCase) e um erro de lógica clássico no operador de comparação (`>` em vez de `>=`).

---

## 🔄 Fluxo de Trabalho (Workflow)

1. **Preparação:** Criação do repositório e das branches de funcionalidade (`feature/missao-linter`).
2. **A Missão:** Escrita do código com 2 erros propositais (1 de lógica, 1 de estilo) por arquivo.
3. **Pull Request:** Abertura do PR da branch de feature para a `main`.
4. **Revisão Humana:** A revisora (Juliana) utiliza a aba *Files Changed* do GitHub para comentar os erros encontrados.
5. **Correção:** O autor (Wellington) aplica as correções sugeridas, realiza um novo commit e finaliza o PR (Merge).

---

## 📋 Problemas Documentados

| Arquivo | Tipo de Erro | Descrição Original | Correção Aplicada |
| :---  | :--- | :--- | :--- |
| `calculo.py` | Estilo | Variável `Imposto` (PascalCase) | Alterado para `imposto` (snake_case) |
| `calculo.py` | Lógica | Soma incorreta da taxa | Ajustada a fórmula matemática |
| `verificacao.py` | Estilo | Função `Verificar_Maioridade` | Alterado para `verificar_maioridade` |
| `verificacao.py` | Lógica | Erro no limite de 18 anos | Alterado de `>` para `>=` |

---

> **Desafio Mental:** Esta atividade foca na atenção aos detalhes. Revisar código "no olho" ajuda a desenvolver uma percepção crítica sobre a legibilidade e a correção lógica antes mesmo de rodar o primeiro teste.