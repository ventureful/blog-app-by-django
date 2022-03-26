import React, { Component } from 'react';


const list = [
  {
    "id":1,
    "title":"Learn Django",
    "body":"Understand how to create basic django powered sites and setup initial configuration"
  },
  {
    "id":2,
    "title":"Study Python builtins",
    "body":"Understand how to use some of the more important Python builtin functions and methods"
  },
  {
    "id":3,
    "title":"Replace os.path with pathlib in repocapp",
    "body":"Learn how to use the Python library pathlib"
  }
]


class App extends Component {
  constructor(props) {
      super(props);
      this.state = { list };
  }
  render() {
    return (
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    );
  }
}


export default App;
