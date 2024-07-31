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

function App() {
  return (
    <div className="App">
      <div className="sideBar">
        <div className="upperSide">
          <div className="upperSideTop">
            <img src={gptLogo} alt="Logo" className="logo" />
            <span className="brand">RAG GPT</span>
          </div>
          <button className="midButton">
            <img src={addBtn} alt="new chat" className="addButton" />
            New Chat
          </button>
          <div className="upperSideBottom">
            <button className="query">
              <img src={msgIcon} alt="Query" />
              What is Programming?
            </button>
            <button className="query">
              <img src={msgIcon} alt="Query" />
              Most demanded jobs
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
          <div className="chat">
            <img className="chatImg" src={userIcon} alt="" />
            <p className="txt">
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Distinctio, quidem. Praesentium ipsum eum alias repellendus
              officiis facilis ipsam autem. Dolor et quos eius, incidunt dolorum
              aliquid quisquam non voluptatem suscipit, laborum explicabo nisi
              ducimus sed sit! Doloribus architecto, atque quibusdam quos
              eligendi earum tenetur maiores inventore et iure eveniet obcaecati
              aut voluptatem commodi aperiam voluptatum temporibus quidem
              molestiae aliquid distinctio dolor ratione recusandae sequi
              deserunt! Eum velit dignissimos perspiciatis molestias recusandae!
              Consequatur sequi dolore earum voluptatum est odio voluptas,
              soluta mollitia accusamus officiis animi nostrum saepe, reiciendis
              voluptates quia numquam distinctio molestias tempora consectetur
              eum quod commodi fuga cum. Recusandae!
            </p>
          </div>
          <div className="chat bot">
            <img className="chatImg" src={gptImgLogo} alt="" />
            <p className="txt">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor
              ullam ab ducimus neque officiis placeat facere temporibus eius,
              consequuntur tempora perspiciatis facilis rem aliquam perferendis
              ipsum. Perspiciatis, cum. Voluptatum, perferendis aliquid, dolor
              velit consequuntur cum aliquam consectetur adipisci facere omnis
              consequatur ab quae, provident exercitationem. Corrupti dolores
              adipisci neque suscipit at dicta repudiandae laboriosam numquam
              est reiciendis ipsam aperiam, asperiores officiis, enim ipsa
              placeat nam laudantium nisi perferendis accusantium debitis unde?
              Consequuntur, quia explicabo suscipit, ad magnam inventore sit
              magni, officia accusantium illum adipisci quis reprehenderit
              obcaecati ab pariatur maxime nostrum cupiditate libero minima
              molestiae voluptatem excepturi! Temporibus, exercitationem eius.
            </p>
          </div>
        </div>
        <div className="chatFooter">
          <div className="inp">
            <input type="text" placeholder="Send a message..." />
            <button className="send">
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
