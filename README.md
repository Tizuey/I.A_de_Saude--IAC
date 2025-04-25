# Extração de Informação de Imagens com Texto em Letras Cursivas
#### 🔄 **ETAPA 0: PREPARAÇÃO DO AMBIENTE**

- [ ] Coletar 50+ amostras reais do que será usado

---

### 🖼️ **ETAPA 1: PRÉ-PROCESSAMENTO PARA CURSIVO**
#### 1. Normalização de Iluminação
**Objetivo:** Corrigir variações de brilho sem perder traços finos  
**Métodos Recomendados:**
- **CLAHE**: Equaliza o contraste localmente, ideal para papéis texturizados  
- **Filtro Bilateral**: Remove ruído enquanto preserva bordas de letras  
**Por quê?** A escrita cursiva tem traços delicados que desaparecem com iluminação irregular  

#### 2. **Binarização Avançada**
**Técnicas Comparativas:**

| Método       | Melhor Para            | Vantagens                  | Cuidados                 |
|--------------|------------------------|----------------------------|--------------------------|
| Sauvola      | Documentos antigos     | Adapta-se a manchas        | Pode suavizar demais     |
| Niblack      | Tintas escuras         | Preserva traços finos      | Amplifica ruídos         |
| Wolf-Jolion  | Iluminação irregular   | Normaliza fundos           | Lento em imagens grandes |

**Validação:** Verificar se mantém conectadas letras como "m" e "n"

#### 3. **Processamento Morfológico**
**Estratégias para Cursiva:**
- **Fechamento Vertical (3x1)**: Liga traços de letras como "p" e "q"  
- **Abertura Horizontal (1x5)**: Remove riscos sem quebrar palavras  
**Atenção:**  
- Evitar kernels maiores que 5px para não distorcer a escrita  
- Testar com letras problemáticas ("e", "a", "t")  

#### 4. **Correção de Inclinação**
**Abordagem em Duas Etapas:**
1. **Detecção Inicial:** Usar transformada de Hough para linhas dominantes  
2. **Ajuste Fino:** Calcular ângulo pelo retângulo envolvente mínimo  
**Tolerância:** Aceitar até 2° de variação para não distorcer o texto  

#### 5. **Validação de Resultados**
**Métricas Importantes:**
1. **Taxa de Conectividade:**  
   - Comparar componentes conectados antes/depois  
   - Meta: Manter 90% das ligações entre letras  

2. **Checklist Visual:**
   - [ ] Acentos visíveis (ã, ç, ê)  
   - [ ] Letras com laços intactas ("b", "d", "g")  
   - [ ] Espaçamento consistente entre palavras  

#### 6. **Casos Especiais**
**Problemas Comuns e Soluções:**
- **Letras "ç"**: Analisar contornos específicos  
- **Pontos flutuantes**: Filtrar por tamanho de componentes  
- **Vazamentos de tinta**: Ajustar dilatação conforme espessura  

#### 📅 **Plano de Implementação**

**Fase 1 (Básica):**
1. Normalizar iluminação com CLAHE  
2. Binarizar com Sauvola (31x31)  
3. Aplicar operações morfológicas direcionais  

**Fase 2 (Otimização):**
1. Implementar correção angular automática  
2. Testar diferentes combinações de kernels  
3. Criar regras para caracteres especiais  

**Fase 3 (Validação):**
1. Montar conjunto de testes com:  
   - 20 amostras perfeitas  
   - 30 amostras desafiadoras (papel rugoso, tinta fraca)  
   - 10 amostras degradadas  

**Dicas Práticas:**
- Sempre comparar resultados lado a lado com o original  
- Documentar quais técnicas funcionam melhor para cada tipo de letra  
- Começar com imagens de boa qualidade antes de avançar para casos difíceis  

Precisa de detalhes adicionais sobre algum desses tópicos ou ajustes na abordagem?

---

### ✂️ **ETAPA 2: SEGMENTAÇÃO DE TEXTO**
**Objetivo:** Dividir o documento em linhas → palavras → caracteres

