# 📝 Guia Rápido de Git

---

## 📌 Configuração inicial (primeira vez no PC)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

---

## 🚀 Fluxo básico de uso

### 1. Clonar um repositório existente

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

### 2. Verificar status do repositório

```bash
git status
```

### 3. Adicionar arquivos para commit

✅ Adicionar arquivos específicos:

```bash
git add arquivo1.ext arquivo2.ext
```

✅ Adicionar tudo que foi alterado:

```bash
git add .
```

### 4. Fazer commit com mensagem

```bash
git commit -m "feat: mensagem clara sobre o que foi feito"
```

🔹 **Prefixos comuns:**
- `feat`: nova feature
- `fix`: correção de bug
- `docs`: documentação
- `style`: formatação/indentação
- `refactor`: refatoração sem mudar comportamento
- `chore`: tarefas gerais

### 5. Enviar alterações para o GitHub

```bash
git push
```

🔔 Se for o primeiro push:

```bash
git branch -M main
git push -u origin main
```

### 6. Puxar alterações do GitHub (antes de começar a trabalhar)

```bash
git pull
```

---

## 🔀 Comandos úteis

✅ Ver branches

```bash
git branch
```

✅ Criar nova branch

```bash
git checkout -b nome-da-branch
```

✅ Mudar para branch existente

```bash
git checkout nome-da-branch
```

✅ Mesclar branch atual com outra

```bash
git merge nome-da-branch
```

✅ Deletar branch local

```bash
git branch -d nome-da-branch
```

---

## 🔧 Configuração de remoto

✅ Adicionar remoto

```bash
git remote add origin https://github.com/seu-usuario/repositorio.git
```

✅ Alterar URL do remoto

```bash
git remote set-url origin https://github.com/seu-usuario/repositorio.git
```

✅ Ver remotos configurados

```bash
git remote -v
```

---

## 🚨 Desfazendo erros rapidamente

✅ Desfazer alterações não commitadas em um arquivo

```bash
git checkout -- arquivo.ext
```

✅ Resetar staging area (antes do commit)

```bash
git reset
```

✅ Voltar commit local (mantendo alterações)

```bash
git reset --soft HEAD~1
```

✅ Voltar commit local (perdendo alterações)

```bash
git reset --hard HEAD~1
```

---

## ✨ Dica visionária

Commita sempre com mensagens claras e contexto, mesmo que o projeto não esteja pronto.  
Isso documenta sua evolução, facilita rollback e te deixa mais profissional.

---

## 🤝 Autor

**Lucas Amorim**  
[Seu LinkedIn aqui]
