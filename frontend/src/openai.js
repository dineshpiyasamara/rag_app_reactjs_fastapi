export async function sendMsgToOpenAI(message) {
  const data = { question: message };
  console.log("=================");
  console.log(JSON.stringify(data));
  fetch("http://127.0.0.1:8000/api/ask_llm", {
    mode: "no-cors",
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ question: "message" }),
  })
    .then((res) => res.json())
    .then((res) => console.log(res));
}

// function fetchAPI() {
//   axios.get('http://localhost:5000/hello')
//     .then(response => console.log(response.data))
// }
