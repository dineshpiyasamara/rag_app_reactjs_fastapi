import axios from "axios";

export async function sendMsgToOpenAI(message) {
  const data = { question: message };
  axios
    .post("http://localhost:8000/api/ask_llm", data)
    .then((response) => {
      if (response.status !== 200) {
        throw new Error("Network response was not ok");
      }
      console.log(response.data.response);
      return response;
    })
    .catch((error) => {
      console.log("There was an error retrieving data: ", error);
    });
}