#### ✔️ Tarefas Críticas:
1. **Detecção de Linhas**
   - [ ] Implementar:
     - Projeção horizontal de pixels
     - Agrupamento por componentes conectados
   - *Validação:* Margem de erro de 1 linha a cada 10

2. **Separação de Palavras**
   - [ ] Calcular:
     - Espaçamento médio entre caracteres
     - Distância Euclidiana entre contornos
   - *Critério:* 90% de acerto em palavras com 4+ letras

3. **Segmentação de Caracteres**
   - [ ] Testar:
     - Watershed com marcadores
     - Decomposição por concavidades
   - *Desafio:* Lidar com letras ligadas ("ri", "ni")

---

### 🔍 **ETAPA 3: RECONHECIMENTO**
**Objetivo:** Converter imagens → texto legível

#### ✔️ Tarefas Críticas:
1. **Seleção de Modelo**
   - [ ] Avaliar:
     - EasyOCR (pré-treinado em português)
     - TrOCR (Transformer-based)
     - Custom CRNN
   - *Métrica:* CER < 15% em teste inicial

2. **Pré-processamento Específico**
   - [ ] Padronizar:
     - Altura de 32 pixels
     - Normalização de intensidade
   - *OBS:* Manear bordas de 5px para letras cortadas

3. **Pós-processamento**
   - [ ] Implementar:
     - Corretor ortográfico (pyspellchecker)
     - Regras contextuais (ex.: "qüe" → "que")

---

### 🎯 **ETAPA 4: OTIMIZAÇÃO PARA PORTUGUÊS**
**Objetivo:** Reduzir erros em caracteres específicos

#### ✔️ Tarefas Críticas:
1. **Tratamento de Diacríticos**
   - [ ] Criar regras para:
     - "~" → transformar "a" em "ã"
     - "^" → diferenciar "e" de "ê"

2. **Dataset de Treino**
   - [ ] Coletar:
     - 500+ exemplos de "ç"
     - 300+ exemplos de acentos agudos

3. **Modelo de Linguagem**
   - [ ] Incorporar:
     - Frequência de bigramas PT-BR
     - Lista de verbos conjugados

---

### 📊 **ETAPA 5: AVALIAÇÃO**
**Objetivo:** Medir performance real

#### ✔️ Tarefas Críticas:
1. **Métricas Quantitativas**
   - [ ] Calcular:
     - CER por faixa de inclinação
     - WER por tipo de documento

2. **Análise Qualitativa**
   - [ ] Identificar:
     - 5 erros mais frequentes
     - Padrões de falha recorrentes

3. **Relatório Final**
   - [ ] Documentar:
     - Taxa de sucesso por etapa
     - Limitações identificadas

---

### 📅 **CRONOGRAMA DETALHADO**

| Semana | Etapa                | Entregáveis Esperados                     |
|--------|----------------------|------------------------------------------|
| 1-2    | Pré-processamento    | Relatório comparativo de 5 técnicas      |
| 3-4    | Segmentação          | Dataset com 50 imagens anotadas manualmente |
| 5-6    | Reconhecimento       | Modelo com CER < 25%                     |
| 7-8    | Otimização           | Sistema integrado com correção contextual |
| 9      | Validação            | Relatório de performance com matriz de confusão |

---

### 🔧 **KIT DE FERRAMENTAS RECOMENDADO**
1. **Anotação Manual**
   - LabelImg (para marcar regiões de texto)
2. **Visualização**
   - Plotly (para gráficos interativos)
3. **Versionamento**
   - DVC (Data Version Control)

---

### ❓ **PONTOS DE VALIDAÇÃO CRÍTICOS**
1. **Pré-processamento**
   - "A letra 'f' cursiva mantém seu laço inferior?"
2. **Segmentação**
   - "Palavras com 'tt' ou 'rr' são divididas corretamente?"
3. **Reconhecimento**
   - "O modelo distingue 'n' de 'u' em contexto?"
