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


/**LISTAR SENSORES */
async function listarSensores() {
  try {
    const resposta = await fetch(SENSOR_LIST);
    const sensores = await resposta.json();

    const container = document.getElementById("listaSensores");
    if (!container) return;

    container.innerHTML = "";

    if (sensores.length === 0) {
      container.innerHTML = "<p>Nenhum sensor encontrado.</p>";
      return;
    }

    sensores.forEach(sensor => {
      const item = document.createElement("p");
      item.textContent = `${sensor.sensor_name} | ${sensor.type_connection} | ${sensor.status} | ${sensor.id}`;
      container.appendChild(item);
    });

  } catch (erro) {
    console.error("Erro ao buscar sensores:", erro);
    document.getElementById("listaSensores").innerHTML = "<p>Nenhum sensor encontrado.</p>";
  }
}
listarSensores();


/*OBTER VALOR DO SENSOR MQ2 */
async function obterMq2() {
  try {
    let url = await fetch(SENSOR_LIST);
    if (!url.ok) {
      throw new Error(`Estado api ${url.status}`);
    }
    let dadosApi = await url.json();
    console.log(dadosApi[0].status);
    document.getElementById("fuga").innerHTML = dadosApi[0].status;
    document.getElementById("sensor1").innerHTML = dadosApi[0].sensor_name;
  } catch (error) {
    console.log("ERRO NA REQUISIÇÃO DA API");
  }
}
obterMq2();


/*OBTER VALOR DO SENSOR PESO */
async function obterPeso() {
  try {
    let url = await fetch(SENSOR_LIST);
    if (!url.ok) {
      throw new Error(`Estado api ${url.status}`);
    }
    let dadosApi = await url.json();
    document.getElementById("gasRestante").innerHTML = dadosApi[1].status;
    document.getElementById("sensor2").innerHTML = dadosApi[1].sensor_name;
  } catch (error) {
    console.log("ERRO NA REQUISIÇÃO DA API");
  }
}

obterPeso();

/**ENVIAR ALERTA DE FOGO */
async function enviarAlerta() {
  const alerta = {
    user_id: 1,
    message: "Fogo detetado!!!",
    type: "fogo"
  };

  try {
    const resposta = await fetch(ALERT_POST, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(alerta)
    });

    const dados = await resposta.json();

    if (resposta.ok) {
      console.log("Alerta enviado:", dados);
      alert("Alerta enviado com sucesso!");
    } else {
      console.error("Erro no envio:", dados.message || dados);
      alert("Erro ao enviar alerta.");
    }

  } catch (erro) {
    console.error("Erro na conexão:", erro);
    alert("Erro de conexão com a API.");
  }
}


/**FUNÇÃO DE TROCA DO ESTADO (botão) */
let contador = 0;
function troca() {
  const img = document.getElementById("icon");

  const imagens = [
    '/static/off-button.png',
    '/static/on-button.png'
  ];

  contador = (contador + 1) % imagens.length;
  img.src = imagens[contador];

  const mensagem = (contador === 1) ? "ligar" : "desligar";

  const dadosControle = {
    user_id: 1,
    message: mensagem
  };

  fetch(CONTROL_SIGNAL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(dadosControle)
  })
    .then(res => res.json())
    .then(data => {
      console.log(`✅ Comando '${mensagem}' enviado com sucesso`, data);
    })
    .catch(error => {
      console.error("❌ Erro ao enviar sinal de controle:", error);
    });
}

hist.addEventListener("click", function () {
  alert("Aguarde os 100%")
})

async function deletarUsuario() {
  const userId = localStorage.getItem("usuarioId");
  if (!userId) {
    alert("Usuário não encontrado no localStorage!");
    return;
  }

  const url = `https://safegas-angola.onrender.com/auth/delete/${userId}`;

  try {
    const resposta = await fetch(url, {
      method: "DELETE"
    });

    const dados = await resposta.json();

    if (resposta.ok) {
      alert("Conta apagada com sucesso.");
      localStorage.clear(); // limpa tudo
      window.location.href = "/views/registro.html"; // ou onde preferir
    } else {
      alert(" Erro ao deletar: " + (dados.message || "Falha desconhecida"));
    }
  } catch (erro) {
    console.error(erro);
    alert("Erro de conexão ao tentar excluir usuário.");
  }
}
