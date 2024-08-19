import axios from "axios";

export async function sendMsgToOpenAI(message) {
  const data = { question: message };
  // console.log("=================");
  // console.log(JSON.stringify(data));
  // fetch("http://localhost:8000/api/ask_llm", {
  //   mode: "no-cors",
  //   method: "POST",
  //   headers: {
  //     "Content-type": "application/json",
  //   },
  //   body: JSON.stringify(data),
  // });
  // // .then((res) => res.json())
  // // .then((res) => console.log(res));

  // const newTodo = {
  //   id: crypto.randomUUID(), // Generate a UUID for the new todo item
  //   title,
  //   completed: false,
  // };

  // setTodos((currentTodos) => [...currentTodos, newTodo]);

  axios
    .post("http://localhost:8000/api/ask_llm", data)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      console.log(response.json());
      return response.json(); // Parses the JSON response into a JavaScript object
    })
    .catch((error) => {
      console.log("There was an error retrieving the todo list: ", error);
    });
}
