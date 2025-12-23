/***************************API****************************/
const API_BASE = "https://safegas-angola.onrender.com";

//  Autenticação
const AUTH_TEST = `${API_BASE}/auth/`;
const AUTH_LIST = `${API_BASE}/auth/list/`;
const AUTH_POST = `${API_BASE}/auth/post/`;
const AUTH_LOGIN = `${API_BASE}/auth/login/`;
const AUTH_DELETE = (id) => `${API_BASE}/auth/delete/${id}`;

// Leitura de Sensores
const READING_TEST = `${API_BASE}/reading/`;
const READING_POST = `${API_BASE}/reading/post/`;
const READING_LIST = `${API_BASE}/reading/list/`;
const READING_BY_ID = (id) => `${API_BASE}/reading/${id}`;
const READING_BY_USER = (userId) => `${API_BASE}/reading/user/${userId}`;
const READING_DELETE = (id) => `${API_BASE}/reading/delete/${id}`;

//  Alertas
const ALERT_TEST = `${API_BASE}/alert/`;
const ALERT_LIST = `${API_BASE}/alert/list/`;
const ALERT_POST = `${API_BASE}/alert/post/`;
const ALERT_DELETE = (id) => `${API_BASE}/alert/delete/${id}`;

//  Controle de Atuação
const CONTROL_TEST = `${API_BASE}/control/`;
const CONTROL_SIGNAL = `${API_BASE}/control/signal/`;
const CONTROL_LIST = `${API_BASE}/control/list/`;

//  Sensores
const SENSOR_TEST = `${API_BASE}/sensor/`;
const SENSOR_REGISTER = `${API_BASE}/sensor/register/`;
const SENSOR_LIST = `${API_BASE}/sensor/list/`;
const SENSOR_FIND = (sensorName) => `${API_BASE}/sensor/find/${sensorName}`;
const SENSOR_DELETE = (id) => `${API_BASE}/sensor/delete/${id}`;



async function getApi(){
    try {
        let url = await fetch(READING_LIST)
        if(!url.ok){
            throw new Error(`Estado api ${url.status}`)
        }
        let dadosApi = await url.json();
        console.log(dadosApi)
      } catch (error) {
        console.log("ERRO NA REQUISIÇÃO DA API")
    }
  }
  getApi();


// async function listarUsuarios() {
//   try {
//     const resposta = await fetch(AUTH_LIST);
//     const usuarios = await resposta.json();
//     console.log(usuarios)

//     //console.log("👥 Lista de usuários:");
//     //usuarios.forEach(usuario => {
//       console.log(`ID: ${usuario.id}, Nome: ${usuario.name}, Email: ${usuario.email}`);
//     //});

//   } catch (erro) {
//     console.error(" Erro ao buscar usuários:", erro);
//   }
// }
// listarUsuarios()



// async function pegarUltimaLeitura() {
//   try {
//     const resposta = await fetch(READING_LIST);
//     const leituras = await resposta.json();

//     if (Array.isArray(leituras) && leituras.length > 0) {
//       const ultimaLeitura = leituras[leituras.length - 1]; // pega o último item do array
//       console.log("📦 Última leitura:", ultimaLeitura);

//       // Exemplo: exibir em elementos HTML
//       document.getElementById("valorGas").textContent = ultimaLeitura.gas_level;
//       document.getElementById("valorTemp").textContent = ultimaLeitura.temperature;
//       document.getElementById("valorPeso").textContent = ultimaLeitura.weight;
//       document.getElementById("valorVazamento").textContent = ultimaLeitura.leak ? "Sim" : "Não";
//     } else {
//       console.log("⚠️ Nenhuma leitura encontrada.");
//     }
//   } catch (erro) {
//     console.error("❌ Erro ao buscar leituras:", erro);
//   }
// }
