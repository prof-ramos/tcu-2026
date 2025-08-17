# 🤝 Guia de Contribuição

Obrigado por querer contribuir com o projeto **TCU 2026 - Banco de Dados de Questões**! 

## 🚀 Como Contribuir

### 1. **Preparação**
```bash
# Fork o repositório no GitHub
# Clone seu fork
git clone https://github.com/SEU_USUARIO/tcu-2026.git
cd tcu-2026

# Configure o upstream
git remote add upstream https://github.com/USUARIO_ORIGINAL/tcu-2026.git

# Configure seu ambiente
python3 -m venv venv
source venv/bin/activate
pip install -r scripts/requirements.txt
```

### 2. **Desenvolvimento**
```bash
# Crie uma branch para sua feature
git checkout -b feature/minha-feature

# Faça suas modificações
# ...

# Teste suas alterações
python scripts/clean_data.py  # Se modificou scripts
```

### 3. **Commit e Push**
```bash
# Commit com mensagem descritiva
git add .
git commit -m "feat: adiciona nova funcionalidade X"

# Push para seu fork
git push origin feature/minha-feature
```

### 4. **Pull Request**
- Abra um Pull Request no GitHub
- Descreva claramente as mudanças
- Referencie issues relacionadas

## 📝 Padrões de Commit

Use o padrão **Conventional Commits**:

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `style:` - Formatação, espaços, etc.
- `refactor:` - Refatoração de código
- `test:` - Adição ou correção de testes
- `chore:` - Manutenção, dependências, etc.

## 🎯 Tipos de Contribuição

### 📊 **Melhorias nos Dados**
- Correção de inconsistências
- Adição de novos datasets
- Melhoria na estrutura hierárquica

### 🧹 **Scripts de Processamento**
- Otimização dos scripts existentes
- Novos scripts de análise
- Melhoria na documentação do código

### 📚 **Documentação**
- Correção de erros na documentação
- Adição de exemplos
- Melhoria na clareza das instruções

### 🔧 **Funcionalidades**
- APIs para acesso aos dados
- Ferramentas de visualização
- Scripts de automação

## 🐛 Reportando Bugs

1. **Verifique** se o bug já foi reportado nas Issues
2. **Crie** uma nova Issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Informações do ambiente (OS, Python, etc.)

## 💡 Sugerindo Melhorias

1. **Abra** uma Issue com label "enhancement"
2. **Descreva** claramente a melhoria sugerida
3. **Explique** o valor/benefício da melhoria
4. **Proponha** uma implementação (se possível)

## 📋 Checklist antes do Pull Request

- [ ] Código testado e funcionando
- [ ] Documentação atualizada (se necessário)
- [ ] Mensagens de commit seguem o padrão
- [ ] Código segue as convenções do projeto
- [ ] Sem dados sensíveis ou pessoais no commit

## 🚫 O que NÃO fazer

- ❌ Fazer commits direto na branch main
- ❌ Incluir dados pessoais ou sensíveis
- ❌ Modificar dados originais na pasta `data/raw/`
- ❌ Fazer PRs muito grandes (prefira PRs menores e focados)
- ❌ Ignorar os padrões de código estabelecidos

## 🔄 Processo de Review

1. **Revisão automática** - Verificações básicas
2. **Revisão manual** - Análise do código e impacto
3. **Testes** - Validação em diferentes ambientes
4. **Merge** - Integração na branch principal

## 🎓 Dicas para Iniciantes

### Python
- Use **type hints** quando possível
- Documente funções complexas
- Siga o **PEP 8** para estilo de código

### Pandas/Data Science
- Valide dados antes e depois do processamento
- Use nomes descritivos para variáveis
- Comente lógicas de negócio complexas

### Git
- Commits pequenos e focados
- Mensagens descritivas
- Sincronize frequentemente com upstream

## 📞 Contato

- 🐛 **Issues**: Para bugs e sugestões
- 📧 **Discussões**: Para dúvidas gerais
- 💬 **Pull Requests**: Para propostas específicas

---

**Obrigado por contribuir! 🙏 Sua ajuda faz a diferença para a comunidade de estudantes do TCU.**