# 🔥 SafeGas Angola

### Sistema Inteligente de Monitoramento e Controle de Gás em Angola

**Autor:** KAAS  
**Versão:** 2.0 – Projeto com Módulos Expansíveis  
**Data:** 09-06-2025  

---

## 🛑 Problema

Em Angola, o gás de cozinha (GLP) é amplamente utilizado, mas o uso de botijas apresenta riscos como:

- Vazamentos de gás por má vedação ou desgaste.
- Explosões/incêndios por ausência de detecção precoce.
- Falta de controle no consumo, descobrindo o fim do gás apenas no momento de uso.
- Insegurança por falta de desligamento automático.

Além disso, a maioria das residências não possui meios digitais de monitoramento, tornando o uso de gás especialmente perigoso para famílias com crianças, idosos ou em cozinhas improvisadas.

---

## 🎯 Objetivo

Desenvolver um **sistema inteligente, acessível e modular** que permita:

- Monitorar o **nível de gás** da botija.
- Detectar **vazamentos** em tempo real.
- **Ligar/desligar** o fornecimento de gás remotamente.
- Funcionar **mesmo sem internet** (via SMS ou USSD).
- Operar com **energia solar** em zonas sem eletricidade.
- Enviar **alertas e dicas educativas** sobre segurança.

---

## 🧱 Estrutura do Sistema

### 🔹 Módulo Base

| Componente                | Função                                              |
|--------------------------|-----------------------------------------------------|
| ESP32                    | Microcontrolador com Wi-Fi e Bluetooth              |
| Sensor de Gás MQ-2       | Detecção de vazamentos de gás GLP                   |
| Célula de carga + HX711  | Medição do peso da botija                          |
| Módulo Relé + Válvula NC | Controle eletrônico do fluxo de gás                 |
| App/Web Dashboard        | Interface para monitoramento e controle remotos     |

### 🔹 Módulos Expansíveis

| Módulo                   | Função / Benefício                                  |
|--------------------------|-----------------------------------------------------|
| 🔋 Energia Solar         | Funcionamento off-grid                              |
| 📱 GSM (SIM800L)         | Alertas por SMS                                     |
| 🧯 Sensor de chama       | Detecção de incêndios                               |
| 🧒 Proteção Infantil     | Bloqueio do gás por segurança                       |
| 📊 Previsão de Consumo   | Estimativa de dias restantes com base no histórico  |
| 🧾 Notificação ao Revendedor | Solicitação automática de nova botija         |
| 📚 Modo Educativo        | Dicas de segurança via app ou SMS                   |
| 📡 Interface USSD        | Acesso via telemóveis simples                       |
| 🆘 Botão SOS             | Alerta e desligamento imediato em emergências       |

---

## 🔧 Como Funciona

1. **Peso** da botija é medido pela célula de carga e enviado ao ESP32.
2. **Vazamentos** são detectados via sensor MQ-2.
3. Em caso de emergência:
   - A válvula fecha automaticamente.
   - Um alerta é enviado (app, som, SMS).
4. O utilizador pode:
   - Ver nível de gás.
   - Ligar/desligar o fornecimento.
   - Receber alertas, previsões e dicas úteis.
   - Controlar via app, SMS ou USSD.

---

## 🌍 Impacto Social em Angola

✅ Redução de acidentes com gás  
✅ Autonomia em zonas sem luz  
✅ Acesso universal via USSD/SMS  
✅ Educação sobre segurança doméstica  
✅ Apoio a revendedores locais  
✅ Inclusão digital e energética

---

## 🧪 Fases do Projeto

| Fase          | Descrição                                                                 |
|---------------|---------------------------------------------------------------------------|
| **Protótipo** | Testes iniciais com sensores e válvula controlada pelo ESP32              |
| **App/Web**   | Desenvolvimento de dashboard para controlo remoto                         |
| **GSM**       | Envio de SMS para utilizadores sem Wi-Fi                                  |
| **Solar**     | Adição de painel solar para autonomia energética                          |
| **Expansão**  | Módulos: USSD, botão SOS, proteção infantil, previsão e integração revenda|

---

## 📈 Futuras Expansões

- Integração com **bombeiros e emergências locais**.
- App multilíngue: **Português, Kimbundu, Umbundu**.
- Banco de dados comunitário para **análise do consumo energético nacional**.

---

## 🛠️ Tecnologias Utilizadas

- ESP32  
- Sensor MQ-2  
- Célula de carga + HX711  
- Módulo Relé + Válvula Solenóide  
- Módulo GSM (SIM800L)  
- Painel Solar  
- App mobile / Web Dashboard / Blynk  
- Plataforma de USSD (em desenvolvimento)  

---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Quer melhorar o projeto, sugerir um módulo ou colaborar com código, documentação ou testes? Basta fazer um fork ou abrir uma issue.

---

## 📬 Contato

**Autor:** KAAS  
**Email:** kaas.tech@protonmail.com *(exemplo)*  
**LinkedIn:** [linkedin.com/in/kaas-tech](#) *(coloque o link real)*  

---

> “SafeGas Angola: onde a segurança encontra a inovação.”
