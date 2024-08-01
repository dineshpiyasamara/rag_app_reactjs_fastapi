import "./App.css";
import gptLogo from "./assets/chatgpt.svg";
import addBtn from "./assets/add-30.png";
import msgIcon from "./assets/message.svg";
import home from "./assets/home.svg";
import saved from "./assets/bookmark.svg";
import rocket from "./assets/rocket.svg";
import sendBtn from "./assets/send.svg";
import userIcon from "./assets/user-icon.png";
import gptImgLogo from "./assets/chatgptLogo.svg";
import { sendMsgToOpenAI } from "./openai";
import { useEffect, useRef, useState } from "react";

function App() {
  const msgEnd = useRef(null);

  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    {
      text: "Hi. I am large language model based application",
      isBot: true,
    },
  ]);

  useEffect(() => {
    msgEnd.current.scrollIntoView();
  }, [messages]);

  const handleSend = async () => {
    const text = input;
    setInput("");
    setMessages([...messages, { text: text, isBot: false }]);
    const res = await sendMsgToOpenAI(text);
    setMessages([
      ...messages,
      { text: text, isBot: false },
      { text: res, isBot: true },
    ]);
  };

  const handleEnter = async (e) => {
    if (e.key === "Enter") await handleSend();
  };

  const handleQuery = async (e) => {
    const text = e.target.value;
    setMessages([...messages, { text: text, isBot: false }]);
    const res = await sendMsgToOpenAI(text);
    setMessages([
      ...messages,
      { text: text, isBot: false },
      { text: res, isBot: true },
    ]);
  };

  return (
    <div className="App">
      <div className="sideBar">
        <div className="upperSide">
          <div className="upperSideTop">
            <img src={gptLogo} alt="Logo" className="logo" />
            <span className="brand">RAG GPT</span>
          </div>
          <button
            className="midButton"
            onClick={() => {
              window.location.reload();
            }}
          >
            <img src={addBtn} alt="new chat" className="addButton" />
            New Chat
          </button>
          <div className="upperSideBottom">
            <button
              className="query"
              onClick={handleQuery}
              value={"What is Programming?"}
            >
              <img src={msgIcon} alt="Query" />
            </button>
            <button
              className="query"
              onClick={handleQuery}
              value={"Most demanded jobs"}
            >
              <img src={msgIcon} alt="Query" />
            </button>
          </div>
        </div>
        <div className="lowerSide">
          <div className="listItems">
            <img src={home} alt="home" className="listItemsImg" />
            Home
          </div>
          <div className="listItems">
            <img src={saved} alt="saved" className="listItemsImg" />
            Saved
          </div>
          <div className="listItems">
            <img src={rocket} alt="rocket" className="listItemsImg" />
            Upgrade to Pro
          </div>
        </div>
      </div>
      <div className="main">
        <div className="chats">
          {messages.map((message, i) => (
            <div key={i} className={message.isBot ? "chat bot" : "chat"}>
              <img
                className="chatImg"
                src={message.isBot ? gptImgLogo : userIcon}
                alt=""
              />
              <p className="txt">{message}</p>
            </div>
          ))}
          <div ref={msgEnd} />
        </div>
        <div className="chatFooter">
          <div className="inp">
            <input
              type="text"
              placeholder="Send a message..."
              value={input}
              onChange={(e) => {
                setInput(e.target.value);
              }}
              onKeyDown={handleEnter}
            />
            <button className="send" onClick={handleSend}>
              <img src={sendBtn} alt="send" />
            </button>
          </div>
          <p>Chat GPT may come with incorrect answers</p>
        </div>
      </div>
    </div>
  );
}

export default App;
